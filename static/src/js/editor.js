odoo.define('jt_webeditor_extras.toolbar_extras', function (require) {
    'use strict';

    const weToolbar = require('web_editor.toolbar');

    weToolbar.include({
        xmlDependencies: (weToolbar.prototype.xmlDependencies || []).concat(
            ['/jt_webeditor_extras/static/src/xml/editor.xml']),
    });

    console.log(weToolbar.prototype.xmlDependencies);

});
