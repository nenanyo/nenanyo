const Genre = require("../models/genre");
const Book = require("../models/book");

const asyncHandler = require("express-async-handler");
const { body, validationResult } = require("express-validator");


// 장르 목록
exports.genre_list = asyncHandler(async (req, res, next) => {
  const allGenres = await Genre.find().sort({ name: 1 }).exec();
  res.render("genre_list", {
    title: "Genre List",
    list_genres: allGenres,
  });
});

// 특정 장르 페이지
exports.genre_detail = asyncHandler(async (req, res, next) => {
  // 장르의 세부 정보와 관련된 모든 책 - 병렬
  const [genre, booksInGenre] = await Promise.all([
    Genre.findById(req.params.id).exec(),
    Book.find({ genre: req.params.id }, "title summary").exec(),
  ]);
  if (genre === null) {
    // No results.
    const err = new Error("Genre not found");
    err.status = 404;
    return next(err);
  }

  res.render("genre_detail", {
    title: "Genre Detail",
    genre: genre,
    genre_books: booksInGenre,
  });
});


// 장르 저장 폼 불러오기 - GET
exports.genre_create_get = (req, res, next) => {
  res.render("genre_form", { title: "Create Genre" });
};

// 장르 저장 - POST
exports.genre_create_post = [
  // 'name' 값을 검증하고 위해코드 정리
  body("name", "Genre name must contain at least 3 characters")
    .trim()
    .isLength({ min: 3 })
    .escape(),

  // 프로세스 진행
  asyncHandler(async (req, res, next) => {
    // 에러값
    const errors = validationResult(req);

    // 장르 객체 생성
    const genre = new Genre({ name: req.body.name });

    if (!errors.isEmpty()) {
      // 에러 있음. 위해코드 정리후에 폼으로 돌아감
      res.render("genre_form", {
        title: "Create Genre",
        genre: genre,
        errors: errors.array(),
      });
      return;
    } else {
      // 데이터 값이 유효함
      // 같은 장르가 있는지 확인
      // 대소문자 구분 없이 장르 이름으로 검색 (collation 설정)
      const genreExists = await Genre.findOne({ name: req.body.name })
        .collation({ locale: "en", strength: 2 })
        .exec();
      if (genreExists) {
        // 이미 있다면, 디테일 페이지로
        res.redirect(genreExists.url);
      } else {
        await genre.save();
        // 장르 저장, 디테일 페이지로
        res.redirect(genre.url);
      }
    }
  }),
];


// 장르 삭제 폼 불러오기 - GET
exports.genre_delete_get = asyncHandler(async (req, res, next) => {
  // 병렬로 장르와 모든 관련된 책 불러오기
  const [genre, booksInGenre] = await Promise.all([
    Genre.findById(req.params.id).exec(),
    Book.find({ genre: req.params.id }, "title summary").exec(),
  ]);
  if (genre === null) {
    // No results.
    res.redirect("/catalog/genres");
  }

  res.render("genre_delete", {
    title: "Delete Genre",
    genre: genre,
    genre_books: booksInGenre,
  });
});

// 장르 삭제 - POST
exports.genre_delete_post = asyncHandler(async (req, res, next) => {
  // 병렬로 장르와 모든 관련된 책 불러오기
  const [genre, booksInGenre] = await Promise.all([
    Genre.findById(req.params.id).exec(),
    Book.find({ genre: req.params.id }, "title summary").exec(),
  ]);

  if (booksInGenre.length > 0) {
    // 관련 책이 있음. get route 와 같은 방식으로 렌더
    res.render("genre_delete", {
      title: "Delete Genre",
      genre: genre,
      genre_books: booksInGenre,
    });
    return;
  } else {
    // Genre has no books. Delete object and redirect to the list of genres.
    // 관련 책이 없음. 객체 삭제 및 장르 목록으로 리다이렉트
    await Genre.findByIdAndDelete(req.body.id);
    res.redirect("/catalog/genres");
  }
});

// 장르 수정 폼 불러오기 - GET
exports.genre_update_get = asyncHandler(async (req, res, next) => {
  const genre = await Genre.findById(req.params.id).exec();

  if (genre === null) {
    // 데이터 없음
    const err = new Error("Genre not found");
    err.status = 404;
    return next(err);
  }

  res.render("genre_form", { title: "Update Genre", genre: genre });
});

// 장르 수정 - POST
exports.genre_update_post = [
  body("name", "Genre name must contain at least 3 characters")
    .trim()
    .isLength({ min: 3 })
    .escape(),

  asyncHandler(async (req, res, next) => {
    const errors = validationResult(req);

    // 장르 객체 생성 (기존 id + 새로운 데이터)
    const genre = new Genre({
      name: req.body.name,
      _id: req.params.id,
    });

    if (!errors.isEmpty()) {
      // 에러 존재
      res.render("genre_form", {
        title: "Update Genre",
        genre: genre,
        errors: errors.array(),
      });
      return;
    } else {
      // 데이터 유효. 데이터 갱신
      await Genre.findByIdAndUpdate(req.params.id, genre);
      res.redirect(genre.url);
    }
  }),
];
