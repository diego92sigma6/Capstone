(this.webpackJsonpPhoneApp=this.webpackJsonpPhoneApp||[]).push([[50],{131:function(o,t,n){"use strict";n.r(t),n.d(t,"ion_button",(function(){return s})),n.d(t,"ion_icon",(function(){return g}));var r,i=n(25),e=(n(3),n(19)),a=n(203),s=function(){function o(o){var t=this;Object(i.l)(this,o),this.inToolbar=!1,this.inItem=!1,this.buttonType="button",this.disabled=!1,this.routerDirection="forward",this.strong=!1,this.type="button",this.handleClick=function(o){if("button"===t.type)Object(a.d)(t.href,o,t.routerDirection);else if(Object(e.g)(t.el)){var n=t.el.closest("form");if(n){o.preventDefault();var r=document.createElement("button");r.type=t.type,r.style.display="none",n.appendChild(r),r.click(),r.remove()}}},this.onFocus=function(){t.ionFocus.emit()},this.onBlur=function(){t.ionBlur.emit()},this.ionFocus=Object(i.d)(this,"ionFocus",7),this.ionBlur=Object(i.d)(this,"ionBlur",7)}return o.prototype.componentWillLoad=function(){this.inToolbar=!!this.el.closest("ion-buttons"),this.inItem=!!this.el.closest("ion-item")||!!this.el.closest("ion-item-divider")},Object.defineProperty(o.prototype,"hasIconOnly",{get:function(){return!!this.el.querySelector('ion-icon[slot="icon-only"]')},enumerable:!0,configurable:!0}),Object.defineProperty(o.prototype,"rippleType",{get:function(){return(void 0===this.fill||"clear"===this.fill)&&this.hasIconOnly&&this.inToolbar?"unbounded":"bounded"},enumerable:!0,configurable:!0}),o.prototype.render=function(){var o,t=Object(i.e)(this),n=this,r=n.buttonType,e=n.type,s=n.disabled,c=n.rel,l=n.target,d=n.size,u=n.href,b=n.color,h=n.expand,f=n.hasIconOnly,p=n.shape,g=n.strong,v=void 0===d&&this.inItem?"small":d,m=void 0===u?"button":"a",y="button"===m?{type:e}:{download:this.download,href:u,rel:c,target:l},w=this.fill;return void 0===w&&(w=this.inToolbar?"clear":"solid"),Object(i.i)(i.a,{onClick:this.handleClick,"aria-disabled":s?"true":null,class:Object.assign(Object.assign({},Object(a.a)(b)),(o={},o[t]=!0,o[r]=!0,o[r+"-"+h]=void 0!==h,o[r+"-"+v]=void 0!==v,o[r+"-"+p]=void 0!==p,o[r+"-"+w]=!0,o[r+"-strong"]=g,o["button-has-icon-only"]=f,o["button-disabled"]=s,o["ion-activatable"]=!0,o["ion-focusable"]=!0,o))},Object(i.i)(m,Object.assign({},y,{class:"button-native",disabled:s,onFocus:this.onFocus,onBlur:this.onBlur}),Object(i.i)("span",{class:"button-inner"},Object(i.i)("slot",{name:"icon-only"}),Object(i.i)("slot",{name:"start"}),Object(i.i)("slot",null),Object(i.i)("slot",{name:"end"})),"md"===t&&Object(i.i)("ion-ripple-effect",{type:this.rippleType})))},Object.defineProperty(o.prototype,"el",{get:function(){return Object(i.f)(this)},enumerable:!0,configurable:!0}),Object.defineProperty(o,"style",{get:function(){return":host{--overflow:hidden;--ripple-color:currentColor;--border-width:initial;--border-color:initial;--border-style:initial;--color-hover:initial;--box-shadow:none;display:inline-block;width:auto;color:var(--color);font-family:var(--ion-font-family,inherit);text-align:center;text-decoration:none;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;vertical-align:top;vertical-align:-webkit-baseline-middle;pointer-events:auto;-webkit-font-kerning:none;font-kerning:none}:host(.button-disabled){--opacity:.5;pointer-events:none}:host(.button-disabled) .button-native{cursor:default;pointer-events:none}:host(.button-solid){--background:var(--ion-color-primary,#3880ff);--background-focused:var(--ion-color-primary-shade,#3171e0);--background-hover:var(--ion-color-primary-tint,#4c8dff);--color:var(--ion-color-primary-contrast,#fff);--color-activated:var(--ion-color-primary-contrast,#fff);--color-focused:var(--ion-color-primary-contrast,#fff)}:host(.button-solid.ion-color) .button-native{background:var(--ion-color-base);color:var(--ion-color-contrast)}:host(.button-solid.ion-color.ion-focused) .button-native{background:var(--ion-color-shade)}:host(.button-outline){--border-color:var(--ion-color-primary,#3880ff);--background:transparent;--color:var(--ion-color-primary,#3880ff);--color-focused:var(--ion-color-primary,#3880ff)}:host(.button-outline.ion-color) .button-native{border-color:var(--ion-color-base);background:transparent;color:var(--ion-color-base)}:host(.button-outline.ion-focused.ion-color) .button-native{background:rgba(var(--ion-color-base-rgb),.1);color:var(--ion-color-base)}:host(.button-clear){--border-width:0;--background:transparent;--color:var(--ion-color-primary,#3880ff)}:host(.button-clear.ion-color) .button-native{background:transparent;color:var(--ion-color-base)}:host(.button-clear.ion-focused.ion-color) .button-native{background:rgba(var(--ion-color-base-rgb),.1);color:var(--ion-color-base)}:host(.button-clear.activated.ion-color) .button-native{background:transparent}:host(.button-block){display:block}:host(.button-block) .button-native{margin-left:0;margin-right:0;display:block;width:100%;clear:both;contain:content}:host(.button-block) .button-native:after{clear:both}:host(.button-full){display:block}:host(.button-full) .button-native{margin-left:0;margin-right:0;display:block;width:100%;contain:content}:host(.button-full:not(.button-round)) .button-native{border-radius:0;border-right-width:0;border-left-width:0}.button-native{border-radius:var(--border-radius);-moz-osx-font-smoothing:grayscale;-webkit-font-smoothing:antialiased;margin-left:0;margin-right:0;margin-top:0;margin-bottom:0;padding-left:var(--padding-start);padding-right:var(--padding-end);padding-top:var(--padding-top);padding-bottom:var(--padding-bottom);font-family:inherit;font-size:inherit;font-style:inherit;font-weight:inherit;letter-spacing:inherit;text-decoration:inherit;text-overflow:inherit;text-transform:inherit;text-align:inherit;white-space:inherit;color:inherit;display:block;position:relative;width:100%;height:100%;-webkit-transition:var(--transition);transition:var(--transition);border-width:var(--border-width);border-style:var(--border-style);border-color:var(--border-color);outline:none;background:var(--background);line-height:1;-webkit-box-shadow:var(--box-shadow);box-shadow:var(--box-shadow);contain:layout style;cursor:pointer;opacity:var(--opacity);overflow:var(--overflow);z-index:0;-webkit-box-sizing:border-box;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}@supports ((-webkit-margin-start:0) or (margin-inline-start:0)) or (-webkit-margin-start:0){.button-native{padding-left:unset;padding-right:unset;-webkit-padding-start:var(--padding-start);padding-inline-start:var(--padding-start);-webkit-padding-end:var(--padding-end);padding-inline-end:var(--padding-end)}}.button-native::-moz-focus-inner{border:0}.button-inner{display:-ms-flexbox;display:flex;-ms-flex-flow:row nowrap;flex-flow:row nowrap;-ms-flex-negative:0;flex-shrink:0;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center;width:100%;height:100%}::slotted(ion-icon){font-size:1.4em;pointer-events:none}::slotted(ion-icon[slot=start]){margin-left:-.3em;margin-right:.3em;margin-top:0;margin-bottom:0}@supports ((-webkit-margin-start:0) or (margin-inline-start:0)) or (-webkit-margin-start:0){::slotted(ion-icon[slot=start]){margin-left:unset;margin-right:unset;-webkit-margin-start:-.3em;margin-inline-start:-.3em;-webkit-margin-end:.3em;margin-inline-end:.3em}}::slotted(ion-icon[slot=end]){margin-left:.3em;margin-right:-.2em;margin-top:0;margin-bottom:0}@supports ((-webkit-margin-start:0) or (margin-inline-start:0)) or (-webkit-margin-start:0){::slotted(ion-icon[slot=end]){margin-left:unset;margin-right:unset;-webkit-margin-start:.3em;margin-inline-start:.3em;-webkit-margin-end:-.2em;margin-inline-end:-.2em}}::slotted(ion-icon[slot=icon-only]){font-size:1.8em}ion-ripple-effect{color:var(--ripple-color)}:host(.ion-focused) .button-native{background:var(--background-focused);color:var(--color-focused)}:host(.activated) .button-native{background:var(--background-activated);color:var(--color-activated)}@media (any-hover:hover){:host(:hover) .button-native{background:var(--background-hover);color:var(--color-hover)}}:host{--border-radius:10px;--padding-top:0;--padding-bottom:0;--padding-start:1em;--padding-end:1em;--transition:background-color,opacity 100ms linear;margin-left:2px;margin-right:2px;margin-top:4px;margin-bottom:4px;height:2.8em;font-size:16px;font-weight:500;letter-spacing:-.03em}@supports ((-webkit-margin-start:0) or (margin-inline-start:0)) or (-webkit-margin-start:0){:host{margin-left:unset;margin-right:unset;-webkit-margin-start:2px;margin-inline-start:2px;-webkit-margin-end:2px;margin-inline-end:2px}}:host(.button-solid){--background-activated:var(--ion-color-primary-shade,#3171e0)}:host(.button-solid.activated){--opacity:1}:host(.button-solid.activated.ion-color) .button-native{background:var(--ion-color-shade)}:host(.button-outline){--border-radius:10px;--border-width:1px;--border-style:solid;--background-activated:var(--ion-color-primary,#3880ff);--background-focused:rgba(var(--ion-color-primary-rgb,56,128,255),0.1);--color-activated:var(--ion-color-primary-contrast,#fff)}:host(.button-outline.activated.ion-color) .button-native{background:var(--ion-color-base);color:var(--ion-color-contrast)}:host(.button-clear.activated){--opacity:0.4}:host(.button-clear){--background-activated:transparent;--background-focused:rgba(var(--ion-color-primary-rgb,56,128,255),0.1);--color-activated:var(--ion-color-primary,#3880ff);--color-focused:var(--ion-color-primary,#3880ff)}:host(.button-large){--border-radius:12px;--padding-top:0;--padding-start:1em;--padding-end:1em;--padding-bottom:0;height:2.8em;font-size:20px}:host(.button-small){--border-radius:6px;--padding-top:0;--padding-start:0.9em;--padding-end:0.9em;--padding-bottom:0;height:2.1em;font-size:13px}:host(.button-round){--border-radius:64px;--padding-top:0;--padding-start:26px;--padding-end:26px;--padding-bottom:0}:host(.button-strong){font-weight:600}@media (any-hover:hover){:host(.button-solid:hover){--opacity:0.8}:host(.button-clear:hover),:host(.button-outline:hover){--opacity:0.6}:host(.ion-focused:hover){--background-hover:var(--background-focused);--color-hover:var(--color-focused)}:host(.activated:hover){--background-hover:var(--background-activated);--color-hover:var(--color-activated)}}"},enumerable:!0,configurable:!0}),o}(),c=function(o){var t=function(){if(!r){var o=window;o.Ionicons=o.Ionicons||{},r=o.Ionicons.map=o.Ionicons.map||new Map}return r}().get(o);return t||Object(i.j)("svg/"+o+".svg")},l=function(o,t,n,r,i){return n="ios"===(n&&n.toLowerCase())?"ios":"md",r&&"ios"===n?o=r.toLowerCase():i&&"md"===n?o=i.toLowerCase():(o||!t||u(t)||(o=t),b(o)&&(o=o.toLowerCase(),/^md-|^ios-|^logo-/.test(o)||(o=n+"-"+o))),b(o)&&""!==o.trim()?""!==o.replace(/[a-z]|-|\d/gi,"")?null:o:null},d=function(o){return b(o)&&(o=o.trim(),u(o))?o:null},u=function(o){return o.length>0&&/(\/|\.)/.test(o)},b=function(o){return"string"===typeof o},h=function o(t){if(1===t.nodeType){if("script"===t.nodeName.toLowerCase())return!1;for(var n=0;n<t.attributes.length;n++){var r=t.attributes[n].value;if(b(r)&&0===r.toLowerCase().indexOf("on"))return!1}for(n=0;n<t.childNodes.length;n++)if(!o(t.childNodes[n]))return!1}return!0},f=new Map,p=function(o){var t=f.get(o);return t||(t=fetch(o).then((function(o){return o.status<=299?o.text():Promise.resolve(null)})).then((function(o){return function(o){if(o){var t=document.createElement("div");t.innerHTML=o;for(var n=t.childNodes.length-1;n>=0;n--)"svg"!==t.childNodes[n].nodeName.toLowerCase()&&t.removeChild(t.childNodes[n]);var r=t.firstElementChild;if(r&&"svg"===r.nodeName.toLowerCase()&&(r.setAttribute("class","s-ion-icon"),h(r)))return t.innerHTML}return""}(o)})),f.set(o,t)),t},g=function(){function o(o){Object(i.l)(this,o),this.mode=v(this),this.isVisible=!1,this.lazy=!1}return o.prototype.connectedCallback=function(){var o=this;this.waitUntilVisible(this.el,"50px",(function(){o.isVisible=!0,o.loadIcon()}))},o.prototype.disconnectedCallback=function(){this.io&&(this.io.disconnect(),this.io=void 0)},o.prototype.waitUntilVisible=function(o,t,n){var r=this;if(this.lazy&&"undefined"!==typeof window&&window.IntersectionObserver){var i=this.io=new window.IntersectionObserver((function(o){o[0].isIntersecting&&(i.disconnect(),r.io=void 0,n())}),{rootMargin:t});i.observe(o)}else n()},o.prototype.loadIcon=function(){var o=this;if(this.isVisible){var t=function(o){var t=d(o.src);if(t)return t;if(t=l(o.name,o.icon,o.mode,o.ios,o.md))return c(t);if(o.icon){if(t=d(o.icon))return t;if(t=d(o.icon[o.mode]))return t}return null}(this);t&&p(t).then((function(t){return o.svgContent=t}))}if(!this.ariaLabel){var n=l(this.name,this.icon,this.mode,this.ios,this.md);n&&(this.ariaLabel=n.replace("ios-","").replace("md-","").replace(/\-/g," "))}},o.prototype.render=function(){var o,t,n=this.mode||"md",r=this.flipRtl||this.ariaLabel&&this.ariaLabel.indexOf("arrow")>-1&&!1!==this.flipRtl;return Object(i.i)(i.a,{role:"img",class:Object.assign((o={},o[n]=!0,o),m(this.color),(t={},t["icon-"+this.size]=!!this.size,t["flip-rtl"]=!!r&&"rtl"===this.el.ownerDocument.dir,t))},this.svgContent?Object(i.i)("div",{class:"icon-inner",innerHTML:this.svgContent}):Object(i.i)("div",{class:"icon-inner"}))},Object.defineProperty(o,"assetsDirs",{get:function(){return["svg"]},enumerable:!0,configurable:!0}),Object.defineProperty(o.prototype,"el",{get:function(){return Object(i.f)(this)},enumerable:!0,configurable:!0}),Object.defineProperty(o,"watchers",{get:function(){return{name:["loadIcon"],src:["loadIcon"],icon:["loadIcon"]}},enumerable:!0,configurable:!0}),Object.defineProperty(o,"style",{get:function(){return":host{display:inline-block;width:1em;height:1em;contain:strict;fill:currentColor;-webkit-box-sizing:content-box!important;box-sizing:content-box!important}.icon-inner,svg{display:block;height:100%;width:100%}:host(.flip-rtl) .icon-inner{-webkit-transform:scaleX(-1);transform:scaleX(-1)}:host(.icon-small){font-size:18px!important}:host(.icon-large){font-size:32px!important}:host(.ion-color){color:var(--ion-color-base)!important}:host(.ion-color-primary){--ion-color-base:var(--ion-color-primary,#3880ff)}:host(.ion-color-secondary){--ion-color-base:var(--ion-color-secondary,#0cd1e8)}:host(.ion-color-tertiary){--ion-color-base:var(--ion-color-tertiary,#f4a942)}:host(.ion-color-success){--ion-color-base:var(--ion-color-success,#10dc60)}:host(.ion-color-warning){--ion-color-base:var(--ion-color-warning,#ffce00)}:host(.ion-color-danger){--ion-color-base:var(--ion-color-danger,#f14141)}:host(.ion-color-light){--ion-color-base:var(--ion-color-light,#f4f5f8)}:host(.ion-color-medium){--ion-color-base:var(--ion-color-medium,#989aa2)}:host(.ion-color-dark){--ion-color-base:var(--ion-color-dark,#222428)}"},enumerable:!0,configurable:!0}),o}(),v=function(o){return Object(i.k)(o)||document.documentElement.getAttribute("mode")||"md"},m=function(o){var t;return o?((t={"ion-color":!0})["ion-color-"+o]=!0,t):null}},203:function(o,t,n){"use strict";n.d(t,"a",(function(){return e})),n.d(t,"b",(function(){return a})),n.d(t,"c",(function(){return i})),n.d(t,"d",(function(){return c}));var r=n(1),i=function(o,t){return null!==t.closest(o)},e=function(o){var t;return"string"===typeof o&&o.length>0?((t={"ion-color":!0})["ion-color-"+o]=!0,t):void 0},a=function(o){var t={};return function(o){return void 0!==o?(Array.isArray(o)?o:o.split(" ")).filter((function(o){return null!=o})).map((function(o){return o.trim()})).filter((function(o){return""!==o})):[]}(o).forEach((function(o){return t[o]=!0})),t},s=/^[a-z][a-z0-9+\-.]*:/,c=function(o,t,n){return Object(r.a)(void 0,void 0,void 0,(function(){var i;return Object(r.c)(this,(function(r){return null!=o&&"#"!==o[0]&&!s.test(o)&&(i=document.querySelector("ion-router"))?(null!=t&&t.preventDefault(),[2,i.push(o,n)]):[2,!1]}))}))}}}]);
//# sourceMappingURL=50.4c80ec14.chunk.js.map