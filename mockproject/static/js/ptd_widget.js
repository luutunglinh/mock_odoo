odoo.define('mockproject.ptd_widget', function (require) {
    "use strict";
    // import packages
    var basic_fields = require('web.basic_fields');
    var registry = require('web.field_registry');

    // widget implementation
    var RedWidget = basic_fields.FieldChar.extend({

        _renderReadonly: function () {
            this._super();

            var old_html_render = this.$el.html();
            console.log("1111111111111111111111");
            console.log(basic_fields);
            console.log(old_html_render);
            console.log("1111111111111111111111");
            var new_html_render = '<b style="color:red;">' + old_html_render + '</b>';
            this.$el.html(new_html_render);
        },
    });

    // var BlueWidget = basic_fields.FieldInteger.extend({
    //
    //     _renderReadonly: function () {
    //         this._super();
    //
    //         var old_html_render = this.$el.html();
    //         console.log("1111111111111111111111");
    //         console.log(basic_fields);
    //         console.log(old_html_render);
    //         console.log("1111111111111111111111");
    //
    //         if( old_html_render < 0) {
    //             var new_html_render = '<b style="color:blue;">' + old_html_render + '</b>';
    //         }
    //         else if (old_html_render > 0 & old_html_render < 7) {
    //             var new_html_render = '<b style="color:green;">' + old_html_render + '</b>';
    //         }
    //         else if ( old_html_render >= 7) {
    //             var new_html_render = '<b style="color:yellow;">' + old_html_render + '</b>';
    //         }
    //
    //         // var new_html_render = '<b style="color:blue;">' + old_html_render + '</b>';
    //         this.$el.html(new_html_render);
    //     },
    // });

    var BlueWidget = basic_fields.FieldInteger.extend({

        _renderReadonly: function () {
            this._super();
            var old_html_render = this.$el.html();
            var count = parseInt(old_html_render);
            console.log("1234");
            console.log(typeof count)
            if( count <= 0) {
                var new_html_render = '<b style="color:blue;">' + old_html_render + '</b>';
            }
            else if (count > 0 & count < 7) {
                var new_html_render = '<b style="color:lawngreen;">' + old_html_render + '</b>';
            }
            else if ( count >= 7) {
                var new_html_render = '<b style="color:purple;">' + old_html_render + '</b>';
            }

            this.$el.html(new_html_render);
        },
    });

    registry.add('red_widget', RedWidget); // add our "bold" widget to the widget registry

});