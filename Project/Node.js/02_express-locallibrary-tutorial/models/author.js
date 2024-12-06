const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const AuthorSchema = new Schema({
  first_name: { type: String, required: true, maxLength: 100 },
  family_name: { type: String, required: true, maxLength: 100 },
  date_of_birth: { type: Date },
  date_of_death: { type: Date },
});

// 작가의 풀네임
AuthorSchema.virtual("name").get(function () {
  // 성이 없는 예외의 경우 허용
  let fullname = "";
  if (this.first_name && this.family_name) {
    fullname = `${this.family_name}, ${this.first_name}`;
  }

  return fullname;
});

// author's URL
AuthorSchema.virtual("url").get(function () {  
  return `/catalog/author/${this._id}`;
});


module.exports = mongoose.model("Author", AuthorSchema);
