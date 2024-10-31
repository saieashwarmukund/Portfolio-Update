var $d = $( ".art" ), 
    tallestDivHeight = 0


$d.each(function (i, v) {
    var $t = $(this), 
        thisDivsHeight = $t.outerHeight()

    console.log(thisDivsHeight)

    if(thisDivsHeight > tallestDivHeight) tallestDivHeight = thisDivsHeight
})


$d.css('height', tallestDivHeight)