from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token 
from database.connection import Database

from auth.hash_password import HashPassword
from database.connection import Database

from models.users import User, TokenResponse

user_router = APIRouter(
    tags=["User"],
)



# ============================ sqlalchemy ===================================
# users = {}
# @user_router.post("/signup")
# async def sign_new_user(data: User) -> dict:
#     if data.email in users:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail="User with supplied username exists" 
#         )
#     users[data.email] = data
#     return {
#         "message": "User successfully registered!"
#     }



# @user_router.post("/signin")
# async def sign_user_in(user: UserSignIn) -> dict:
#     if user.email not in users:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User does not exist"
#         )

#     if users[user.email].password != user.password:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Wrong credential passed"
#         )
#     return {
#         "message": "User signed in successfully"
#     }

# # ============================ mongoDB ===================================
# user_database = Database(User)
# @user_router.post("/signup")
# async def sign_new_user(user: User) -> dict:
#     user_exist = await User.find_one(User.email == user.email)
#     if user_exist:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail="User with email provided exists already" 
#         )
#     await user_database.save(user)
#     return {
#         "message": "User successfully registered!"
#     }



# @user_router.post("/signin")
# async def sign_user_in(user: UserSignIn) -> dict:
#     user_exist = await User.find_one(User.email == user.email)
#     if not user_exist:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User does not exist"
#         )

#     if user_exist.password == user.password:
#         return {
#         "message": "User signed in successfully"
#     }

#     raise HTTPException(
#         status_code=status.HTTP_403_FORBIDDEN,
#         detail="Wrong credential passed"
#         )


# ============================ hash_password ===================================
user_database = Database(User)
hash_password = HashPassword()

@user_router.post("/signup")
async def sign_new_user(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email provided exists already" 
        )
    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password
    await user_database.save(user)
    return {
        "message": "User successfully registered!"
    }



@user_router.post("/signin", response_model=TokenResponse)
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends()) -> dict:
    user_exist = await User.find_one(User.email == user.username)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist."
        )
    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed."
    )
    

