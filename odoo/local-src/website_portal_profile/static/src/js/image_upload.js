odoo.define('website_portal_profile.image_upload', function (require) {
"use strict";

var core = require('web.core');
var website = require('website.website');

if(!$('.o_website_portal_details').length) {
    return $.Deferred().reject("DOM doesn't contain '.o_website_portal_details'");
}
    $('.imgupload').imgupload();

});
