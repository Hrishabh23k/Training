/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ListController } from "@web/views/list/list_controller";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { dialog } from "@web/core/dialog/dialog";
import { _t } from "@web/core/l10n/translation";
import { sprintf } from "@web/core/utils/strings";


patch(ListController.prototype, 'device_custom', {

OnCheckClick() {
        console.log("Hello")
        return this.actionService.doAction({
            type: 'ir.actions.act_window',
            res_model: 'display.wizard',
            views: [[false, 'form']],
        });

        },

        OnMyClick() {
        var c = "Hrishabh nagar";
        console.log("Hello Confirmation Dialog")
            this.dialogService.add(ConfirmationDialog, {
                    title: this.env._t("My Model"),
                    body: sprintf(this.env._t("You are getting the model %s"), this.props.resModel)
                });
        }

});

