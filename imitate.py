<!DOCTYPE html>
<html lang="en">
<head>
  <meta id="bb-bootstrap" data-current-user="{&quot;username&quot;: &quot;rbhattacharyya&quot;, &quot;displayName&quot;: &quot;Raunak Pushpak Bhattacharyya&quot;, &quot;uuid&quot;: &quot;{9113a1a1-daee-4e75-bfd9-5e0f0bcc8ae1}&quot;, &quot;firstName&quot;: &quot;Raunak Pushpak Bhattacharyya&quot;, &quot;hasPremium&quot;: false, &quot;lastName&quot;: &quot;&quot;, &quot;avatarUrl&quot;: &quot;https://bitbucket.org/account/rbhattacharyya/avatar/32/?ts=1519424381&quot;, &quot;isTeam&quot;: false, &quot;isSshEnabled&quot;: false, &quot;isKbdShortcutsEnabled&quot;: true, &quot;id&quot;: 10931899, &quot;isAuthenticated&quot;: true}"
data-atlassian-id="5a5f86707b4e6b6c2a81aad2" />
  
  
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta charset="utf-8">
  <title>
  sisl / Multiagent_GAIL 
  / source  / ngsim_env / scripts / imitation / imitate.py
 &mdash; Bitbucket
</title>
  <script type="text/javascript">(window.NREUM||(NREUM={})).loader_config={xpid:"VwMGVVZSGwIIUFBQDwU="};window.NREUM||(NREUM={}),__nr_require=function(t,n,e){function r(e){if(!n[e]){var o=n[e]={exports:{}};t[e][0].call(o.exports,function(n){var o=t[e][1][n];return r(o||n)},o,o.exports)}return n[e].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<e.length;o++)r(e[o]);return r}({1:[function(t,n,e){function r(t){try{s.console&&console.log(t)}catch(n){}}var o,i=t("ee"),a=t(15),s={};try{o=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(s.console=!0,o.indexOf("dev")!==-1&&(s.dev=!0),o.indexOf("nr_dev")!==-1&&(s.nrDev=!0))}catch(c){}s.nrDev&&i.on("internal-error",function(t){r(t.stack)}),s.dev&&i.on("fn-err",function(t,n,e){r(e.stack)}),s.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(s,function(t,n){return t}).join(", ")))},{}],2:[function(t,n,e){function r(t,n,e,r,s){try{p?p-=1:o(s||new UncaughtException(t,n,e),!0)}catch(f){try{i("ierr",[f,c.now(),!0])}catch(d){}}return"function"==typeof u&&u.apply(this,a(arguments))}function UncaughtException(t,n,e){this.message=t||"Uncaught error with no additional information",this.sourceURL=n,this.line=e}function o(t,n){var e=n?null:c.now();i("err",[t,e])}var i=t("handle"),a=t(16),s=t("ee"),c=t("loader"),f=t("gos"),u=window.onerror,d=!1,l="nr@seenError",p=0;c.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(h){"stack"in h&&(t(8),t(7),"addEventListener"in window&&t(5),c.xhrWrappable&&t(9),d=!0)}s.on("fn-start",function(t,n,e){d&&(p+=1)}),s.on("fn-err",function(t,n,e){d&&!e[l]&&(f(e,l,function(){return!0}),this.thrown=!0,o(e))}),s.on("fn-end",function(){d&&!this.thrown&&p>0&&(p-=1)}),s.on("internal-error",function(t){i("ierr",[t,c.now(),!0])})},{}],3:[function(t,n,e){t("loader").features.ins=!0},{}],4:[function(t,n,e){function r(t){}if(window.performance&&window.performance.timing&&window.performance.getEntriesByType){var o=t("ee"),i=t("handle"),a=t(8),s=t(7),c="learResourceTimings",f="addEventListener",u="resourcetimingbufferfull",d="bstResource",l="resource",p="-start",h="-end",m="fn"+p,w="fn"+h,v="bstTimer",y="pushState",g=t("loader");g.features.stn=!0,t(6);var b=NREUM.o.EV;o.on(m,function(t,n){var e=t[0];e instanceof b&&(this.bstStart=g.now())}),o.on(w,function(t,n){var e=t[0];e instanceof b&&i("bst",[e,n,this.bstStart,g.now()])}),a.on(m,function(t,n,e){this.bstStart=g.now(),this.bstType=e}),a.on(w,function(t,n){i(v,[n,this.bstStart,g.now(),this.bstType])}),s.on(m,function(){this.bstStart=g.now()}),s.on(w,function(t,n){i(v,[n,this.bstStart,g.now(),"requestAnimationFrame"])}),o.on(y+p,function(t){this.time=g.now(),this.startPath=location.pathname+location.hash}),o.on(y+h,function(t){i("bstHist",[location.pathname+location.hash,this.startPath,this.time])}),f in window.performance&&(window.performance["c"+c]?window.performance[f](u,function(t){i(d,[window.performance.getEntriesByType(l)]),window.performance["c"+c]()},!1):window.performance[f]("webkit"+u,function(t){i(d,[window.performance.getEntriesByType(l)]),window.performance["webkitC"+c]()},!1)),document[f]("scroll",r,{passive:!0}),document[f]("keypress",r,!1),document[f]("click",r,!1)}},{}],5:[function(t,n,e){function r(t){for(var n=t;n&&!n.hasOwnProperty(u);)n=Object.getPrototypeOf(n);n&&o(n)}function o(t){s.inPlace(t,[u,d],"-",i)}function i(t,n){return t[1]}var a=t("ee").get("events"),s=t(18)(a,!0),c=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";n.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(o(window),o(f.prototype)),a.on(u+"-start",function(t,n){var e=t[1],r=c(e,"nr@wrapped",function(){function t(){if("function"==typeof e.handleEvent)return e.handleEvent.apply(e,arguments)}var n={object:t,"function":e}[typeof e];return n?s(n,"fn-",null,n.name||"anonymous"):e});this.wrapped=t[1]=r}),a.on(d+"-start",function(t){t[1]=this.wrapped||t[1]})},{}],6:[function(t,n,e){var r=t("ee").get("history"),o=t(18)(r);n.exports=r,o.inPlace(window.history,["pushState","replaceState"],"-")},{}],7:[function(t,n,e){var r=t("ee").get("raf"),o=t(18)(r),i="equestAnimationFrame";n.exports=r,o.inPlace(window,["r"+i,"mozR"+i,"webkitR"+i,"msR"+i],"raf-"),r.on("raf-start",function(t){t[0]=o(t[0],"fn-")})},{}],8:[function(t,n,e){function r(t,n,e){t[0]=a(t[0],"fn-",null,e)}function o(t,n,e){this.method=e,this.timerDuration=isNaN(t[1])?0:+t[1],t[0]=a(t[0],"fn-",this,e)}var i=t("ee").get("timer"),a=t(18)(i),s="setTimeout",c="setInterval",f="clearTimeout",u="-start",d="-";n.exports=i,a.inPlace(window,[s,"setImmediate"],s+d),a.inPlace(window,[c],c+d),a.inPlace(window,[f,"clearImmediate"],f+d),i.on(c+u,r),i.on(s+u,o)},{}],9:[function(t,n,e){function r(t,n){d.inPlace(n,["onreadystatechange"],"fn-",s)}function o(){var t=this,n=u.context(t);t.readyState>3&&!n.resolved&&(n.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,y,"fn-",s)}function i(t){g.push(t),h&&(x?x.then(a):w?w(a):(E=-E,O.data=E))}function a(){for(var t=0;t<g.length;t++)r([],g[t]);g.length&&(g=[])}function s(t,n){return n}function c(t,n){for(var e in t)n[e]=t[e];return n}t(5);var f=t("ee"),u=f.get("xhr"),d=t(18)(u),l=NREUM.o,p=l.XHR,h=l.MO,m=l.PR,w=l.SI,v="readystatechange",y=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],g=[];n.exports=u;var b=window.XMLHttpRequest=function(t){var n=new p(t);try{u.emit("new-xhr",[n],n),n.addEventListener(v,o,!1)}catch(e){try{u.emit("internal-error",[e])}catch(r){}}return n};if(c(p,b),b.prototype=p.prototype,d.inPlace(b.prototype,["open","send"],"-xhr-",s),u.on("send-xhr-start",function(t,n){r(t,n),i(n)}),u.on("open-xhr-start",r),h){var x=m&&m.resolve();if(!w&&!m){var E=1,O=document.createTextNode(E);new h(a).observe(O,{characterData:!0})}}else f.on("fn-end",function(t){t[0]&&t[0].type===v||a()})},{}],10:[function(t,n,e){function r(t){var n=this.params,e=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<d;r++)t.removeEventListener(u[r],this.listener,!1);if(!n.aborted){if(e.duration=a.now()-this.startTime,4===t.readyState){n.status=t.status;var i=o(t,this.lastSize);if(i&&(e.rxSize=i),this.sameOrigin){var c=t.getResponseHeader("X-NewRelic-App-Data");c&&(n.cat=c.split(", ").pop())}}else n.status=0;e.cbTime=this.cbTime,f.emit("xhr-done",[t],t),s("xhr",[n,e,this.startTime])}}}function o(t,n){var e=t.responseType;if("json"===e&&null!==n)return n;var r="arraybuffer"===e||"blob"===e||"json"===e?t.response:t.responseText;return h(r)}function i(t,n){var e=c(n),r=t.params;r.host=e.hostname+":"+e.port,r.pathname=e.pathname,t.sameOrigin=e.sameOrigin}var a=t("loader");if(a.xhrWrappable){var s=t("handle"),c=t(11),f=t("ee"),u=["load","error","abort","timeout"],d=u.length,l=t("id"),p=t(14),h=t(13),m=window.XMLHttpRequest;a.features.xhr=!0,t(9),f.on("new-xhr",function(t){var n=this;n.totalCbs=0,n.called=0,n.cbTime=0,n.end=r,n.ended=!1,n.xhrGuids={},n.lastSize=null,p&&(p>34||p<10)||window.opera||t.addEventListener("progress",function(t){n.lastSize=t.loaded},!1)}),f.on("open-xhr-start",function(t){this.params={method:t[0]},i(this,t[1]),this.metrics={}}),f.on("open-xhr-end",function(t,n){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&n.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid)}),f.on("send-xhr-start",function(t,n){var e=this.metrics,r=t[0],o=this;if(e&&r){var i=h(r);i&&(e.txSize=i)}this.startTime=a.now(),this.listener=function(t){try{"abort"===t.type&&(o.params.aborted=!0),("load"!==t.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof n.onload))&&o.end(n)}catch(e){try{f.emit("internal-error",[e])}catch(r){}}};for(var s=0;s<d;s++)n.addEventListener(u[s],this.listener,!1)}),f.on("xhr-cb-time",function(t,n,e){this.cbTime+=t,n?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof e.onload||this.end(e)}),f.on("xhr-load-added",function(t,n){var e=""+l(t)+!!n;this.xhrGuids&&!this.xhrGuids[e]&&(this.xhrGuids[e]=!0,this.totalCbs+=1)}),f.on("xhr-load-removed",function(t,n){var e=""+l(t)+!!n;this.xhrGuids&&this.xhrGuids[e]&&(delete this.xhrGuids[e],this.totalCbs-=1)}),f.on("addEventListener-end",function(t,n){n instanceof m&&"load"===t[0]&&f.emit("xhr-load-added",[t[1],t[2]],n)}),f.on("removeEventListener-end",function(t,n){n instanceof m&&"load"===t[0]&&f.emit("xhr-load-removed",[t[1],t[2]],n)}),f.on("fn-start",function(t,n,e){n instanceof m&&("onload"===e&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=a.now()))}),f.on("fn-end",function(t,n){this.xhrCbStart&&f.emit("xhr-cb-time",[a.now()-this.xhrCbStart,this.onload,n],n)})}},{}],11:[function(t,n,e){n.exports=function(t){var n=document.createElement("a"),e=window.location,r={};n.href=t,r.port=n.port;var o=n.href.split("://");!r.port&&o[1]&&(r.port=o[1].split("/")[0].split("@").pop().split(":")[1]),r.port&&"0"!==r.port||(r.port="https"===o[0]?"443":"80"),r.hostname=n.hostname||e.hostname,r.pathname=n.pathname,r.protocol=o[0],"/"!==r.pathname.charAt(0)&&(r.pathname="/"+r.pathname);var i=!n.protocol||":"===n.protocol||n.protocol===e.protocol,a=n.hostname===document.domain&&n.port===e.port;return r.sameOrigin=i&&(!n.hostname||a),r}},{}],12:[function(t,n,e){function r(){}function o(t,n,e){return function(){return i(t,[f.now()].concat(s(arguments)),n?null:this,e),n?void 0:this}}var i=t("handle"),a=t(15),s=t(16),c=t("ee").get("tracer"),f=t("loader"),u=NREUM;"undefined"==typeof window.newrelic&&(newrelic=u);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],l="api-",p=l+"ixn-";a(d,function(t,n){u[n]=o(l+n,!0,"api")}),u.addPageAction=o(l+"addPageAction",!0),u.setCurrentRouteName=o(l+"routeName",!0),n.exports=newrelic,u.interaction=function(){return(new r).get()};var h=r.prototype={createTracer:function(t,n){var e={},r=this,o="function"==typeof n;return i(p+"tracer",[f.now(),t,e],r),function(){if(c.emit((o?"":"no-")+"fn-start",[f.now(),r,o],e),o)try{return n.apply(this,arguments)}catch(t){throw c.emit("fn-err",[arguments,this,t],e),t}finally{c.emit("fn-end",[f.now()],e)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,n){h[n]=o(p+n)}),newrelic.noticeError=function(t){"string"==typeof t&&(t=new Error(t)),i("err",[t,f.now()])}},{}],13:[function(t,n,e){n.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(n){return}}}},{}],14:[function(t,n,e){var r=0,o=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);o&&(r=+o[1]),n.exports=r},{}],15:[function(t,n,e){function r(t,n){var e=[],r="",i=0;for(r in t)o.call(t,r)&&(e[i]=n(r,t[r]),i+=1);return e}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],16:[function(t,n,e){function r(t,n,e){n||(n=0),"undefined"==typeof e&&(e=t?t.length:0);for(var r=-1,o=e-n||0,i=Array(o<0?0:o);++r<o;)i[r]=t[n+r];return i}n.exports=r},{}],17:[function(t,n,e){n.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],18:[function(t,n,e){function r(t){return!(t&&t instanceof Function&&t.apply&&!t[a])}var o=t("ee"),i=t(16),a="nr@original",s=Object.prototype.hasOwnProperty,c=!1;n.exports=function(t,n){function e(t,n,e,o){function nrWrapper(){var r,a,s,c;try{a=this,r=i(arguments),s="function"==typeof e?e(r,a):e||{}}catch(f){l([f,"",[r,a,o],s])}u(n+"start",[r,a,o],s);try{return c=t.apply(a,r)}catch(d){throw u(n+"err",[r,a,d],s),d}finally{u(n+"end",[r,a,c],s)}}return r(t)?t:(n||(n=""),nrWrapper[a]=t,d(t,nrWrapper),nrWrapper)}function f(t,n,o,i){o||(o="");var a,s,c,f="-"===o.charAt(0);for(c=0;c<n.length;c++)s=n[c],a=t[s],r(a)||(t[s]=e(a,f?s+o:o,i,s))}function u(e,r,o){if(!c||n){var i=c;c=!0;try{t.emit(e,r,o,n)}catch(a){l([a,e,r,o])}c=i}}function d(t,n){if(Object.defineProperty&&Object.keys)try{var e=Object.keys(t);return e.forEach(function(e){Object.defineProperty(n,e,{get:function(){return t[e]},set:function(n){return t[e]=n,n}})}),n}catch(r){l([r])}for(var o in t)s.call(t,o)&&(n[o]=t[o]);return n}function l(n){try{t.emit("internal-error",n)}catch(e){}}return t||(t=o),e.inPlace=f,e.flag=a,e}},{}],ee:[function(t,n,e){function r(){}function o(t){function n(t){return t&&t instanceof r?t:t?c(t,s,i):i()}function e(e,r,o,i){if(!l.aborted||i){t&&t(e,r,o);for(var a=n(o),s=h(e),c=s.length,f=0;f<c;f++)s[f].apply(a,r);var d=u[y[e]];return d&&d.push([g,e,r,a]),a}}function p(t,n){v[t]=h(t).concat(n)}function h(t){return v[t]||[]}function m(t){return d[t]=d[t]||o(e)}function w(t,n){f(t,function(t,e){n=n||"feature",y[e]=n,n in u||(u[n]=[])})}var v={},y={},g={on:p,emit:e,get:m,listeners:h,context:n,buffer:w,abort:a,aborted:!1};return g}function i(){return new r}function a(){(u.api||u.feature)&&(l.aborted=!0,u=l.backlog={})}var s="nr@context",c=t("gos"),f=t(15),u={},d={},l=n.exports=o();l.backlog=u},{}],gos:[function(t,n,e){function r(t,n,e){if(o.call(t,n))return t[n];var r=e();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,n,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return t[n]=r,r}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(t,n,e){function r(t,n,e,r){o.buffer([t],r),o.emit(t,n,e)}var o=t("ee").get("handle");n.exports=r,r.ee=o},{}],id:[function(t,n,e){function r(t){var n=typeof t;return!t||"object"!==n&&"function"!==n?-1:t===window?0:a(t,i,function(){return o++})}var o=1,i="nr@id",a=t("gos");n.exports=r},{}],loader:[function(t,n,e){function r(){if(!x++){var t=b.info=NREUM.info,n=l.getElementsByTagName("script")[0];if(setTimeout(u.abort,3e4),!(t&&t.licenseKey&&t.applicationID&&n))return u.abort();f(y,function(n,e){t[n]||(t[n]=e)}),c("mark",["onload",a()+b.offset],null,"api");var e=l.createElement("script");e.src="https://"+t.agent,n.parentNode.insertBefore(e,n)}}function o(){"complete"===l.readyState&&i()}function i(){c("mark",["domContent",a()+b.offset],null,"api")}function a(){return E.exists&&performance.now?Math.round(performance.now()):(s=Math.max((new Date).getTime(),s))-b.offset}var s=(new Date).getTime(),c=t("handle"),f=t(15),u=t("ee"),d=window,l=d.document,p="addEventListener",h="attachEvent",m=d.XMLHttpRequest,w=m&&m.prototype;NREUM.o={ST:setTimeout,SI:d.setImmediate,CT:clearTimeout,XHR:m,REQ:d.Request,EV:d.Event,PR:d.Promise,MO:d.MutationObserver};var v=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1071.min.js"},g=m&&w&&w[p]&&!/CriOS/.test(navigator.userAgent),b=n.exports={offset:s,now:a,origin:v,features:{},xhrWrappable:g};t(12),l[p]?(l[p]("DOMContentLoaded",i,!1),d[p]("load",r,!1)):(l[h]("onreadystatechange",o),d[h]("onload",r)),c("mark",["firstbyte",s],null,"api");var x=0,E=t(17)},{}]},{},["loader",2,10,4,3]);</script>
  


<meta id="bb-canon-url" name="bb-canon-url" content="https://bitbucket.org">
<meta name="bb-api-canon-url" content="https://api.bitbucket.org">
<meta name="apitoken" content="{&quot;token&quot;: &quot;unY8XBojfpLR6uJoL17l0ahqc8Fgu87mwr3SbS4gH6zlQFBz6r4lY0TawtLVpKIBAZ3ErZmY7zfdUteEiJzZnH4N5mOVKGNH3wuPtDExdFTuKZIh&quot;, &quot;expiration&quot;: 1519432162.078728}">

<meta name="bb-commit-hash" content="1e95fd7a0231">
<meta name="bb-app-node" content="app-167">
<meta name="bb-view-name" content="bitbucket.apps.repo2.views.filebrowse">
<meta name="ignore-whitespace" content="False">
<meta name="tab-size" content="None">
<meta name="locale" content="en">

<meta name="application-name" content="Bitbucket">
<meta name="apple-mobile-web-app-title" content="Bitbucket">


<meta name="theme-color" content="#0049B0">
<meta name="msapplication-TileColor" content="#0052CC">
<meta name="msapplication-TileImage" content="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/img/logos/bitbucket/mstile-150x150.png">
<link rel="apple-touch-icon" sizes="180x180" type="image/png" href="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/img/logos/bitbucket/apple-touch-icon.png">
<link rel="icon" sizes="192x192" type="image/png" href="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/img/logos/bitbucket/android-chrome-192x192.png">

<link rel="icon" sizes="16x16 24x24 32x32 64x64" type="image/x-icon" href="/favicon.ico?v=2">
<link rel="mask-icon" href="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/img/logos/bitbucket/safari-pinned-tab.svg" color="#0052CC">

<link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="Bitbucket">

  <meta name="description" content="">
  
  
    
  



  <link rel="stylesheet" href="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/css/entry/vendor.css" />
<link rel="stylesheet" href="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/css/entry/app.css" />



  <link rel="stylesheet" href="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/css/entry/adg3.css">
  
  <script nonce="nq9dLrG58xDeDrCa">
  window.__sentry__ = {"dsn": "https://ea49358f525d4019945839a3d7a8292a@sentry.io/159509", "release": "1e95fd7a0231 (production)", "tags": {"project": "bitbucket-core"}, "environment": "production"};
</script>
<script src="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/dist/webpack/sentry.js" nonce="nq9dLrG58xDeDrCa"></script>
  <script src="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/dist/webpack/early.js" nonce="nq9dLrG58xDeDrCa"></script>
  
  
  
    <link href="/sisl/multiagent_gail/rss?token=d7bad65e9903b76d36662b12126b192c" rel="alternate nofollow" type="application/rss+xml" title="RSS feed for Multiagent_GAIL" />

</head>
<body class="production adg3  "
    data-static-url="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/"
data-base-url="https://bitbucket.org"
data-no-avatar-image="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/img/default_avatar/user_blue.svg"
data-current-user="{&quot;username&quot;: &quot;rbhattacharyya&quot;, &quot;displayName&quot;: &quot;Raunak Pushpak Bhattacharyya&quot;, &quot;uuid&quot;: &quot;{9113a1a1-daee-4e75-bfd9-5e0f0bcc8ae1}&quot;, &quot;firstName&quot;: &quot;Raunak Pushpak Bhattacharyya&quot;, &quot;hasPremium&quot;: false, &quot;lastName&quot;: &quot;&quot;, &quot;avatarUrl&quot;: &quot;https://bitbucket.org/account/rbhattacharyya/avatar/32/?ts=1519424381&quot;, &quot;isTeam&quot;: false, &quot;isSshEnabled&quot;: false, &quot;isKbdShortcutsEnabled&quot;: true, &quot;id&quot;: 10931899, &quot;isAuthenticated&quot;: true}"
data-atlassian-id="{&quot;loginStatusUrl&quot;: &quot;https://id.atlassian.com/profile/rest/profile&quot;}"
data-settings="{&quot;MENTIONS_MIN_QUERY_LENGTH&quot;: 3}"

data-current-repo="{&quot;scm&quot;: &quot;git&quot;, &quot;readOnly&quot;: false, &quot;mainbranch&quot;: {&quot;name&quot;: &quot;master&quot;}, &quot;uuid&quot;: &quot;8dde33f3-fa45-4a28-a9eb-160d30aa37fa&quot;, &quot;language&quot;: &quot;&quot;, &quot;owner&quot;: {&quot;username&quot;: &quot;sisl&quot;, &quot;uuid&quot;: &quot;42facedf-c93f-4098-b192-ce01960ae38c&quot;, &quot;isTeam&quot;: true}, &quot;fullslug&quot;: &quot;sisl/multiagent_gail&quot;, &quot;slug&quot;: &quot;multiagent_gail&quot;, &quot;id&quot;: 31314162, &quot;pygmentsLanguage&quot;: null}"
data-current-cset="9e0940949186a8a7ff7fb57e6a6dec95ab7ba79b"





data-browser-monitoring="true"
data-switch-create-pullrequest-commit-status="true"




>
<div id="page">
  
    <div id="adg3-navigation"
  
  
  
  >
  <nav class="skeleton-nav">
    <div class="skeleton-nav--left">
      <div class="skeleton-nav--left-top">
        <ul class="skeleton-nav--items">
          <li></li>
          <li></li>
          <li></li>
          <li class="skeleton--icon"></li>
          <li class="skeleton--icon-sub"></li>
          <li class="skeleton--icon-sub"></li>
          <li class="skeleton--icon-sub"></li>
          <li class="skeleton--icon-sub"></li>
          <li class="skeleton--icon-sub"></li>
          <li class="skeleton--icon-sub"></li>
        </ul>
      </div>
      <div class="skeleton-nav--left-bottom">
        <div class="skeleton-nav--left-bottom-wrapper">
          <div class="skeleton-nav--item-help"></div>
          <div class="skeleton-nav--item-profile"></div>
        </div>
      </div>
    </div>
    <div class="skeleton-nav--right">
      <ul class="skeleton-nav--items-wide">
        <li class="skeleton--icon-logo-container">
          <div class="skeleton--icon-container"></div>
          <div class="skeleton--icon-description"></div>
          <div class="skeleton--icon-logo"></div>
        </li>
        <li>
          <div class="skeleton--icon-small"></div>
          <div class="skeleton-nav--item-wide-content"></div>
        </li>
        <li>
          <div class="skeleton--icon-small"></div>
          <div class="skeleton-nav--item-wide-content"></div>
        </li>
        <li>
          <div class="skeleton--icon-small"></div>
          <div class="skeleton-nav--item-wide-content"></div>
        </li>
        <li>
          <div class="skeleton--icon-small"></div>
          <div class="skeleton-nav--item-wide-content"></div>
        </li>
        <li>
          <div class="skeleton--icon-small"></div>
          <div class="skeleton-nav--item-wide-content"></div>
        </li>
        <li>
          <div class="skeleton--icon-small"></div>
          <div class="skeleton-nav--item-wide-content"></div>
        </li>
      </ul>
    </div>
  </nav>
</div>

    <div id="wrapper">
      
  


      
  <div id="nps-survey-container"></div>

 

      
  

<div id="account-warning" data-module="header/account-warning"
  data-unconfirmed-addresses="false"
  data-no-addresses="false"
  
></div>



      
  
<header id="aui-message-bar">
  
</header>


      <div id="content" role="main">

        
          <header class="app-header">
            <div class="app-header--primary">
              
                <div class="app-header--context">
                  <div class="app-header--breadcrumbs">
                    
  <ol class="aui-nav aui-nav-breadcrumbs">
    <li>
  <a href="/sisl/">SISL</a>
</li>

  <li class="aui-nav-selected">
    <a href="/account/user/sisl/projects/PROJ">SISL</a>
  </li>

<li>
  <a href="/sisl/multiagent_gail">Multiagent_GAIL</a>
</li>
    
  <li>
    <a href="/sisl/multiagent_gail/src">
      Source
    </a>
  </li>

  </ol>

                  </div>
                  <h1 class="app-header--heading">
                    <span class="file-path">imitate.py</span>
                  </h1>
                </div>
              
            </div>

            <div class="app-header--secondary">
              
                
              
            </div>
          </header>
        

        
        
  <div class="aui-page-panel ">
    <div class="hidden">
  
  
  </div>
    <div class="aui-page-panel-inner">

      <div
        id="repo-content"
        class="aui-page-panel-content forks-enabled can-create"
        data-module="repo/index"
        
          data-project-id="95373"
        
      >
        
        
  <div id="source-container" class="maskable" data-module="repo/source/index">
    



<header id="source-path">
  
    <div class="labels labels-csv">
      <div class="aui-buttons">
        <button data-branches-tags-url="/api/1.0/repositories/sisl/multiagent_gail/branches-tags"
                data-module="components/branch-dialog"
                
                class="aui-button branch-dialog-trigger" title="master">
          
            
              <span class="aui-icon aui-icon-small aui-iconfont-devtools-branch">Branch</span>
            
            <span class="name">master</span>
          
          <span class="aui-icon-dropdown"></span>
        </button>
        <button class="aui-button" id="checkout-branch-button"
                title="Check out this branch">
          <span class="aui-icon aui-icon-small aui-iconfont-devtools-clone">Check out branch</span>
          <span class="aui-icon-dropdown"></span>
        </button>
      </div>
      
    
    
  
    </div>
  
  
    <div class="secondary-actions">
      <div class="aui-buttons">
        
          <a href="/sisl/multiagent_gail/src/9e0940949186/ngsim_env/scripts/imitation/imitate.py?at=master"
            class="aui-button pjax-trigger source-toggle" aria-pressed="true">
            Source
          </a>
          <a href="/sisl/multiagent_gail/diff/ngsim_env/scripts/imitation/imitate.py?diff2=9e0940949186&at=master"
            class="aui-button pjax-trigger diff-toggle"
            title="Diff to previous change">
            Diff
          </a>
          <a href="/sisl/multiagent_gail/history-node/9e0940949186/ngsim_env/scripts/imitation/imitate.py?at=master"
            class="aui-button pjax-trigger history-toggle">
            History
          </a>
        
      </div>

      
      

    </div>
  
  <h1>
    
      
        <a href="/sisl/multiagent_gail/src/9e0940949186?at=master"
          class="pjax-trigger root" title="sisl/multiagent_gail at 9e0940949186">Multiagent_GAIL</a> /
      
      
        
          
            <a href="/sisl/multiagent_gail/src/9e0940949186/ngsim_env/?at=master"
              class="pjax-trigger directory-name">ngsim_env</a> /
          
        
      
        
          
            <a href="/sisl/multiagent_gail/src/9e0940949186/ngsim_env/scripts/?at=master"
              class="pjax-trigger directory-name">scripts</a> /
          
        
      
        
          
            <a href="/sisl/multiagent_gail/src/9e0940949186/ngsim_env/scripts/imitation/?at=master"
              class="pjax-trigger directory-name">imitation</a> /
          
        
      
        
          
            <span class="file-name">imitate.py</span>
          
        
      
    
  </h1>
  
    
    
  
  <div class="clearfix"></div>
</header>


  
    
  

  <div id="editor-container" class="maskable"
       data-module="repo/source/editor"
       data-owner="sisl"
       data-slug="multiagent_gail"
       data-is-writer="true"
       data-has-push-access="true"
       data-hash="9e0940949186a8a7ff7fb57e6a6dec95ab7ba79b"
       data-branch="master"
       data-path="ngsim_env/scripts/imitation/imitate.py"
       data-source-url="/api/internal/repositories/sisl/multiagent_gail/src/9e0940949186a8a7ff7fb57e6a6dec95ab7ba79b/ngsim_env/scripts/imitation/imitate.py">
    <div id="source-view" class="file-source-container" data-module="repo/source/view-file" data-is-lfs="false">
      <div class="toolbar">
        <div class="primary">
          <div class="aui-buttons">
            
              <button id="file-history-trigger" class="aui-button aui-button-light changeset-info"
                      data-changeset="9e0940949186a8a7ff7fb57e6a6dec95ab7ba79b"
                      data-path="ngsim_env/scripts/imitation/imitate.py"
                      data-current="9e0940949186a8a7ff7fb57e6a6dec95ab7ba79b">
                 

  <div class="aui-avatar aui-avatar-xsmall">
    <div class="aui-avatar-inner">
      <img src="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/img/default_avatar/user_blue.svg">
    </div>
  </div>
  <span class="changeset-hash">9e09409</span>
  <time datetime="2018-02-22T06:20:53+00:00" class="timestamp"></time>
  <span class="aui-icon-dropdown"></span>

              </button>
            
          </div>
          
          <a href="/sisl/multiagent_gail/full-commit/9e0940949186/ngsim_env/scripts/imitation/imitate.py" id="full-commit-link"
             title="View full commit 9e09409">Full commit</a>
        </div>
        <div class="secondary">
          
          <div class="aui-buttons">
            
              <a href="/sisl/multiagent_gail/annotate/9e0940949186a8a7ff7fb57e6a6dec95ab7ba79b/ngsim_env/scripts/imitation/imitate.py?at=master"
                 class="aui-button aui-button-light pjax-trigger blame-link">Blame</a>
              
            
            <a href="/sisl/multiagent_gail/raw/9e0940949186a8a7ff7fb57e6a6dec95ab7ba79b/ngsim_env/scripts/imitation/imitate.py" class="aui-button aui-button-light raw-link">Raw</a>
          </div>
          
            

            <div class="aui-buttons">
              
              <button id="file-edit-button" class="edit-button aui-button aui-button-light aui-button-split-main"
                  

                  >
                Edit
                
              </button>
              <button id="file-more-actions-button" class="aui-button aui-button-light aui-dropdown2-trigger aui-button-split-more" aria-owns="split-container-dropdown" aria-haspopup="true"
                  >
                More file actions
              </button>
            </div>
            <div id="split-container-dropdown" class="aui-dropdown2 aui-style-default" data-container="#editor-container">
              <ul class="aui-list-truncate">
                <li><a href="#" data-module="repo/source/rename-file" class="rename-link">Rename</a></li>
                <li><a href="#" data-module="repo/source/delete-file" class="delete-link">Delete</a></li>
              </ul>
            </div>
          
        </div>

        <div id="fileview-dropdown"
            class="aui-dropdown2 aui-style-default"
            data-fileview-container="#fileview-container"
            
            
            data-fileview-button="#fileview-trigger"
            data-module="connect/fileview">
          <div class="aui-dropdown2-section">
            <ul>
              <li>
                <a class="aui-dropdown2-radio aui-dropdown2-checked"
                    data-fileview-id="-1"
                    data-fileview-loaded="true"
                    data-fileview-target="#fileview-original"
                    data-fileview-connection-key=""
                    data-fileview-module-key="file-view-default">
                  Default File Viewer
                </a>
              </li>
              
            </ul>
          </div>
        </div>

        <div class="clearfix"></div>
      </div>
      <div id="fileview-container">
        <div id="fileview-original"
            class="fileview"
            data-module="repo/source/highlight-lines"
            data-fileview-loaded="true">
          


  
    <div class="file-source">
      <table class="codehilite highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><a href="#imitate.py-1"> 1</a>
<a href="#imitate.py-2"> 2</a>
<a href="#imitate.py-3"> 3</a>
<a href="#imitate.py-4"> 4</a>
<a href="#imitate.py-5"> 5</a>
<a href="#imitate.py-6"> 6</a>
<a href="#imitate.py-7"> 7</a>
<a href="#imitate.py-8"> 8</a>
<a href="#imitate.py-9"> 9</a>
<a href="#imitate.py-10">10</a>
<a href="#imitate.py-11">11</a>
<a href="#imitate.py-12">12</a>
<a href="#imitate.py-13">13</a>
<a href="#imitate.py-14">14</a>
<a href="#imitate.py-15">15</a>
<a href="#imitate.py-16">16</a>
<a href="#imitate.py-17">17</a>
<a href="#imitate.py-18">18</a>
<a href="#imitate.py-19">19</a>
<a href="#imitate.py-20">20</a>
<a href="#imitate.py-21">21</a>
<a href="#imitate.py-22">22</a>
<a href="#imitate.py-23">23</a>
<a href="#imitate.py-24">24</a>
<a href="#imitate.py-25">25</a>
<a href="#imitate.py-26">26</a>
<a href="#imitate.py-27">27</a>
<a href="#imitate.py-28">28</a>
<a href="#imitate.py-29">29</a>
<a href="#imitate.py-30">30</a>
<a href="#imitate.py-31">31</a>
<a href="#imitate.py-32">32</a>
<a href="#imitate.py-33">33</a>
<a href="#imitate.py-34">34</a>
<a href="#imitate.py-35">35</a>
<a href="#imitate.py-36">36</a>
<a href="#imitate.py-37">37</a>
<a href="#imitate.py-38">38</a>
<a href="#imitate.py-39">39</a>
<a href="#imitate.py-40">40</a>
<a href="#imitate.py-41">41</a>
<a href="#imitate.py-42">42</a>
<a href="#imitate.py-43">43</a>
<a href="#imitate.py-44">44</a>
<a href="#imitate.py-45">45</a>
<a href="#imitate.py-46">46</a>
<a href="#imitate.py-47">47</a>
<a href="#imitate.py-48">48</a>
<a href="#imitate.py-49">49</a>
<a href="#imitate.py-50">50</a>
<a href="#imitate.py-51">51</a>
<a href="#imitate.py-52">52</a>
<a href="#imitate.py-53">53</a>
<a href="#imitate.py-54">54</a>
<a href="#imitate.py-55">55</a>
<a href="#imitate.py-56">56</a>
<a href="#imitate.py-57">57</a>
<a href="#imitate.py-58">58</a>
<a href="#imitate.py-59">59</a>
<a href="#imitate.py-60">60</a>
<a href="#imitate.py-61">61</a>
<a href="#imitate.py-62">62</a>
<a href="#imitate.py-63">63</a>
<a href="#imitate.py-64">64</a>
<a href="#imitate.py-65">65</a>
<a href="#imitate.py-66">66</a>
<a href="#imitate.py-67">67</a>
<a href="#imitate.py-68">68</a>
<a href="#imitate.py-69">69</a>
<a href="#imitate.py-70">70</a>
<a href="#imitate.py-71">71</a>
<a href="#imitate.py-72">72</a>
<a href="#imitate.py-73">73</a>
<a href="#imitate.py-74">74</a>
<a href="#imitate.py-75">75</a>
<a href="#imitate.py-76">76</a>
<a href="#imitate.py-77">77</a>
<a href="#imitate.py-78">78</a>
<a href="#imitate.py-79">79</a>
<a href="#imitate.py-80">80</a>
<a href="#imitate.py-81">81</a>
<a href="#imitate.py-82">82</a>
<a href="#imitate.py-83">83</a>
<a href="#imitate.py-84">84</a>
<a href="#imitate.py-85">85</a>
<a href="#imitate.py-86">86</a>
<a href="#imitate.py-87">87</a>
<a href="#imitate.py-88">88</a>
<a href="#imitate.py-89">89</a>
<a href="#imitate.py-90">90</a>
<a href="#imitate.py-91">91</a>
<a href="#imitate.py-92">92</a>
<a href="#imitate.py-93">93</a>
<a href="#imitate.py-94">94</a>
<a href="#imitate.py-95">95</a>
<a href="#imitate.py-96">96</a></pre></div></td><td class="code"><div class="codehilite highlight"><pre><span></span><a name="imitate.py-1"></a>
<a name="imitate.py-2"></a><span class="kn">import</span> <span class="nn">numpy</span> <span class="kn">as</span> <span class="nn">np</span>
<a name="imitate.py-3"></a><span class="kn">import</span> <span class="nn">os</span>
<a name="imitate.py-4"></a><span class="kn">import</span> <span class="nn">tensorflow</span> <span class="kn">as</span> <span class="nn">tf</span>
<a name="imitate.py-5"></a>
<a name="imitate.py-6"></a><span class="kn">from</span> <span class="nn">sandbox.rocky.tf.optimizers.conjugate_gradient_optimizer</span> <span class="kn">import</span> <span class="n">FiniteDifferenceHvp</span><span class="p">,</span> <span class="n">ConjugateGradientOptimizer</span>
<a name="imitate.py-7"></a>
<a name="imitate.py-8"></a><span class="kn">from</span> <span class="nn">hgail.algos.gail</span> <span class="kn">import</span> <span class="n">GAIL</span>
<a name="imitate.py-9"></a>
<a name="imitate.py-10"></a><span class="kn">import</span> <span class="nn">auto_validator</span>
<a name="imitate.py-11"></a><span class="kn">import</span> <span class="nn">hyperparams</span>
<a name="imitate.py-12"></a><span class="kn">import</span> <span class="nn">utils</span>
<a name="imitate.py-13"></a>
<a name="imitate.py-14"></a><span class="c1"># setup</span>
<a name="imitate.py-15"></a><span class="n">args</span> <span class="o">=</span> <span class="n">hyperparams</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span>
<a name="imitate.py-16"></a><span class="n">exp_dir</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">set_up_experiment</span><span class="p">(</span><span class="n">exp_name</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">exp_name</span><span class="p">,</span> <span class="n">phase</span><span class="o">=</span><span class="s1">&#39;imitate&#39;</span><span class="p">)</span>
<a name="imitate.py-17"></a><span class="n">saver_dir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">exp_dir</span><span class="p">,</span> <span class="s1">&#39;imitate&#39;</span><span class="p">,</span> <span class="s1">&#39;log&#39;</span><span class="p">)</span>
<a name="imitate.py-18"></a><span class="n">saver_filepath</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">saver_dir</span><span class="p">,</span> <span class="s1">&#39;checkpoint&#39;</span><span class="p">)</span>
<a name="imitate.py-19"></a><span class="n">np</span><span class="o">.</span><span class="n">savez</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">saver_dir</span><span class="p">,</span> <span class="s1">&#39;args&#39;</span><span class="p">),</span> <span class="n">args</span><span class="o">=</span><span class="n">args</span><span class="p">)</span>
<a name="imitate.py-20"></a><span class="n">summary_writer</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">summary</span><span class="o">.</span><span class="n">FileWriter</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">exp_dir</span><span class="p">,</span> <span class="s1">&#39;imitate&#39;</span><span class="p">,</span> <span class="s1">&#39;summaries&#39;</span><span class="p">))</span>
<a name="imitate.py-21"></a>
<a name="imitate.py-22"></a><span class="c1"># build components</span>
<a name="imitate.py-23"></a><span class="n">env</span><span class="p">,</span> <span class="n">act_low</span><span class="p">,</span> <span class="n">act_high</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">build_ngsim_env</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">exp_dir</span><span class="p">,</span> <span class="n">vectorize</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">vectorize</span><span class="p">)</span>
<a name="imitate.py-24"></a><span class="n">data</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">load_data</span><span class="p">(</span>
<a name="imitate.py-25"></a>    <span class="n">args</span><span class="o">.</span><span class="n">expert_filepath</span><span class="p">,</span> 
<a name="imitate.py-26"></a>    <span class="n">act_low</span><span class="o">=</span><span class="n">act_low</span><span class="p">,</span> 
<a name="imitate.py-27"></a>    <span class="n">act_high</span><span class="o">=</span><span class="n">act_high</span><span class="p">,</span> 
<a name="imitate.py-28"></a>    <span class="n">min_length</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">env_H</span> <span class="o">+</span> <span class="n">args</span><span class="o">.</span><span class="n">env_primesteps</span><span class="p">,</span>
<a name="imitate.py-29"></a>    <span class="n">clip_std_multiple</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">normalize_clip_std_multiple</span><span class="p">,</span>
<a name="imitate.py-30"></a>    <span class="n">ngsim_filename</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">ngsim_filename</span>
<a name="imitate.py-31"></a><span class="p">)</span>
<a name="imitate.py-32"></a><span class="n">critic</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">build_critic</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">data</span><span class="p">,</span> <span class="n">env</span><span class="p">,</span> <span class="n">summary_writer</span><span class="p">)</span>
<a name="imitate.py-33"></a><span class="n">policy</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">build_policy</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">env</span><span class="p">)</span>
<a name="imitate.py-34"></a><span class="n">recognition_model</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">build_recognition_model</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">env</span><span class="p">,</span> <span class="n">summary_writer</span><span class="p">)</span>
<a name="imitate.py-35"></a><span class="n">baseline</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">build_baseline</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">env</span><span class="p">)</span>
<a name="imitate.py-36"></a><span class="n">reward_handler</span> <span class="o">=</span> <span class="n">utils</span><span class="o">.</span><span class="n">build_reward_handler</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">summary_writer</span><span class="p">)</span>
<a name="imitate.py-37"></a><span class="n">validator</span> <span class="o">=</span> <span class="n">auto_validator</span><span class="o">.</span><span class="n">AutoValidator</span><span class="p">(</span>
<a name="imitate.py-38"></a>    <span class="n">summary_writer</span><span class="p">,</span> 
<a name="imitate.py-39"></a>    <span class="n">data</span><span class="p">[</span><span class="s1">&#39;obs_mean&#39;</span><span class="p">],</span> 
<a name="imitate.py-40"></a>    <span class="n">data</span><span class="p">[</span><span class="s1">&#39;obs_std&#39;</span><span class="p">],</span>
<a name="imitate.py-41"></a>    <span class="n">render</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">validator_render</span><span class="p">,</span>
<a name="imitate.py-42"></a>    <span class="n">render_every</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">render_every</span><span class="p">,</span>
<a name="imitate.py-43"></a>    <span class="n">flat_recurrent</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">policy_recurrent</span>
<a name="imitate.py-44"></a><span class="p">)</span>
<a name="imitate.py-45"></a>
<a name="imitate.py-46"></a><span class="c1"># build algo </span>
<a name="imitate.py-47"></a><span class="n">saver</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">train</span><span class="o">.</span><span class="n">Saver</span><span class="p">(</span><span class="n">max_to_keep</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">keep_checkpoint_every_n_hours</span><span class="o">=.</span><span class="mi">5</span><span class="p">)</span>
<a name="imitate.py-48"></a><span class="n">sampler_args</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">n_envs</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">n_envs</span><span class="p">)</span> <span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">vectorize</span> <span class="k">else</span> <span class="bp">None</span>
<a name="imitate.py-49"></a><span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">policy_recurrent</span><span class="p">:</span>
<a name="imitate.py-50"></a>    <span class="n">optimizer</span> <span class="o">=</span> <span class="n">ConjugateGradientOptimizer</span><span class="p">(</span>
<a name="imitate.py-51"></a>        <span class="n">max_backtracks</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span>
<a name="imitate.py-52"></a>        <span class="n">hvp_approach</span><span class="o">=</span><span class="n">FiniteDifferenceHvp</span><span class="p">(</span><span class="n">base_eps</span><span class="o">=</span><span class="mf">1e-5</span><span class="p">)</span>
<a name="imitate.py-53"></a>    <span class="p">)</span>
<a name="imitate.py-54"></a><span class="k">else</span><span class="p">:</span>
<a name="imitate.py-55"></a>    <span class="n">optimizer</span> <span class="o">=</span> <span class="bp">None</span>
<a name="imitate.py-56"></a><span class="n">algo</span> <span class="o">=</span> <span class="n">GAIL</span><span class="p">(</span>
<a name="imitate.py-57"></a>    <span class="n">critic</span><span class="o">=</span><span class="n">critic</span><span class="p">,</span>
<a name="imitate.py-58"></a>    <span class="n">recognition</span><span class="o">=</span><span class="n">recognition_model</span><span class="p">,</span>
<a name="imitate.py-59"></a>    <span class="n">reward_handler</span><span class="o">=</span><span class="n">reward_handler</span><span class="p">,</span>
<a name="imitate.py-60"></a>    <span class="n">env</span><span class="o">=</span><span class="n">env</span><span class="p">,</span>
<a name="imitate.py-61"></a>    <span class="n">policy</span><span class="o">=</span><span class="n">policy</span><span class="p">,</span>
<a name="imitate.py-62"></a>    <span class="n">baseline</span><span class="o">=</span><span class="n">baseline</span><span class="p">,</span>
<a name="imitate.py-63"></a>    <span class="n">validator</span><span class="o">=</span><span class="n">validator</span><span class="p">,</span>
<a name="imitate.py-64"></a>    <span class="n">batch_size</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">batch_size</span><span class="p">,</span>
<a name="imitate.py-65"></a>    <span class="n">max_path_length</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">max_path_length</span><span class="p">,</span>
<a name="imitate.py-66"></a>    <span class="n">n_itr</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">n_itr</span><span class="p">,</span>
<a name="imitate.py-67"></a>    <span class="n">discount</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">discount</span><span class="p">,</span>
<a name="imitate.py-68"></a>    <span class="n">step_size</span><span class="o">=</span><span class="n">args</span><span class="o">.</span><span class="n">trpo_step_size</span><span class="p">,</span>
<a name="imitate.py-69"></a>    <span class="n">saver</span><span class="o">=</span><span class="n">saver</span><span class="p">,</span>
<a name="imitate.py-70"></a>    <span class="n">saver_filepath</span><span class="o">=</span><span class="n">saver_filepath</span><span class="p">,</span>
<a name="imitate.py-71"></a>    <span class="n">force_batch_sampler</span><span class="o">=</span><span class="bp">False</span> <span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">vectorize</span> <span class="k">else</span> <span class="bp">True</span><span class="p">,</span>
<a name="imitate.py-72"></a>    <span class="n">sampler_args</span><span class="o">=</span><span class="n">sampler_args</span><span class="p">,</span>
<a name="imitate.py-73"></a>    <span class="n">snapshot_env</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span>
<a name="imitate.py-74"></a>    <span class="n">plot</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span>
<a name="imitate.py-75"></a>    <span class="n">optimizer</span><span class="o">=</span><span class="n">optimizer</span><span class="p">,</span>
<a name="imitate.py-76"></a>    <span class="n">optimizer_args</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span>
<a name="imitate.py-77"></a>        <span class="n">max_backtracks</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span>
<a name="imitate.py-78"></a>        <span class="n">debug_nan</span><span class="o">=</span><span class="bp">True</span>
<a name="imitate.py-79"></a>    <span class="p">)</span>
<a name="imitate.py-80"></a><span class="p">)</span>
<a name="imitate.py-81"></a>
<a name="imitate.py-82"></a><span class="c1"># run it</span>
<a name="imitate.py-83"></a><span class="k">with</span> <span class="n">tf</span><span class="o">.</span><span class="n">Session</span><span class="p">()</span> <span class="k">as</span> <span class="n">session</span><span class="p">:</span>
<a name="imitate.py-84"></a>    
<a name="imitate.py-85"></a>    <span class="c1"># running the initialization here to allow for later loading</span>
<a name="imitate.py-86"></a>    <span class="c1"># NOTE: rllab batchpolopt runs this before training as well </span>
<a name="imitate.py-87"></a>    <span class="c1"># this means that any loading subsequent to this is nullified </span>
<a name="imitate.py-88"></a>    <span class="c1"># you have to comment of that initialization for any loading to work</span>
<a name="imitate.py-89"></a>    <span class="n">session</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">tf</span><span class="o">.</span><span class="n">global_variables_initializer</span><span class="p">())</span>
<a name="imitate.py-90"></a>
<a name="imitate.py-91"></a>    <span class="c1"># loading</span>
<a name="imitate.py-92"></a>    <span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">params_filepath</span> <span class="o">!=</span> <span class="s1">&#39;&#39;</span><span class="p">:</span>
<a name="imitate.py-93"></a>        <span class="n">algo</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">params_filepath</span><span class="p">)</span>
<a name="imitate.py-94"></a>
<a name="imitate.py-95"></a>    <span class="c1"># run training</span>
<a name="imitate.py-96"></a>    <span class="n">algo</span><span class="o">.</span><span class="n">train</span><span class="p">(</span><span class="n">sess</span><span class="o">=</span><span class="n">session</span><span class="p">)</span>
</pre></div>
</td></tr></table>
    </div>
  


        </div>
        
      </div>
    </div>
  </div>
  
  <div data-module="source/set-changeset" data-hash="9e0940949186a8a7ff7fb57e6a6dec95ab7ba79b"></div>



  
    
    
    
  
  

  </div>

        
        
        
          
    
    
  
        
      </div>
    </div>
  </div>

      </div>
    </div>
  
