$l = $(".left");
$r = $(".right");

$l.mouseenter(function () {
    $(".container").addClass("left-is-hovered");
}).mouseleave(function () {
    $(".container").removeClass("left-is-hovered");
});

$r.mouseenter(function () {
    $(".container").addClass("right-is-hovered");
}).mouseleave(function () {
    $(".container").removeClass("right-is-hovered");
});

if (annyang) {
    // Add our commands to annyang
    annyang.addCommands({
        // 'hello': function () { alert('Hello world!'); },

        'navigate *page': navigator

    });

    // Tell KITT to use annyang
    SpeechKITT.annyang();

    // Define a stylesheet for KITT to use
    SpeechKITT.setStylesheet('//cdnjs.cloudflare.com/ajax/libs/SpeechKITT/0.3.0/themes/flat.css');

    // Render KITT's interface
    SpeechKITT.vroom();
}

function navigator(page) {
    if (page == new String('media')) window.location.href = "mediaList.html";
    else if (page == new String('video')) window.location.href = "video.html";
    else if (page == new String('home')) window.location.href = "index.html";
}

