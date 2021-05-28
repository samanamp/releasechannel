# Vue

<div class='component'>
<demo-component app-code="vue"/>
</div>


## v2.6.12
<p style="font-size:12px;"> 20, Aug 2020 
<a href="https://github.com/vuejs/vue/releases/tag/v2.6.12" target="_blank"> 
Source </a><OutboundLink /></p>
<p>build: release 2.6.12</p>

## v2.6.11
<p style="font-size:12px;"> 13, Dec 2019 
<a href="https://github.com/vuejs/vue/releases/tag/v2.6.11" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Security Fixes</h3>
<ul>
<li>Bump <code>vue-server-renderer</code>'s dependency of <code>serialize-javascript</code> to 2.1.2</li>
</ul>
<h3>Bug Fixes</h3>
<ul>
<li><strong>types:</strong> fix prop constructor type inference (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/10779">#10779</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/4821149b8bbd4650b1d9c9c3cfbb539ac1e24589"><tt>4821149</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/10779">#10779</a></li>
<li>fix function expression regex (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9922">#9922</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/569b728ab19d1956bf935a98c9c65a03d92ac85f"><tt>569b728</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9922">#9922</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9920">#9920</a></li>
<li><strong>compiler:</strong> Remove the warning for valid v-slot value (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9917">#9917</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/085d188379af98e9f482d7e2009ebfd771bd7ca5"><tt>085d188</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9917">#9917</a></li>
<li><strong>types:</strong> fix global namespace declaration for UMD bundle (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9912">#9912</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/ab50e8e1da2f4f944af683252481728485fedf16"><tt>ab50e8e</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9912">#9912</a></li>
</ul>

## v2.6.10
<p style="font-size:12px;"> 20, Mar 2019 
<a href="https://github.com/vuejs/vue/releases/tag/v2.6.10" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Bug Fixes</h3>
<ul>
<li><strong>codegen:</strong> support named function expression in v-on (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9709">#9709</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/3433ba5beef9a6dd97705943c3441ebbee222afd"><tt>3433ba5</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9709">#9709</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9707">#9707</a></li>
<li><strong>core:</strong> cleanup timeouts for async components (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9649">#9649</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/02d21c265c239682e73b2b3f98028f2da5e7205d"><tt>02d21c2</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9649">#9649</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9648">#9648</a></li>
<li><strong>core:</strong> only unset dom prop when not present <a class="commit-link" href="https://github.com/vuejs/vue/commit/f11449d916a468651d4fd5024c37e3eebbc9941f"><tt>f11449d</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9650">#9650</a></li>
<li><strong>core:</strong> use window.performance for compatibility in JSDOM (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9700">#9700</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/653c74e64e5ccd66cda94c77577984f8afa8386d"><tt>653c74e</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9700">#9700</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9698">#9698</a></li>
<li><strong>scheduler:</strong> revert timeStamp check <a class="commit-link" href="https://github.com/vuejs/vue/commit/22790b250cd5239a8379b4ec8cc3a9b570dac4bc"><tt>22790b2</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9729">#9729</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9632">#9632</a></li>
<li><strong>slots:</strong> fix slots not updating when passing down normal slots as $scopedSlots <a class="commit-link" href="https://github.com/vuejs/vue/commit/ebc1893faccd1a9d953a8e8feddcb49cf1b9004d"><tt>ebc1893</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9699">#9699</a></li>
<li><strong>types:</strong> allow using functions on the PropTypes (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9733">#9733</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/df4af4bd1906b9f23b62816142fdfbd6336d3d2f"><tt>df4af4b</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9733">#9733</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9692">#9692</a></li>
<li><strong>types:</strong> support string type for style in VNode data (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9728">#9728</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/982d5a492fb95577217e2dacaa044eabe78a8601"><tt>982d5a4</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9728">#9728</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9727">#9727</a></li>
</ul>

## v2.6.9
<p style="font-size:12px;"> 20, Mar 2019 
<a href="https://github.com/vuejs/vue/releases/tag/v2.6.9" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Bug Fixes</h3>
<ul>
<li>event timeStamp check for Qt <a class="commit-link" href="https://github.com/vuejs/vue/commit/7591b9dc6dde314f2d32dcd7a8355f696a330979"><tt>7591b9d</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9681">#9681</a></li>
<li>should consider presence of normal slots when caching normalized scoped slots <a class="commit-link" href="https://github.com/vuejs/vue/commit/9313cf91740e1d43c43cf9e73d905dbab913beb5"><tt>9313cf9</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9644">#9644</a></li>
<li>should not swallow user catch on rejected promise in methods <a class="commit-link" href="https://github.com/vuejs/vue/commit/7186940143704acc4ec046132f6a56e9c983e510"><tt>7186940</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9694">#9694</a></li>
<li>should use fallback for scoped slots with single falsy v-if <a class="commit-link" href="https://github.com/vuejs/vue/commit/781c70514e01bc402828946805bfad7437c7175e"><tt>781c705</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9658">#9658</a></li>
<li><strong>ssr:</strong> not push non-async css files into map (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9677">#9677</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/d28240009c4c49fb2ef42a79206f0d9ad03f736c"><tt>d282400</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9677">#9677</a></li>
<li>v-bind object should be overridable by single bindings (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9653">#9653</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/0b57380f10986c6b07e3c240acc06bfd2eddfd1b"><tt>0b57380</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9653">#9653</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9641">#9641</a></li>
<li><strong>compiler:</strong> whitespace: 'condense' should honor pre tag as well (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9660">#9660</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/f1bdd7ff9d1fc86f7a8ad8d5cb6d9abc7b2e47f3"><tt>f1bdd7f</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9660">#9660</a></li>
<li><strong>scheduler:</strong> fix getNow check in IE9 (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9647">#9647</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/da77d6a98bdccd8a2c8bfdfe6b9cb46efcb1193c"><tt>da77d6a</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9647">#9647</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9632">#9632</a></li>
<li><strong>scheduler:</strong> getNow detection can randomly fail (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9667">#9667</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/ef2a380c6eb6bd1a7ff516c357dafa717e75a745"><tt>ef2a380</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9667">#9667</a></li>
<li><strong>ssr:</strong> fix nested async functional componet rendering (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9673">#9673</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/8082d2f910d963f14c151fb445e0fcc5c975cca9"><tt>8082d2f</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9673">#9673</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9643">#9643</a></li>
<li><strong>transition:</strong> fix appear check for transition wrapper components (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9668">#9668</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/4de4649d9637262a9b007720b59f80ac72a5620c"><tt>4de4649</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9668">#9668</a></li>
</ul>

## v2.6.8
<p style="font-size:12px;"> 01, Mar 2019 
<a href="https://github.com/vuejs/vue/releases/tag/v2.6.8" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Bug Fixes</h3>
<ul>
<li>avoid compression of unicode sequences by using regexps (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9595">#9595</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/7912f75c5eb09e0aef3e4bfd8a3bb78cad7540d7"><tt>7912f75</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9595">#9595</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9456">#9456</a></li>
<li>fix modifier parsing for dynamic argument with deep path (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9585">#9585</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/060c3b98efa44a9f21bcc038a2593b1cc3c782e9"><tt>060c3b9</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9585">#9585</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9577">#9577</a></li>
<li>further adjust max stack size <a class="commit-link" href="https://github.com/vuejs/vue/commit/571a4880fc06b491a280325b79fd4cbb59ceb47e"><tt>571a488</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9562">#9562</a></li>
<li>handle async component when parent is toggled before resolve (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9572">#9572</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/ed341137b23315b76ba391db1b0e537950c091e1"><tt>ed34113</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9572">#9572</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9571">#9571</a></li>
<li>scoped slots dynamic check should include v-for on element itself <a class="commit-link" href="https://github.com/vuejs/vue/commit/2277b2322cf81b5830a5b85f6600e1896edc7aa9"><tt>2277b23</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9596">#9596</a></li>
<li><strong>compiler:</strong> set end location for incomplete elements (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9598">#9598</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/cbad54aa52847cfc934bb925d53c53ee57fc153d"><tt>cbad54a</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9598">#9598</a></li>
<li><strong>types:</strong> allow scoped slots to return a single VNode (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9563">#9563</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/241eea19a64550bfdb3f9d7e4197127997572842"><tt>241eea1</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9563">#9563</a></li>
<li><strong>types:</strong> update this for nextTick api (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9541">#9541</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/f33301619d18b9392597c5230af17921c0b42466"><tt>f333016</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9541">#9541</a></li>
</ul>

## v2.6.7
<p style="font-size:12px;"> 21, Feb 2019 
<a href="https://github.com/vuejs/vue/releases/tag/v2.6.7" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Bug Fixes</h3>
<ul>
<li>avoid errors thrown during dom props update <a class="commit-link" href="https://github.com/vuejs/vue/commit/8a80a23ecba23f92f278d664388050ffcd121385"><tt>8a80a23</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9459">#9459</a></li>
<li>avoid possible infinite loop by accessing observables in error handler (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9489">#9489</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/ee29e41ef469b3ca3c793f04289075e3b128447f"><tt>ee29e41</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9489">#9489</a></li>
<li>ensure generated scoped slot code is compatible with 2.5 <a class="commit-link" href="https://github.com/vuejs/vue/commit/7ec4627902020cccd7b3f4fbc63e1b0d6b9798cd"><tt>7ec4627</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9545">#9545</a></li>
<li>ensure scoped slots update in conditional branches <a class="commit-link" href="https://github.com/vuejs/vue/commit/d9b27a92bd5277ee23a4e68a8bd31ecc72f4c99b"><tt>d9b27a9</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9534">#9534</a></li>
<li>scoped slots should update when inside v-for <a class="commit-link" href="https://github.com/vuejs/vue/commit/8f004ea44e06d7764fa884212fa95c2033515928"><tt>8f004ea</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9506">#9506</a></li>
<li><strong><a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9511">#9511</a>:</strong> avoid promise catch multiple times (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9526">#9526</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/2f3020e9cc1ad5c878606b56bb73a30b1d9bb7d9"><tt>2f3020e</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9511">#9511</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9526">#9526</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9511">#9511</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9511">#9511</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9511">#9511</a></li>
<li><strong>compiler:</strong> handle negative length in codeframe repeat <a class="commit-link" href="https://github.com/vuejs/vue/commit/7a8de91cd78f523fabe8452652513250871a01c6"><tt>7a8de91</tt></a></li>
</ul>

## v2.6.6
<p style="font-size:12px;"> 12, Feb 2019 
<a href="https://github.com/vuejs/vue/releases/tag/v2.6.6" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Bug Fixes</h3>
<ul>
<li>ensure scoped slot containing passed down slot content updates properly <a class="commit-link" href="https://github.com/vuejs/vue/commit/21fca2fffc3a75235a6656eb85ae40835e04bf69"><tt>21fca2f</tt></a></li>
<li>fix keyCode check for Chrome autofill fake key events <a class="commit-link" href="https://github.com/vuejs/vue/commit/29c348f3cf60c50a52cc98123f8c54fa8f5672fc"><tt>29c348f</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9441">#9441</a></li>
</ul>

## v2.6.5
<p style="font-size:12px;"> 11, Feb 2019 
<a href="https://github.com/vuejs/vue/releases/tag/v2.6.5" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Bug Fixes</h3>
<ul>
<li>allow passing multiple arguments to scoped slot <a class="commit-link" href="https://github.com/vuejs/vue/commit/e7d49cdcf2fd9a612e0dac7a7bea318824210881"><tt>e7d49cd</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9468">#9468</a></li>
<li>bail out of event blocking for iOS bug <a class="commit-link" href="https://github.com/vuejs/vue/commit/0bad7e2a3508b55abaa8aec2a1bd9c1127305cb4"><tt>0bad7e2</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9462">#9462</a></li>
<li>do not cache scoped slots when mixed with normal slots <a class="commit-link" href="https://github.com/vuejs/vue/commit/060686d6ea4d013129b4d2e93d7d2e5c93e09686"><tt>060686d</tt></a></li>
</ul>

## v2.6.4
<p style="font-size:12px;"> 08, Feb 2019 
<a href="https://github.com/vuejs/vue/releases/tag/v2.6.4" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Performance Improvements</h3>
<ul>
<li>cache result from functional ctx.slots() calls <a class="commit-link" href="https://github.com/vuejs/vue/commit/7a0dfd0badf3054c95ac1ec66cc6e213f1592c95"><tt>7a0dfd0</tt></a></li>
<li>skip scoped slots normalization when possible <a class="commit-link" href="https://github.com/vuejs/vue/commit/099f3ba60085a089ff369442bdb835f3868e47c0"><tt>099f3ba</tt></a></li>
</ul>
<h3>Bug Fixes</h3>
<ul>
<li>avoid breaking avoriaz edge case <a class="commit-link" href="https://github.com/vuejs/vue/commit/9011b83db79cf2f3563f8fccb2e41b5b863c3ee9"><tt>9011b83</tt></a></li>
<li>avoid logging same error twice when thrown by user in global handler <a class="commit-link" href="https://github.com/vuejs/vue/commit/ca57920edb56000bfc87bb64f4e5e3450c03e13a"><tt>ca57920</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9445">#9445</a></li>
<li>empty scoped slot should return undefined <a class="commit-link" href="https://github.com/vuejs/vue/commit/57bc80a546acb2bd092edd393228324b453ae4e2"><tt>57bc80a</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9452">#9452</a></li>
<li>expose v-slot slots without scope on this.$slots <a class="commit-link" href="https://github.com/vuejs/vue/commit/0e8560d0fc1c0fbf3a52464939701e0e44543b00"><tt>0e8560d</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9421">#9421</a> <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9458">#9458</a></li>
<li>new syntax slots without scope should also be exposed on functional slots() <a class="commit-link" href="https://github.com/vuejs/vue/commit/8a800867fe61e5aa642e1e3da91bb890d07312f7"><tt>8a80086</tt></a></li>
</ul>

## v2.6.3
<p style="font-size:12px;"> 06, Feb 2019 
<a href="https://github.com/vuejs/vue/releases/tag/v2.6.3" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Bug Fixes</h3>
<ul>
<li>async component should use render owner as force update context <a class="commit-link" href="https://github.com/vuejs/vue/commit/b9de23b1008b52deca7e7df40843e318a42f3f53"><tt>b9de23b</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9432">#9432</a></li>
<li>avoid exposing internal flags on $scopedSlots <a class="commit-link" href="https://github.com/vuejs/vue/commit/24b4640c1f268722f5ab8f03e68e2df897cfbdf6"><tt>24b4640</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9443">#9443</a></li>
<li>bail out scoped slot optimization when there are nested scopes <a class="commit-link" href="https://github.com/vuejs/vue/commit/4d4d22a3f6017c46d08b67afe46af43027b06629"><tt>4d4d22a</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9438">#9438</a></li>
<li><strong>compiler:</strong> fix v-bind dynamic arguments on slot outlets <a class="commit-link" href="https://github.com/vuejs/vue/commit/96a09aad99bdecbcc0e5c420077bf41893d4a745"><tt>96a09aa</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9444">#9444</a></li>
<li><strong>types:</strong> add Vue.version to types (<a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9431">#9431</a>) <a class="commit-link" href="https://github.com/vuejs/vue/commit/54e6a121e992f20c03f104533caa4c59e59b1ee7"><tt>54e6a12</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/pull/9431">#9431</a></li>
<li>skip microtask fix if event is fired from different document <a class="commit-link" href="https://github.com/vuejs/vue/commit/dae7e4182fbbb41e599953cc22e5d54dbb164070"><tt>dae7e41</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9448">#9448</a></li>
<li>skip microtask fix in Firefix &lt;= 53 <a class="commit-link" href="https://github.com/vuejs/vue/commit/7bc88f30c3eadded07dd5b460d1e7cb9342d017c"><tt>7bc88f3</tt></a>, closes <a class="issue-link js-issue-link" href="https://github.com/vuejs/vue/issues/9446">#9446</a></li>
</ul>
<h3>Reverts</h3>
<ul>
<li>revert: expose all scoped slots on this.$slots <a class="commit-link" href="https://github.com/vuejs/vue/commit/d5ade28652b07303ac6b713813792752ae5e4e04"><tt>d5ade28</tt></a></li>
</ul>
