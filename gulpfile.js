var gulp = require('gulp')
var { spawn } = require('child_process')
var sass = require('gulp-sass')

gulp.task('django:runserver', () => {
  spawn('python3', ['manage.py', 'runserver', '0.0.0.0:8000'], {
    stdio: 'inherit'
  })
})

gulp.task('sass:build', () => {
  gulp.src('./media/css/base.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./static/css'))
})

gulp.task('sass:watch', () => {
  gulp.watch('./media/css/*', ['sass:build'])
})

gulp.task('js:build', () => {
  gulp.src(['./node_modules/jquery/dist/jquery.slim.min.js',
            './node_modules/bootstrap/dist/js/bootstrap.bundle.min.js',
            './node_modules/d3/build/d3.min.js',
            './node_modules/metrics-graphics/dist/metricsgraphics.min.js'])
    .pipe(gulp.dest('./static/js'))
})

gulp.task('build', () => {
  gulp.start('sass:build')
  gulp.start('js:build')
})

gulp.task('default', () => {
  gulp.start('build')
  gulp.start('django:runserver')
  gulp.start('sass:watch')
})
