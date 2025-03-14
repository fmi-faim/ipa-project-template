document$.subscribe(function() {
    var elements = document.getElementsByTagName("input");
    for (var ii=0; ii < elements.length; ii++) {
      if (elements[ii].type == "text") {
        elements[ii].dispatchEvent(new Event("input"));
      }
    }
});
