odoo.define('l10n_fr_pos_cert.pos', function (require) {
"use strict";

const { Gui } = require('point_of_sale.Gui');
var { PosGlobalState, Order, Orderline } = require('point_of_sale.models');
var core = require('web.core');
const Registries = require('point_of_sale.Registries');

var _t = core._t;

const L10nFrPosGlobalState = (PosGlobalState) => class L10nFrPosGlobalState extends PosGlobalState {
    is_french_country(){
      var french_countries = ['FR', 'MF', 'MQ', 'NC', 'PF', 'RE', 'GF', 'GP', 'TF'];
      if (!this.company.country) {
        Gui.showPopup("ErrorPopup", {
            'title': _t("Missing Country"),
            'body':  _.str.sprintf(_t('The company %s doesn\'t have a country set.'), this.company.name),
        });
        return false;
      }
      return _.contains(french_countries, this.company.country.code);
    }
    disallowLineQuantityChange() {
        let result = super.disallowLineQuantityChange(...arguments);
        return this.is_french_country() || result;
    }
}
Registries.Model.extend(PosGlobalState, L10nFrPosGlobalState);


const L10nFrOrder = (Order) => class L10nFrOrder extends Order {
    constructor() {
        super(...arguments);
        this.l10n_fr_hash = this.l10n_fr_hash || false;
        this.save_to_db();
    }
    export_for_printing() {
      var result = super.export_for_printing(...arguments);
      result.l10n_fr_hash = this.get_l10n_fr_hash();
      return result;
    }
    set_l10n_fr_hash (l10n_fr_hash){
      this.l10n_fr_hash = l10n_fr_hash;
    }
    get_l10n_fr_hash() {
      return this.l10n_fr_hash;
    }
    wait_for_push_order() {
      var result = super.wait_for_push_order(...arguments);
      result = Boolean(result || this.pos.is_french_country());
      return result;
    }
    destroy (option) {
        // SUGGESTION: It's probably more appropriate to apply this restriction
        // in the TicketScreen.
        if (option && option.reason == 'abandon' && this.pos.is_french_country() && this.get_orderlines().length) {
            Gui.showPopup("ErrorPopup", {
                'title': _t("Fiscal Data Module error"),
                'body':  _t("Deleting of orders is not allowed."),
            });
        } else {
            super.destroy(...arguments);
        }
    }
}
Registries.Model.extend(Order, L10nFrOrder);


const L10nFrOrderline = (Orderline) => class L10nFrOrderline extends Orderline {
    can_be_merged_with(orderline) {
        let order = this.pos.get_order();
        let orderlines = order.orderlines;
        let lastOrderline = order.orderlines.at(orderlines.length - 1);

        if(this.pos.is_french_country() && (lastOrderline.product.id !== orderline.product.id || lastOrderline.quantity < 0)) {
            return false;
        } else {
            return super.can_be_merged_with(...arguments);
        }
    }
}
Registries.Model.extend(Orderline, L10nFrOrderline);

});