</div>

<div id="adg3-dialog"></div>


  

<div data-module="components/mentions/index">
  
    
    
  
  
    
    
  
  
    
    
  
</div>
<div data-module="components/typeahead/emoji/index">
  
    
    
  
</div>

<div data-module="components/repo-typeahead/index">
  
    
    
  
</div>

    
    
  

    
    
  

    
    
  

    
    
  


  


    
    
  

    
    
  


  
    
    
  
  
    
    
  
  
    
    
  
  
    
    
  
  
    
    
  
  
    
    
  
  
    
    
  


  
  
  <aui-inline-dialog
    id="help-menu-dialog"
    data-aui-alignment="bottom right"

    
    data-aui-alignment-static="true"
    data-module="header/help-menu"
    responds-to="toggle"
    aria-hidden="true">

  <div id="help-menu-section">
    <h1 class="help-menu-heading">Help</h1>

    <form id="help-menu-search-form" class="aui" target="_blank" method="get"
        action="https://support.atlassian.com/customer/search">
      <span id="help-menu-search-icon" class="aui-icon aui-icon-large aui-iconfont-search"></span>
      <input id="help-menu-search-form-input" name="q" class="text" type="text" placeholder="Ask a question">
    </form>

    <ul id="help-menu-links">
      <li>
        <a class="support-ga" data-support-gaq-page="DocumentationHome"
            href="https://confluence.atlassian.com/x/bgozDQ" target="_blank">
          Online help
        </a>
      </li>
      <li>
        <a class="support-ga" data-support-gaq-page="GitTutorials"
            href="https://www.atlassian.com/git?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=help_dropdown&amp;utm_content=learn_git"
            target="_blank">
          Learn Git
        </a>
      </li>
      <li>
        <a id="keyboard-shortcuts-link"
           href="#">Keyboard shortcuts</a>
      </li>
      <li>
        <a class="support-ga" data-support-gaq-page="DocumentationTutorials"
            href="https://confluence.atlassian.com/x/Q4sFLQ" target="_blank">
          Bitbucket tutorials
        </a>
      </li>
      <li>
        <a class="support-ga" data-support-gaq-page="SiteStatus"
            href="https://status.bitbucket.org/" target="_blank">
          Site status
        </a>
      </li>
      <li>
        <a class="support-ga" data-support-gaq-page="Home"
            href="https://support.atlassian.com/bitbucket-cloud/" target="_blank">
          Support
        </a>
      </li>
    </ul>
  </div>
