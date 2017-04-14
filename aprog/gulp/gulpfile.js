
const gulp = require('gulp');
const pug = require('gulp-pug');
const stylus = require('gulp-stylus');


gulp.task('pages', function() {

    return gulp
        .src('./source/pages/*.pug')
        .pipe(pug({pretty: true}))
        .pipe(gulp.dest('./public'));

});


gulp.task('styles', function() {

    return gulp
        .src('./source/styles/*.styl')
        .pipe(stylus())
        .pipe(postcss([autoprefixer]))
        .pipe(gulp.dest('./public/css'));

});



gulp.task('watch', function() {

    gulp.watch('./source/**/*.styl', ['styles']);
    gulp.watch('./source/**/*.pug', ['pages']);

});


gulp.task('default', ['pages', 'styles', 'watch']);