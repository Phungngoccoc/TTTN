odoo.define("custom_snippet.options", function(require) {
    "use strict";

    var options = require("web_editor.snippets.options");

    options.registry.s_custom_snippet = options.Class.extend({
        onBuilt: function() {
            this._super();
            console.log("Snippet options initialized");
        },
    });
});