</aui-inline-dialog>
  


  <div class="omnibar" data-module="components/omnibar/index">
    <form class="omnibar-form aui"></form>
  </div>
  
    
    
  
  
    
    
  
  
    
    
  
  
    
    
  





  

  <div class="_mustache-templates">
    
      <script id="branch-checkout-template" type="text/html">
        

<div id="checkout-branch-contents">
  <div class="command-line">
    <p>
      Check out this branch on your local machine to begin working on it.
    </p>
    <input type="text" class="checkout-command" readonly="readonly"
        
           value="git fetch && git checkout [[branchName]]"
        
        >
  </div>
  
    <div class="sourcetree-callout clone-in-sourcetree"
  data-module="components/clone/clone-in-sourcetree"
  data-https-url="https://rbhattacharyya@bitbucket.org/sisl/multiagent_gail.git"
  data-ssh-url="git@bitbucket.org:sisl/multiagent_gail.git">

  <div>
    <button class="aui-button aui-button-primary">
      
        Check out in Sourcetree
      
    </button>
  </div>

  <p class="windows-text">
    
      <a href="http://www.sourcetreeapp.com/?utm_source=internal&amp;utm_medium=link&amp;utm_campaign=clone_repo_win" target="_blank">Atlassian Sourcetree</a>
      is a free Git and Mercurial client for Windows.
    
  </p>
  <p class="mac-text">
    
      <a href="http://www.sourcetreeapp.com/?utm_source=internal&amp;utm_medium=link&amp;utm_campaign=clone_repo_mac" target="_blank">Atlassian Sourcetree</a>
      is a free Git and Mercurial client for Mac.
    
  </p>
