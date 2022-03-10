// Sass configuration
var gulp = require('gulp');
var concat = require('gulp-concat');  
var sass = require('gulp-sass')(require('sass'));


gulp.task('sass', function(cb) {
  gulp
    .src('scss/custom.scss')
    .pipe(concat('styles.css'))
    .pipe(sass())
    .pipe(
      gulp.dest('static/')
    ).on('end', cb);
});

gulp.task(  
  'default',
  gulp.series('sass', function(cb) {
    gulp.watch('scss/custom.scss', gulp.series('sass'));
    cb();
  })
);