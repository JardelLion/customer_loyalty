/** @odoo-module **/
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component } from "@odoo/owl";

export class LoyaltyPointsWidget extends Component {
    static template = "customer_loyalty.LoyaltyPointsWidget";
    static props = {
        ...standardFieldProps,
    };

    get totalPoints() {
        return this.props.record.data[this.props.name] || 0;
    }

    get rawLevel() {
        return (this.props.record.data.loyalty_level || 'bronze').toLowerCase();
    }

    get loyaltyLevel() {
        return this.rawLevel.toUpperCase();
    }

    get levelImage() {
        const level = this.rawLevel;
        const validLevels = ['bronze', 'silver', 'gold'];
        const currentLevel = validLevels.includes(level) ? level : 'bronze';
        
        return `/customer_loyalty/static/src/img/${currentLevel}.png`;
    }
}

export const loyaltyPointsWidget = {
    component: LoyaltyPointsWidget,
    supportedTypes: ["float", "integer"],
};

registry.category("fields").add("loyalty_points_badge", loyaltyPointsWidget);