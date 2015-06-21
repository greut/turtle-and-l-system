var gulp = require('gulp'),
    util = require('gulp-util'),
    fs = require('fs'),
    path = require('path'),
    through = require('through2'),
    markdown = require('gulp-markdown'),
    pygmentize = require('pygmentize-bundled'),
    handlebars = require('handlebars'),
    rename = require('gulp-rename'),
    data = require('gulp-data'),
    frontMatter = require('gulp-front-matter')

function applyTemplate(template) {
    var tpl = handlebars.compile(fs.readFileSync(path.join(__dirname, template), "utf-8"))

    return through.obj(function(file, enc, cb) {
        var data = {
            page: file.page,
            contents: file.contents.toString()
        }

        file.contents = new Buffer(tpl(data), enc)
        this.push(file)
        cb()
    })
}

gulp.task('default', function() {
    return gulp.src([
            'docs/*.md',
        ]).
        pipe(frontMatter({
            property: 'page',
            remove: true
        })).
        pipe(markdown({
            highlight: function(code, lang, callback) {
                //return highlight.highlight(code).value
                return pygmentize({lang: lang, format: 'html'}, code, function(err, result) {
                     callback(err, result.toString())
                })
            }
        })).
        pipe(applyTemplate('design/page.html')).
        pipe(gulp.dest('dist'))
})
