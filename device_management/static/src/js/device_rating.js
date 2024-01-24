/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, xml } from "@odoo/owl";

class Rating extends Component{
    setup(){
        console.log("Star Rating")
       };

};

Rating.template = "device_management.star_template";

registry.category("fields").add("rating", Rating);
