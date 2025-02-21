odoo.define("custom_snippet.s_custom_snippet", function(require) {
    "use strict";

    var publicWidget = require("web.public.widget");

    publicWidget.registry.sCustomSnippet = publicWidget.Widget.extend({
        selector: ".s_custom_snippet",
        start: function() {
            console.log("Custom snippet loaded!");
        },
    });
});