</div>
  
</div>

      </script>
    
      <script id="branch-dialog-template" type="text/html">
        

<div class="tabbed-filter-widget branch-dialog">
  <div class="tabbed-filter">
    <input placeholder="Filter branches" class="filter-box" autosave="branch-dropdown-31314162" type="text">
    [[^ignoreTags]]
      <div class="aui-tabs horizontal-tabs aui-tabs-disabled filter-tabs">
        <ul class="tabs-menu">
          <li class="menu-item active-tab"><a href="#branches">Branches</a></li>
          <li class="menu-item"><a href="#tags">Tags</a></li>
        </ul>
      </div>
    [[/ignoreTags]]
  </div>
  
    <div class="tab-pane active-pane" id="branches" data-filter-placeholder="Filter branches">
      <ol class="filter-list">
        <li class="empty-msg">No matching branches</li>
        [[#branches]]
          
            [[#hasMultipleHeads]]
              [[#heads]]
                <li class="comprev filter-item">
                  <a class="pjax-trigger filter-item-link" href="/sisl/multiagent_gail/src/[[changeset]]/ngsim_env/scripts/imitation/imitate.py?at=[[safeName]]"
                     title="[[name]]">
                    [[name]] ([[shortChangeset]])
                  </a>
                </li>
              [[/heads]]
            [[/hasMultipleHeads]]
            [[^hasMultipleHeads]]
              <li class="comprev filter-item">
                <a class="pjax-trigger filter-item-link" href="/sisl/multiagent_gail/src/[[changeset]]/ngsim_env/scripts/imitation/imitate.py?at=[[safeName]]" title="[[name]]">
                  [[name]]
                </a>
              </li>
            [[/hasMultipleHeads]]
          
        [[/branches]]
      </ol>
    </div>
    <div class="tab-pane" id="tags" data-filter-placeholder="Filter tags">
      <ol class="filter-list">
        <li class="empty-msg">No matching tags</li>
        [[#tags]]
          <li class="comprev filter-item">
            <a class="pjax-trigger filter-item-link" href="/sisl/multiagent_gail/src/[[changeset]]/ngsim_env/scripts/imitation/imitate.py?at=[[safeName]]" title="[[name]]">
              [[name]]
            </a>
          </li>
        [[/tags]]
      </ol>
    </div>
  
</div>

      </script>
    
      <script id="image-upload-template" type="text/html">
        

<form id="upload-image" method="POST"
    
      action="/xhr/sisl/multiagent_gail/image-upload/"
    >
  <input type='hidden' name='csrfmiddlewaretoken' value='epzXVs3ie1eDh1a8gWIdY77UQAv7F42zGILGSD0stYUKcFSAiBz8czjR7ybAwO0g' />

  <div class="drop-target">
    <p class="centered">Drag image here</p>
  </div>

  
  <div>
    <button class="aui-button click-target">Select an image</button>
    <input name="file" type="file" class="hidden file-target"
           accept="image/jpeg, image/gif, image/png" />
    <input type="submit" class="hidden">
  </div>
</form>


      </script>
    
      <script id="mention-result" type="text/html">
        
<span class="mention-result">
  <span class="aui-avatar aui-avatar-small mention-result--avatar">
    <span class="aui-avatar-inner">
      <img src="[[avatar_url]]">
    </span>
  </span>
  [[#display_name]]
    <span class="display-name mention-result--display-name">[[&display_name]]</span> <small class="username mention-result--username">[[&username]]</small>
  [[/display_name]]
  [[^display_name]]
    <span class="username mention-result--username">[[&username]]</span>
  [[/display_name]]
  [[#is_teammate]][[^is_team]]
    <span class="aui-lozenge aui-lozenge-complete aui-lozenge-subtle mention-result--lozenge">teammate</span>
  [[/is_team]][[/is_teammate]]
</span>
      </script>
    
      <script id="mention-call-to-action" type="text/html">
        
[[^query]]
<li class="bb-typeahead-item">Begin typing to search for a user</li>
[[/query]]
[[#query]]
<li class="bb-typeahead-item">Continue typing to search for a user</li>
[[/query]]

      </script>
    
      <script id="mention-no-results" type="text/html">
        
[[^searching]]
<li class="bb-typeahead-item">Found no matching users for <em>[[query]]</em>.</li>
[[/searching]]
[[#searching]]
<li class="bb-typeahead-item bb-typeahead-searching">Searching for <em>[[query]]</em>.</li>
[[/searching]]

      </script>
    
      <script id="emoji-result" type="text/html">
        
<span class="emoji-result">
  <span class="emoji-result--avatar">
    <img class="emoji" src="[[src]]">
  </span>
  <span class="name emoji-result--name">[[&name]]</span>
</span>

      </script>
    
      <script id="repo-typeahead-result" type="text/html">
        <span class="aui-avatar aui-avatar-project aui-avatar-xsmall">
  <span class="aui-avatar-inner">
    <img src="[[avatar]]">
  </span>
</span>
<span class="owner">[[&owner]]</span>/<span class="slug">[[&slug]]</span>

      </script>
    
      <script id="share-form-template" type="text/html">
        

<div class="error aui-message hidden">
  <span class="aui-icon icon-error"></span>
  <div class="message"></div>
</div>
<form class="aui">
  <table class="widget bb-list aui">
    <thead>
    <tr class="assistive">
      <th class="user">User</th>
      <th class="role">Role</th>
      <th class="actions">Actions</th>
    </tr>
    </thead>
    <tbody>
      <tr class="form">
        <td colspan="2">
          <input type="text" class="text bb-user-typeahead user-or-email"
                 placeholder="Username or email address"
                 autocomplete="off"
                 data-bb-typeahead-focus="false"
                 [[#disabled]]disabled[[/disabled]]>
        </td>
        <td class="actions">
          <button type="submit" class="aui-button aui-button-light" disabled>Add</button>
        </td>
      </tr>
    </tbody>
  </table>
</form>

      </script>
    
      <script id="share-detail-template" type="text/html">
        

[[#username]]
<td class="user
    [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]"
    [[#error]]data-error="[[error]]"[[/error]]>
  <div title="[[displayName]]">
    <a href="/[[username]]/" class="user">
      <span class="aui-avatar aui-avatar-xsmall">
        <span class="aui-avatar-inner">
          <img src="[[avatar]]">
        </span>
      </span>
      <span>[[displayName]]</span>
    </a>
  </div>
</td>
[[/username]]
[[^username]]
<td class="email
    [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]"
    [[#error]]data-error="[[error]]"[[/error]]>
  <div title="[[email]]">
    <span class="aui-icon aui-icon-small aui-iconfont-email"></span>
    [[email]]
  </div>
</td>
[[/username]]
<td class="role
    [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]">
  <div>
    [[#group]]
      [[#hasCustomGroups]]
        <select class="group [[#noGroupChoices]]hidden[[/noGroupChoices]]">
          [[#groups]]
            <option value="[[slug]]"
                [[#isSelected]]selected[[/isSelected]]>
              [[name]]
            </option>
          [[/groups]]
        </select>
      [[/hasCustomGroups]]
      [[^hasCustomGroups]]
      <label>
        <input type="checkbox" class="admin"
            [[#isAdmin]]checked[[/isAdmin]]>
        Administrator
      </label>
      [[/hasCustomGroups]]
    [[/group]]
    [[^group]]
      <ul>
        <li class="permission aui-lozenge aui-lozenge-complete
            [[^read]]aui-lozenge-subtle[[/read]]"
            data-permission="read">
          read
        </li>
        <li class="permission aui-lozenge aui-lozenge-complete
            [[^write]]aui-lozenge-subtle[[/write]]"
            data-permission="write">
          write
        </li>
        <li class="permission aui-lozenge aui-lozenge-complete
            [[^admin]]aui-lozenge-subtle[[/admin]]"
            data-permission="admin">
          admin
        </li>
      </ul>
    [[/group]]
  </div>
</td>
<td class="actions
    [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]">
  <div>
    <a href="#" class="delete">
      <span class="aui-icon aui-icon-small aui-iconfont-remove">Delete</span>
    </a>
  </div>
</td>

      </script>
    
      <script id="share-team-template" type="text/html">
        

<div class="clearfix">
  <span class="team-avatar-container">
    <span class="aui-avatar aui-avatar-medium">
      <span class="aui-avatar-inner">
        <img src="[[avatar]]">
      </span>
    </span>
  </span>
  <span class="team-name-container">
    [[display_name]]
  </span>
</div>
<p class="helptext">
  
    Existing users are granted access to this team immediately.
    New users will be sent an invitation.
  
</p>
<div class="share-form"></div>

      </script>
    
      <script id="scope-list-template" type="text/html">
        <ul class="scope-list">
  [[#scopes]]
    <li class="scope-list--item">
      <span class="scope-list--icon aui-icon aui-icon-small [[icon]]"></span>
      <span class="scope-list--description">[[description]]</span>
    </li>
  [[/scopes]]
</ul>

      </script>
    
      <script id="source-changeset" type="text/html">
        

<a href="/sisl/multiagent_gail/src/[[raw_node]]/[[path]]?at=master"
    class="[[#selected]]highlight[[/selected]]"
    data-hash="[[node]]">
  [[#author.username]]
    <span class="aui-avatar aui-avatar-xsmall">
      <span class="aui-avatar-inner">
        <img src="[[author.avatar]]">
      </span>
    </span>
    <span class="author" title="[[raw_author]]">[[author.display_name]]</span>
  [[/author.username]]
  [[^author.username]]
    <span class="aui-avatar aui-avatar-xsmall">
      <span class="aui-avatar-inner">
        <img src="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/img/default_avatar/user_blue.svg">
      </span>
    </span>
    <span class="author unmapped" title="[[raw_author]]">[[author]]</span>
  [[/author.username]]
  <time datetime="[[utctimestamp]]" data-title="true">[[utctimestamp]]</time>
  <span class="message">[[message]]</span>
</a>

      </script>
    
      <script id="embed-template" type="text/html">
        

<form class="aui inline-dialog-embed-dialog">
  <label for="embed-code-[[dialogId]]">Embed this source in another page:</label>
  <input type="text" readonly="true" value="&lt;script src=&quot;[[url]]&quot;&gt;&lt;/script&gt;" id="embed-code-[[dialogId]]" class="embed-code">
</form>

      </script>
    
      <script id="edit-form-template" type="text/html">
        


<form class="bb-content-container online-edit-form aui"
      data-repository="[[owner]]/[[slug]]"
      data-destination-repository="[[destinationOwner]]/[[destinationSlug]]"
      data-local-id="[[localID]]"
      [[#isWriter]]data-is-writer="true"[[/isWriter]]
      [[#hasPushAccess]]data-has-push-access="true"[[/hasPushAccess]]
      [[#isPullRequest]]data-is-pull-request="true"[[/isPullRequest]]
      [[#hideCreatePullRequest]]data-hide-create-pull-request="true"[[/hideCreatePullRequest]]
      data-hash="[[hash]]"
      data-branch="[[branch]]"
      data-path="[[path]]"
      data-is-create="[[isCreate]]"
      data-preview-url="/xhr/[[owner]]/[[slug]]/preview/[[hash]]/[[encodedPath]]"
      data-preview-error="We had trouble generating your preview."
      data-unsaved-changes-error="Your changes will be lost. Are you sure you want to leave?">
  <div class="bb-content-container-header">
    <div class="bb-content-container-header-primary">
      <span class="bb-content-container-heading">
        [[#isCreate]]
          [[#branch]]
            
              Creating <span class="edit-path">[[path]]</span> on branch: <strong>[[branch]]</strong>
            
          [[/branch]]
          [[^branch]]
            [[#path]]
              
                Creating <span class="edit-path">[[path]]</span>
              
            [[/path]]
            [[^path]]
              
                Creating <span class="edit-path">unnamed file</span>
              
            [[/path]]
          [[/branch]]
        [[/isCreate]]
        [[^isCreate]]
          
            Editing <span class="edit-path">[[path]]</span> on branch: <strong>[[branch]]</strong>
          
        [[/isCreate]]
      </span>
    </div>
    <div class="bb-content-container-header-secondary">
      <div class="hunk-nav aui-buttons">
        <button class="prev-hunk-button aui-button aui-button-light"
            disabled="disabled" aria-disabled="true"
            title="Previous change">
          <span class="aui-icon aui-icon-small aui-iconfont-up">Previous change</span>
        </button>
        <button class="next-hunk-button aui-button aui-button-light"
            disabled="disabled" aria-disabled="true"
            title="Next change">
          <span class="aui-icon aui-icon-small aui-iconfont-down">Next change</span>
        </button>
      </div>
    </div>
  </div>
  <div class="bb-content-container-body has-header has-footer file-editor">
    <textarea id="id_source"></textarea>
  </div>
  <div class="preview-pane"></div>
  <div class="bb-content-container-footer">
    <div class="bb-content-container-footer-primary">
      <div id="syntax-mode" class="bb-content-container-item field">
        <label for="id_syntax-mode" class="online-edit-form--label">Syntax mode:</label>
        <select id="id_syntax-mode">
          [[#syntaxes]]
            <option value="[[#mime]][[mime]][[/mime]][[^mime]][[mode]][[/mime]]">[[name]]</option>
          [[/syntaxes]]
        </select>
      </div>
      <div id="indent-mode" class="bb-content-container-item field">
        <label for="id_indent-mode" class="online-edit-form--label">Indent mode:</label>
        <select id="id_indent-mode">
          <option value="tabs">Tabs</option>
          <option value="spaces">Spaces</option>
        </select>
      </div>
      <div id="indent-size" class="bb-content-container-item field">
        <label for="id_indent-size" class="online-edit-form--label">Indent size:</label>
        <select id="id_indent-size">
          <option value="2">2</option>
          <option value="4">4</option>
          <option value="8">8</option>
        </select>
      </div>
      <div id="wrap-mode" class="bb-content-container-item field">
        <label for="id_wrap-mode" class="online-edit-form--label">Line wrap:</label>
        <select id="id_wrap-mode">
          <option value="">Off</option>
          <option value="soft">On</option>
        </select>
      </div>
    </div>
    <div class="bb-content-container-footer-secondary">
      [[^isCreate]]
        <button class="preview-button aui-button aui-button-light"
                disabled="disabled" aria-disabled="true"
                data-preview-label="View diff"
                data-edit-label="Edit file">View diff</button>
      [[/isCreate]]
      <button class="save-button aui-button aui-button-primary"
              disabled="disabled" aria-disabled="true">Commit</button>
      [[^isCreate]]
        <a class="aui-button aui-button-link cancel-link" href="#">Cancel</a>
      [[/isCreate]]
    </div>
  </div>
</form>

      </script>
    
      <script id="commit-form-template" type="text/html">
        

<form class="aui commit-form"
      data-title="Commit changes"
      [[#isDelete]]
        data-default-message="[[filename]] deleted online with Bitbucket"
      [[/isDelete]]
      [[#isCreate]]
        data-default-message="[[filename]] created online with Bitbucket"
      [[/isCreate]]
      [[^isDelete]]
        [[^isCreate]]
          data-default-message="[[filename]] edited online with Bitbucket"
        [[/isCreate]]
      [[/isDelete]]
      data-fork-error="We had trouble creating your fork."
      data-commit-error="We had trouble committing your changes."
      data-pull-request-error="We had trouble creating your pull request."
      data-update-error="We had trouble updating your pull request."
      data-branch-conflict-error="A branch with that name already exists."
      data-forking-message="Forking repository"
      data-committing-message="Committing changes"
      data-merging-message="Branching and merging changes"
      data-creating-pr-message="Creating pull request"
      data-updating-pr-message="Updating pull request"
      data-cta-label="Commit"
      data-cancel-label="Cancel">
  [[#isDelete]]
    <div class="aui-message info">
      <span class="aui-icon icon-info"></span>
      <span class="message">
        
          Committing this change will delete [[filename]] from your repository.
        
      </span>
    </div>
  [[/isDelete]]
  <div class="aui-message error hidden">
    <span class="aui-icon icon-error"></span>
    <span class="message"></span>
  </div>
  [[^isWriter]]
    <div class="aui-message info">
      <span class="aui-icon icon-info"></span>
      <p class="title">
        
          You don't have write access to this repository.
        
      </p>
      <span class="message">
        
          We'll create a fork for your changes and submit a
          pull request back to this repository.
        
      </span>
    </div>
  [[/isWriter]]
  [[#isRename]]
    <div class="field-group">
      <label for="id_path">New path</label>
      <input type="text" id="id_path" class="text" value="[[path]]"/>
    </div>
  [[/isRename]]
  <div class="field-group">
    <label for="id_message">Commit message</label>
    <textarea id="id_message" class="long-field textarea"></textarea>
  </div>
  [[^isPullRequest]]
    [[#isWriter]]
      <fieldset class="group">
        <div class="checkbox">
          [[#hasPushAccess]]
            [[^hideCreatePullRequest]]
              <input id="id_create-pullrequest" class="checkbox" type="checkbox">
              <label for="id_create-pullrequest">Create a pull request for this change</label>
            [[/hideCreatePullRequest]]
          [[/hasPushAccess]]
          [[^hasPushAccess]]
            <input id="id_create-pullrequest" class="checkbox" type="checkbox" checked="checked" aria-disabled="true" disabled="true">
            <label for="id_create-pullrequest" title="Branch restrictions do not allow you to update this branch.">Create a pull request for this change</label>
          [[/hasPushAccess]]
        </div>
      </fieldset>
      <div id="pr-fields">
        <div id="branch-name-group" class="field-group">
          <label for="id_branch-name">Branch name</label>
          <input type="text" id="id_branch-name" class="text long-field">
        </div>
        

<div class="field-group" id="id_reviewers_group">
  <label for="reviewers">Reviewers</label>

  
  <input id="reviewers" name="reviewers" type="hidden"
          value=""
          data-mention-url="/xhr/mentions/repositories/:dest_username/:dest_slug"
          data-reviewers="[]"
          data-suggested="[]"
          data-locked="[]">

  <div class="error"></div>
  <div class="suggested-reviewers"></div>

</div>

      </div>
    [[/isWriter]]
  [[/isPullRequest]]
  <button type="submit" id="id_submit">Commit</button>
</form>

      </script>
    
      <script id="merge-message-template" type="text/html">
        Merged [[hash]] into [[branch]]

[[message]]

      </script>
    
      <script id="commit-merge-error-template" type="text/html">
        



  We had trouble merging your changes. We stored them on the <strong>[[branch]]</strong> branch, so feel free to
  <a href="/[[owner]]/[[slug]]/full-commit/[[hash]]/[[path]]?at=[[encodedBranch]]">view them</a> or
  <a href="#" class="create-pull-request-link">create a pull request</a>.


      </script>
    
      <script id="selected-reviewer-template" type="text/html">
        <div class="aui-avatar aui-avatar-xsmall">
  <div class="aui-avatar-inner">
    <img src="[[avatar_url]]">
  </div>
</div>
[[display_name]]

      </script>
    
      <script id="suggested-reviewer-template" type="text/html">
        <button class="aui-button aui-button-link" type="button" tabindex="-1">[[display_name]]</button>

      </script>
    
      <script id="suggested-reviewers-template" type="text/html">
        

<span class="suggested-reviewer-list-label">Recent:</span>
<ul class="suggested-reviewer-list unstyled-list"></ul>

      </script>
    
      <script id="omnibar-form-template" type="text/html">
        <div class="omnibar-input-container">
  <input class="omnibar-input" type="text" [[#placeholder]]placeholder="[[placeholder]]"[[/placeholder]]>
</div>
<ul class="omnibar-result-group-list"></ul>

      </script>
    
      <script id="omnibar-blank-slate-template" type="text/html">
        

<div class="omnibar-blank-slate">No results found</div>

      </script>
    
      <script id="omnibar-result-group-list-item-template" type="text/html">
        <div class="omnibar-result-group-header clearfix">
  <h2 class="omnibar-result-group-label" title="[[label]]">[[label]]</h2>
  <span class="omnibar-result-group-context" title="[[context]]">[[context]]</span>
</div>
<ul class="omnibar-result-list unstyled-list"></ul>

      </script>
    
      <script id="omnibar-result-list-item-template" type="text/html">
        [[#url]]
  <a href="[[&url]]" class="omnibar-result-label">[[&label]]</a>
[[/url]]
[[^url]]
  <span class="omnibar-result-label">[[&label]]</span>
[[/url]]
[[#context]]
  <span class="omnibar-result-context">[[context]]</span>
[[/context]]

      </script>
    
  </div>




  
  


<script nonce="nq9dLrG58xDeDrCa">
  window.__initial_state__ = {"section": {"repository": {"connectActions": [], "cloneProtocol": "https", "currentRepository": {"scm": "git", "website": "", "name": "Multiagent_GAIL", "links": {"clone": [{"href": "https://rbhattacharyya@bitbucket.org/sisl/multiagent_gail.git", "name": "https"}, {"href": "git@bitbucket.org:sisl/multiagent_gail.git", "name": "ssh"}], "self": {"href": "https://bitbucket.org/!api/2.0/repositories/sisl/multiagent_gail"}, "html": {"href": "https://bitbucket.org/sisl/multiagent_gail"}, "avatar": {"href": "https://bitbucket.org/sisl/multiagent_gail/avatar/32/"}}, "description": "", "project": {"uuid": "{c3cee952-e55a-4a84-a561-2348a1bf81a1}", "links": {"self": {"href": "https://bitbucket.org/!api/2.0/teams/sisl/projects/PROJ"}, "html": {"href": "https://bitbucket.org/account/user/sisl/projects/PROJ"}, "avatar": {"href": "https://bitbucket.org/account/user/sisl/projects/PROJ/avatar/32"}}, "name": "SISL", "created_on": "2015-12-03T20:02:57.974675+00:00", "key": "PROJ", "owner": {"username": "sisl", "type": "team", "display_name": "SISL", "uuid": "{42facedf-c93f-4098-b192-ce01960ae38c}", "links": {"self": {"href": "https://bitbucket.org/!api/2.0/teams/sisl"}, "html": {"href": "https://bitbucket.org/sisl/"}, "avatar": {"href": "https://bitbucket.org/account/sisl/avatar/32/"}}}, "updated_on": "2016-03-30T03:39:16.603422+00:00", "type": "project", "is_private": false, "description": "Project created by Bitbucket for SISL"}, "language": "", "full_name": "sisl/multiagent_gail", "owner": {"username": "sisl", "website": "http://sisl.stanford.edu/", "display_name": "SISL", "uuid": "{42facedf-c93f-4098-b192-ce01960ae38c}", "links": {"self": {"href": "https://bitbucket.org/!api/2.0/teams/sisl"}, "html": {"href": "https://bitbucket.org/sisl/"}, "avatar": {"href": "https://bitbucket.org/account/sisl/avatar/32/"}}, "created_on": "2013-12-02T03:58:23.223452+00:00", "location": null, "type": "team"}, "type": "repository", "slug": "multiagent_gail", "is_private": true, "uuid": "{8dde33f3-fa45-4a28-a9eb-160d30aa37fa}"}, "menuItems": [{"analytics_label": "repository.overview", "is_client_link": false, "icon_class": "icon-overview", "badge_label": null, "weight": 100, "url": "/sisl/multiagent_gail/overview", "tab_name": "overview", "can_display": true, "label": "Overview", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "target": "_self", "id": "repo-overview-link", "icon": "icon-overview"}, {"analytics_label": "repository.source", "is_client_link": false, "icon_class": "icon-source", "badge_label": null, "weight": 200, "url": "/sisl/multiagent_gail/src", "tab_name": "source", "can_display": true, "label": "Source", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": ["/diff", "/history-node"], "target": "_self", "id": "repo-source-link", "icon": "icon-source"}, {"analytics_label": "repository.commits", "is_client_link": false, "icon_class": "icon-commits", "badge_label": null, "weight": 300, "url": "/sisl/multiagent_gail/commits/", "tab_name": "commits", "can_display": true, "label": "Commits", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "target": "_self", "id": "repo-commits-link", "icon": "icon-commits"}, {"analytics_label": "repository.branches", "is_client_link": false, "icon_class": "icon-branches", "badge_label": null, "weight": 400, "url": "/sisl/multiagent_gail/branches/", "tab_name": "branches", "can_display": true, "label": "Branches", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "target": "_self", "id": "repo-branches-link", "icon": "icon-branches"}, {"analytics_label": "repository.pullrequests", "is_client_link": false, "icon_class": "icon-pull-requests", "badge_label": "0 open pull requests", "weight": 500, "url": "/sisl/multiagent_gail/pull-requests/", "tab_name": "pullrequests", "can_display": true, "label": "Pull requests", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "target": "_self", "id": "repo-pullrequests-link", "icon": "icon-pull-requests"}, {"analytics_label": "user.addon", "is_client_link": false, "icon_class": "aui-iconfont-build", "badge_label": null, "weight": 550, "url": "/sisl/multiagent_gail/addon/pipelines/home", "tab_name": "repopage-4rd9jr-add-on-link", "can_display": true, "label": "Pipelines", "icon_url": null, "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "type": "connect_menu_item", "id": "repopage-4rd9jr-add-on-link", "target": "_self"}, {"analytics_label": "user.addon", "is_client_link": false, "icon_class": "aui-iconfont-unfocus", "badge_label": null, "weight": 560, "url": "/sisl/multiagent_gail/addon/pipelines/deployments", "tab_name": "repopage-eek9jX-add-on-link", "can_display": true, "label": "Deployments", "icon_url": "https://bitbucket-assetroot.s3.amazonaws.com/add-on/icons/fca72d46-7e20-4dc4-b6a8-c83fb9665cc6.svg?Signature=EoW19BowA6Q8Oiy3kAj22qa5kiA%3D&Expires=1519433662&AWSAccessKeyId=AKIAIQWXW6WLXMB5QZAQ&versionId=z.ggvA9RJ7VZF4B8B.tbvzjqnPmgCf7w", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "type": "connect_menu_item", "id": "repopage-eek9jX-add-on-link", "target": "_self"}, {"analytics_label": "repository.downloads", "is_client_link": false, "icon_class": "icon-downloads", "badge_label": null, "weight": 800, "url": "/sisl/multiagent_gail/downloads/", "tab_name": "downloads", "can_display": true, "label": "Downloads", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "target": "_self", "id": "repo-downloads-link", "icon": "icon-downloads"}, {"analytics_label": "user.addon", "is_client_link": false, "icon_class": "aui-iconfont-unfocus", "badge_label": null, "weight": 100, "url": "/sisl/multiagent_gail/addon/bitbucket-trello-addon/trello-board", "tab_name": "repopage-jyKppo-add-on-link", "can_display": true, "label": "Boards", "icon_url": "https://bitbucket-assetroot.s3.amazonaws.com/add-on/icons/35ceae0c-17b1-443c-a6e8-d9de1d7cccdb.svg?Signature=vIZ2M2mk6TpD2ee1n65kG74EtVc%3D&Expires=1519433662&AWSAccessKeyId=AKIAIQWXW6WLXMB5QZAQ&versionId=3oqdrZZjT.HijZ3kHTPsXE6IcSjhCG.P", "anchor": false, "analytics_payload": {}, "matching_url_prefixes": [], "type": "connect_menu_item", "id": "repopage-jyKppo-add-on-link", "target": "_self"}], "bitbucketActions": [{"analytics_label": "repository.clone", "is_client_link": false, "icon_class": "icon-clone", "badge_label": null, "weight": 100, "url": "#clone", "tab_name": "clone", "can_display": true, "label": "<strong>Clone<\/strong> this repository", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "target": "_self", "id": "repo-clone-button", "icon": "icon-clone"}, {"analytics_label": "repository.create_branch", "is_client_link": false, "icon_class": "icon-create-branch", "badge_label": null, "weight": 200, "url": "/sisl/multiagent_gail/branch", "tab_name": "create-branch", "can_display": true, "label": "Create a <strong>branch<\/strong>", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "target": "_self", "id": "repo-create-branch-link", "icon": "icon-create-branch"}, {"analytics_label": "create_pullrequest", "is_client_link": false, "icon_class": "icon-create-pull-request", "badge_label": null, "weight": 300, "url": "/sisl/multiagent_gail/pull-requests/new", "tab_name": "create-pullreqs", "can_display": true, "label": "Create a <strong>pull request<\/strong>", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "target": "_self", "id": "repo-create-pull-request-link", "icon": "icon-create-pull-request"}, {"analytics_label": "repository.compare", "is_client_link": false, "icon_class": "aui-icon-small aui-iconfont-devtools-compare", "badge_label": null, "weight": 400, "url": "/sisl/multiagent_gail/branches/compare", "tab_name": "compare", "can_display": true, "label": "<strong>Compare<\/strong> branches or tags", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "target": "_self", "id": "repo-compare-link", "icon": "aui-icon-small aui-iconfont-devtools-compare"}, {"analytics_label": "repository.fork", "is_client_link": false, "icon_class": "icon-fork", "badge_label": null, "weight": 500, "url": "/sisl/multiagent_gail/fork", "tab_name": "fork", "can_display": true, "label": "<strong>Fork<\/strong> this repository", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "target": "_self", "id": "repo-fork-link", "icon": "icon-fork"}], "activeMenuItem": "source"}}, "global": {"features": {"cache-ref-adverts": true, "evolution": false, "dashboard-single-page-app": true, "app-passwords": true, "diff-renames-internal": true, "search-syntax-highlighting": true, "clonebundles": true, "deployments": true, "fe_word_diff": true, "trello-boards": true, "atlassian-editor": false, "use-moneybucket": true, "show-guidance-message": true, "diff-renames-public": true, "lfs_post_beta": true, "new-source-browser": false}, "locale": "en", "geoip_country": "US", "targetFeatures": {"cache-ref-adverts": true, "evolution": false, "dashboard-single-page-app": true, "app-passwords": true, "diff-renames-internal": true, "search-syntax-highlighting": true, "clonebundles": true, "deployments": true, "fe_word_diff": true, "trello-boards": true, "atlassian-editor": false, "use-moneybucket": true, "show-guidance-message": true, "diff-renames-public": true, "lfs_post_beta": true, "new-source-browser": false}, "isFocusedTask": false, "teams": [{"username": "sisl", "type": "team", "display_name": "SISL", "uuid": "{42facedf-c93f-4098-b192-ce01960ae38c}", "links": {"self": {"href": "https://bitbucket.org/!api/2.0/teams/sisl"}, "html": {"href": "https://bitbucket.org/sisl/"}, "avatar": {"href": "https://bitbucket.org/account/sisl/avatar/32/"}}}], "bitbucketActions": [{"analytics_label": null, "is_client_link": false, "icon_class": "", "badge_label": null, "weight": 100, "url": "/repo/create?owner=sisl", "tab_name": null, "can_display": true, "label": "<strong>Repository<\/strong>", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "target": "_self", "id": "repository-create-drawer-item", "icon": ""}, {"analytics_label": null, "is_client_link": false, "icon_class": "", "badge_label": null, "weight": 110, "url": "/account/create-team/", "tab_name": null, "can_display": true, "label": "<strong>Team<\/strong>", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "target": "_self", "id": "team-create-drawer-item", "icon": ""}, {"analytics_label": null, "is_client_link": false, "icon_class": "", "badge_label": null, "weight": 120, "url": "/account/projects/create?owner=sisl", "tab_name": null, "can_display": true, "label": "<strong>Project<\/strong>", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "target": "_self", "id": "project-create-drawer-item", "icon": ""}, {"analytics_label": null, "is_client_link": false, "icon_class": "", "badge_label": null, "weight": 130, "url": "/snippets/new?owner=sisl", "tab_name": null, "can_display": true, "label": "<strong>Snippet<\/strong>", "type": "menu_item", "anchor": true, "analytics_payload": {}, "matching_url_prefixes": [], "target": "_self", "id": "snippet-create-drawer-item", "icon": ""}], "targetUser": {"username": "sisl", "website": "http://sisl.stanford.edu/", "display_name": "SISL", "uuid": "{42facedf-c93f-4098-b192-ce01960ae38c}", "links": {"self": {"href": "https://bitbucket.org/!api/2.0/teams/sisl"}, "html": {"href": "https://bitbucket.org/sisl/"}, "avatar": {"href": "https://bitbucket.org/account/sisl/avatar/32/"}}, "created_on": "2013-12-02T03:58:23.223452+00:00", "location": null, "type": "team"}, "isNavigationOpen": true, "path": "/sisl/multiagent_gail/src/9e0940949186a8a7ff7fb57e6a6dec95ab7ba79b/ngsim_env/scripts/imitation/imitate.py", "focusedTaskBackButtonUrl": "https://bitbucket.org/sisl/multiagent_gail/src/9e0940949186a8a7ff7fb57e6a6dec95ab7ba79b/ngsim_env/scripts/imitation/?at=master", "currentUser": {"username": "rbhattacharyya", "website": null, "display_name": "Raunak Pushpak Bhattacharyya", "account_id": "5a5f86707b4e6b6c2a81aad2", "links": {"self": {"href": "https://bitbucket.org/!api/2.0/users/rbhattacharyya"}, "html": {"href": "https://bitbucket.org/rbhattacharyya/"}, "avatar": {"href": "https://bitbucket.org/account/rbhattacharyya/avatar/32/"}}, "extra": {"has_ssh_key": false, "has_atlassian_account": true}, "created_on": "2018-01-30T23:34:24.609421+00:00", "is_staff": false, "location": null, "type": "user", "uuid": "{9113a1a1-daee-4e75-bfd9-5e0f0bcc8ae1}"}}, "connect": {}};
  window.__settings__ = {"JIRA_ISSUE_COLLECTORS": {"code-review": {"url": "https://jira.atlassian.com/s/42e64237a0aa70b2fff514729f4cc549-T/ubr4ye/78000/d09c6b3599a0a8533f4324e4b45ccfea/2.0.26/_/download/batch/com.atlassian.jira.collector.plugin.jira-issue-collector-plugin:issuecollector/com.atlassian.jira.collector.plugin.jira-issue-collector-plugin:issuecollector.js?locale=en-UK&collectorId=76ebbf00", "id": "76ebbf00"}}, "SOCIAL_AUTH_ATLASSIANID_LOGOUT_URL": "https://id.atlassian.com/logout", "CANON_URL": "https://bitbucket.org", "API_CANON_URL": "https://api.bitbucket.org"};
</script>

<script src="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/jsi18n/en/djangojs.js" nonce="nq9dLrG58xDeDrCa"></script>

  <script src="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/dist/webpack/locales/en.js"></script>

<script src="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/dist/webpack/vendor.js" nonce="nq9dLrG58xDeDrCa"></script>
<script src="https://d301sr5gafysq2.cloudfront.net/1e95fd7a0231/dist/webpack/app.js" nonce="nq9dLrG58xDeDrCa"></script>


<script async src="https://www.google-analytics.com/analytics.js" nonce="nq9dLrG58xDeDrCa"></script>

<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","queueTime":0,"licenseKey":"a2cef8c3d3","agent":"","transactionName":"Z11RZxdWW0cEVkYLDV4XdUYLVEFdClsdAAtEWkZQDlJBGgRFQhFMQl1DXFcZQ10AQkFYBFlUVlEXWEJHAA==","applicationID":"1841284","errorBeacon":"bam.nr-data.net","applicationTime":971}</script>
</body>
</html>