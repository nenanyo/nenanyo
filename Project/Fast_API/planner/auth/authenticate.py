from auth.jwt_handler import verify_access_token
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

"""
Depends: oauth2_schema를 의존 라이브러리 함수에 주입
OAuth2PasswordBearer:보안 로직이 존재한다는 것을 앱에 알림
verify_access_token: 앞서 정의한 토큰 생성 및 검증 함수로, 토큰의 유효성 확인
"""

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/signin")


async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Sign in for access"
        )

    decoded_token = verify_access_token(token)
    return decoded_token["user"]