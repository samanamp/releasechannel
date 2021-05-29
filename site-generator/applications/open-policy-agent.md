# Open Policy Agent

<div>
<demo-component app-code="open-policy-agent"/>
</div>


## v0.29.3
<p style="font-size:12px;"> 28, May 2021 
<a href="https://github.com/open-policy-agent/opa/releases/tag/v0.29.3" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This bugfix release addresses another edge case in function evaluation (<a href="https://github.com/open-policy-agent/opa/pull/3505">#3505</a>).</p>

## v0.29.2
<p style="font-size:12px;"> 28, May 2021 
<a href="https://github.com/open-policy-agent/opa/releases/tag/v0.29.2" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This is a bugfix release to resolve an issue in topdown's function output caching (<a href="https://github.com/open-policy-agent/opa/issues/3501">#3501</a>)</p>

## v0.29.1
<p style="font-size:12px;"> 27, May 2021 
<a href="https://github.com/open-policy-agent/opa/releases/tag/v0.29.1" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release contains a number of enhancements and fixes.</p>
<h3>SDK</h3>
<ul>
<li>This release includes a new top-level package to support OPA integrations in Go programs: <code>github.com/open-policy-agent/opa/sdk</code>. Users that want to integrate OPA as a library in Go and expose features like bundles and decision logging should use this package. The package is controlled by specifying an OPA configuration file. Hot reloading is supported out-of-the-box. See the GoDoc for <a href="https://pkg.go.dev/github.com/open-policy-agent/opa@v0.29.0/sdk" rel="nofollow">the package docs</a> for more details.</li>
</ul>
<h3>Server</h3>
<ul>
<li>A deadlock in the bundle plugin during shutdown has been resolved (<a href="https://github.com/open-policy-agent/opa/issues/3363">#3363</a>)</li>
<li>An issue between bundle signing and bundle persistence when multiple data.json files are included in the bundle has been resolved (<a href="https://github.com/open-policy-agent/opa/issues/3472">#3472</a>)</li>
<li>The <code>github.com/open-policy-agent/opa/runtime#Params</code> struct now supports a router parameter to enable custom routes on the HTTP server.</li>
<li>The bundle manifest can now include an extra <code>metadata</code> key where arbitrary key-value pairs can be stored. Authored by @<a href="https://github.com/viovanov">viovanov</a></li>
<li>The bundle plugin now supports file:// urls in the <code>resource</code> field for test purposes.</li>
<li>The decision log plugin emits a clearer message at DEBUG instead of INFO when there is no work to do. Authored by <a href="https://github.com/andrewbanchich">andrewbanchich</a></li>
<li>The discovery plugin now supports a <code>resource</code> configuration field like the bundle plugin. Similarly, the <code>resource</code> is treated as the canonical setting to identify the discovery bundle.</li>
</ul>
<h3>Tooling</h3>
<ul>
<li>The <code>opa test</code> timeout as been increased to 30 seconds when benchmarking (<a href="https://github.com/open-policy-agent/opa/issues/3107">#3107</a>)</li>
<li>The <code>opa eval --schema</code> flag has been fixed to correctly set the schema when a <em>single</em> schema file is passed</li>
<li>The <code>opa build --debug</code> flag output has been improved for readability</li>
<li>The <code>array.items</code> JSON schema value is now supported by the type checker</li>
<li>The <code>opa fmt</code> subcommand can now exit with a non-zero status when a diff is detected (by passing <code>--fail</code>)</li>
<li>The <code>opa test</code> subcommand no longer emits bogus file paths when fed a file:// url</li>
</ul>
<h3>Built-in Functions</h3>
<ul>
<li>The <code>http.send</code> built-in function falls back to the system certificate pool when the <code>tls_ca_cert</code> or <code>tls_ca_cert_env_variable</code> options are not specified (<a href="https://github.com/open-policy-agent/opa/issues/2271">#2271</a>) authored by @<a href="https://github.com/olamiko">olamiko</a></li>
</ul>
<h3>Evaluation</h3>
<ul>
<li>The order of support rules emitted by partial evaluation is now deterministic (<a href="https://github.com/open-policy-agent/opa/issues/3453">#3453</a>) authored by @<a href="https://github.com/andrehaland">andrehaland</a></li>
<li>The big number performance regression caught by the fuzzer has been resolved (<a href="https://github.com/open-policy-agent/opa/issues/3262">#3262</a>)</li>
<li>The evaluator has been updated to memoize calls to rules with arguments (functions) within a single query. This avoids recomputing function results when the same input is passed multiple times (similar to how complete rules are memoized.)</li>
</ul>
<h3>WebAssembly</h3>
<ul>
<li>The <code>wasm</code> target no longer panics if the OPA binary does not include a wasm runtime (<a href="https://github.com/open-policy-agent/opa/issues/3264">#3264</a>)</li>
<li>The interrupt handling mechanism has been rewritten to make safe use of the wasmtime package. The SDK also returns structured errors now that are more aligned with topdown. (<a href="https://github.com/open-policy-agent/opa/issues/3225">#3225</a>)</li>
<li>The SDK provides the subset of required imports now (which is useful for debugging with opa_println in the runtime library if needed.)</li>
<li>The opa_number_float type has been removed from the value library (it was unused after moving to libmpdec)</li>
<li>The runtime library builder has been updated to use llvm-12 and the wasmtime-go package has been updated to v0.27.0</li>
</ul>
<h3>Documentation</h3>
<ul>
<li>The HTTP API authorization tutorial has been updated to show how to distribute policies using bundles</li>
<li>The Envoy tutorial has been tweaked to show better path matching examples</li>
</ul>
<h3>Infrastructure</h3>
<ul>
<li>The release-patch script has been improved to deal with <em>this file</em> in bugfix/patch releases (<a href="https://github.com/open-policy-agent/opa/issues/2533">#2533</a>) authored by @<a href="https://github.com/jjshanks">jjshanks</a></li>
<li>The Makefile check targets now rely on golangci-lint and many linting errors have been resolved (authored by @<a href="https://github.com/willbeason">willbeason</a>)</li>
<li>Multiple nightly fuzzing and data race issues in test cases have been resolved</li>
</ul>

## Prepare v0.29.0 release
<p style="font-size:12px;"> 27, May 2021 
<a href="https://github.com/open-policy-agent/opa/releases/tag/v0.29.0" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Signed-off-by: Torin Sandall <a href="mailto:torinsandall@gmail.com">torinsandall@gmail.com</a></p>

## v0.28.0
<p style="font-size:12px;"> 27, Apr 2021 
<a href="https://github.com/open-policy-agent/opa/releases/tag/v0.28.0" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release includes a number of features, enhancements, and fixes. The default<br />
branch for the Git repository has also been updated to <code>main</code>.</p>
<h4>Schema Annotations</h4>
<p>This release adds support for <em>annotations</em>. Annotations allow users to declare metadata on rules and packages. Currently, OPA supports one form of metadata: schema declarations. For example:</p>
<div class="highlight highlight-source-rego"><pre><span class="pl-k">package </span>example

<span class="pl-c"><span class="pl-c">#</span> METADATA</span>
<span class="pl-c"><span class="pl-c">#</span> schemas:</span>
<span class="pl-c"><span class="pl-c">#</span> - input: schema.service</span>
<span class="pl-en">deny</span>[<span class="pl-s"><span class="pl-pds">"</span>service is missing required 'owner' label<span class="pl-pds">"</span></span>] {
  input.kind <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">"</span>Service<span class="pl-pds">"</span></span>
<span class="pl-k">  not </span>input.metadata.labels.owner
}

<span class="pl-c"><span class="pl-c">#</span> METADATA</span>
<span class="pl-c"><span class="pl-c">#</span> schemas:</span>
<span class="pl-c"><span class="pl-c">#</span> - input: schema.deployment</span>
<span class="pl-en">deny</span>[<span class="pl-s"><span class="pl-pds">"</span>deployment replica count too low for 'production' namespace<span class="pl-pds">"</span></span>] {
  input.kind <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">"</span>Deployment<span class="pl-pds">"</span></span>
  input.metadata.namespace <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">"</span>production<span class="pl-pds">"</span></span>
  object.<span class="pl-c1">get</span>(input.spec, <span class="pl-s"><span class="pl-pds">"</span>replicas<span class="pl-pds">"</span></span>, <span class="pl-c1">1</span>) <span class="pl-k">&lt;</span> <span class="pl-c1">3</span>
}</pre></div>
<p>Users can include schema annotations in their policies to tell OPA about the structure of external data loaded under <code>input</code> or <code>data</code>. By learning the schema of base documents, OPA can surface mistakes in the policy at authoring time (e.g., referring to a non-existent field in a JSON object or calling a built-in function with an invalid value.) For more information on the annotations and schema support see the <a href="https://www.openpolicyagent.org/docs/latest/schemas/" rel="nofollow">Type Checking</a> page in the documentation. In the future, annotations will be expanded to support other kinds of metadata and additional tooling will be added to leverage them.</p>
<h3>Server</h3>
<ul>
<li>The server now automatically sets GOMAXPROCS when running inside of a container that has cgroups applied. This helps the Go runtime avoid consuming too many CPU resources and being throttled by the kernel. (<a href="https://github.com/open-policy-agent/opa/issues/3328">#3328</a>)</li>
<li>The server now logs an error if users enable the <code>token</code> authentication mode without a corresponding authorization policy. (<a href="https://github.com/open-policy-agent/opa/issues/3380">#3380</a>) authored by @<a href="https://github.com/kale-amruta">kale-amruta</a></li>
<li>The server now supports a <code>GET /v1/config</code> endpoint that returns OPA's active configuration. This API is useful if you need to debug the running configuration in an OPA configured via Discovery. (<a href="https://github.com/open-policy-agent/opa/issues/2020">#2020</a>)</li>
<li>The server now respects the <code>?pretty</code> option in the v0 API (<a href="https://github.com/open-policy-agent/opa/issues/3332">#3332</a>) authored by @<a href="https://github.com/clarshad">clarshad</a></li>
<li>The Bundle plugin is more forgiving when it comes to Etag processing on HTTP 304 responses (<a href="https://github.com/open-policy-agent/opa/issues/3361">#3361</a>)</li>
<li>The Decision Log plugin now supports a "Decision Per Second" rate limit configuration setting.</li>
<li>The Status plugin can now be configured to use a custom reporter similar to the Decision Log plugin (e.g., so that Status messages can be sent to AWS Kinesis, etc.)</li>
<li>The Status plugin now reports the number of decision logs that are dropped due to buffer limits.</li>
<li>The service clients can authenticate with the Azure Identity OAuth2 implementation the client credentials JWT flow is used (<a href="https://github.com/open-policy-agent/opa/issues/3372">#3372</a>)</li>
<li>Library users can now customize the logger used by the plugins by providing the <code>plugins.Logger</code> option when creating the plugin manager.</li>
</ul>
<h3>Tooling</h3>
<ul>
<li>The various OPA subcommands that accept schema files now accept a directory tree of schemas instead of only a single schema.</li>
<li>The <code>opa refactor move</code> subcommand was added to support package renaming use cases (<a href="https://github.com/open-policy-agent/opa/issues/3290">#3290</a>)</li>
<li>The <code>opa check</code> subcommand now supports a <code>-s</code>/<code>--schema</code> flag like the <code>opa eval</code> subcommand.</li>
</ul>
<h3>Documentation</h3>
<ul>
<li>The <a href="https://www.openpolicyagent.org/docs/latest/management-introduction/" rel="nofollow">Management API</a> docs have been restructured so that each API has a dedicated page. In addition, the <a href="https://www.openpolicyagent.org/docs/latest/management-bundles/#implementations" rel="nofollow">Bundle API</a> docs now include getting started steps for cloud-provider specific services (e.g., AWS, GCP, Azure, etc.)</li>
</ul>
<h3>Security</h3>
<ul>
<li>OPA now supports PKCS8 encoded EC private keys for JWT verification (which includes service authentication, bundle verification, and verification built-in functions) (<a href="https://github.com/open-policy-agent/opa/issues/3283">#3283</a>). Authored by @<a href="https://github.com/andrehaland">andrehaland</a>.</li>
<li>The bundle signing and verification APIs have been updated to support custom signers/verififers (<a href="https://github.com/open-policy-agent/opa/pull/3336">#3336</a>). Authored by @<a href="https://github.com/gshively11">gshively11</a>.</li>
</ul>
<h3>Evaluation</h3>
<ul>
<li>The <code>time.diff</code> function was added to support calculating differences between date/time values (<a href="https://github.com/open-policy-agent/opa/issues/3348">#3348</a>) authored by @<a href="https://github.com/andrehaland">andrehaland</a></li>
<li>The <code>units.parse_bytes</code> function now supports floating-point values (<a href="https://github.com/open-policy-agent/opa/issues/3297">#3297</a>) authored by @<a href="https://github.com/andy-paine">andy-paine</a></li>
<li>The evaluator was fixed to use correct bindings when evaluating the full-extent of a partial rule set. This issue was causing unexpected undefined results and evaluation errors in some rare cases. (<a href="https://github.com/open-policy-agent/opa/issues/3369">#3369</a> <a href="https://github.com/open-policy-agent/opa/issues/3376">#3376</a>)</li>
<li>The evaluator was fixed to correctly generate package paths when namespacing is disabled partial evaluation. (<a href="https://github.com/open-policy-agent/opa/issues/3302">#3302</a>).</li>
<li>The <code>http.send</code> function no longer errors out on invalid Expires headers. (<a href="https://github.com/open-policy-agent/opa/issues/3284">#3284</a>)</li>
<li>The inter-query cache now serializes elements on insertion thereby reducing memory usage significantly (because deserialized elements carry a ~20x cost.) (<a href="https://github.com/open-policy-agent/opa/issues/3042">#3042</a>)</li>
<li>The rule indexer was fixed to correctly handle mapped and non-mapped values which could occur with <code>glob.match</code> usage (<a href="https://github.com/open-policy-agent/opa/issues/3293">#3293</a>)</li>
</ul>
<h3>WebAssembly</h3>
<ul>
<li>The <code>opa eval</code> subcommand now correctly returns the set of all variable bindings and expression values when the <code>wasm</code> target is enabled. Previously it returned only set of variable bindings. (<a href="https://github.com/open-policy-agent/opa/issues/3281">#3281</a>)</li>
<li>The <code>glob.match</code> function now handles the default delimiter correctly. (<a href="https://github.com/open-policy-agent/opa/issues/3294">#3294</a>)</li>
<li>The <code>opa build</code> subcommand no longer requires a capabilities file when the <code>wasm</code> target is enabled. If capabilities are not provided, OPA will use the capabilities for its own version. (<a href="https://github.com/open-policy-agent/opa/issues/3270">#3270</a>)</li>
<li>The <code>opa build</code> subcommand now dumps the IR emitted by the planner when <code>--debug</code> is specified.</li>
<li>The <code>opa eval</code> subcommand no longer panics when a policy fails to type check and the <code>wasm</code> target is enabled.</li>
<li>The comparison functions can now return <code>false</code> instead of either being <code>true</code> or <code>undefined</code>.  (<a href="https://github.com/open-policy-agent/opa/issues/3271">#3271</a>)</li>
<li>The internal wasm runtime will now correctly return <code>CancelErr</code> to indicate cancellation errors (instead of <code>BuiltinErr</code> which it returned previously.)</li>
<li>The internal wasm runtime now correctly handles non-halt built-in errors (<a href="https://github.com/open-policy-agent/opa/issues/3320">#3320</a>)</li>
<li>The planner no longer generates unexpected scan statements when negation used over base documents under <code>data</code> (<a href="https://github.com/open-policy-agent/opa/issues/3279">#3279</a>) and (<a href="https://github.com/open-policy-agent/opa/issues/3305">#3305</a>)</li>
<li>The planner now correctly discards out-of-scope variables when exiting comprehensions (<a href="https://github.com/open-policy-agent/opa/issues/3325">#3325</a>)</li>
<li>The <code>rego</code> package no longer panics when the <code>wasm</code> target is enabled and undefined functions are encountered (<a href="https://github.com/open-policy-agent/opa/issues/3251">#3251</a>)</li>
<li>🎈 The remaining exceptions in the e2e test framework for the internal wasm runtime have been resolved.</li>
</ul>
<h3>Build</h3>
<ul>
<li>The <code>make image</code> target now uses the CI image for building the Go binary. This avoids platform-specific build issues by building the Go binary inside of Docker.</li>
</ul>

## v0.27.1
<p style="font-size:12px;"> 12, Mar 2021 
<a href="https://github.com/open-policy-agent/opa/releases/tag/v0.27.1" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release contains a fix for crashes experienced when configuring OPA to use S3 signing as service credentials (<a href="https://github.com/open-policy-agent/opa/issues/3255">#3255</a>).</p>
<p>In addition to that, we have a small number of enhancements and fixes:</p>
<h3>Tooling</h3>
<ul>
<li>The <code>eval</code> subcommand now allows using <code>--import</code> without using <code>--package</code>. Authored by @<a href="https://github.com/onelittlenightmusic">onelittlenightmusic</a>, <a href="https://github.com/open-policy-agent/opa/pull/3240">#3240</a>.</li>
</ul>
<h3>Compiler</h3>
<ul>
<li>The <code>ast</code> package now exports another method for JSON conversion, <code>ast.JSONWithOpts</code>, that allows further options to be set (<a href="https://github.com/open-policy-agent/opa/pull/3244">#3244</a>.</li>
</ul>
<h3>Server</h3>
<ul>
<li>REST plugins using <code>s3_signing</code> as credentials method can now include the specified service in the signature (SigV4). Authored by @<a href="https://github.com/cogwirrel">cogwirrel</a>, <a href="https://github.com/open-policy-agent/opa/pull/3210">#3210</a>.</li>
</ul>
<h3>Documentation</h3>
<ul>
<li>Remove soon-to-be deprecated <code>any</code> and <code>all</code> from the <a href="https://www.openpolicyagent.org/docs/v0.27.1/policy-reference/#aggregates" rel="nofollow">Policy Reference</a> (<a href="https://github.com/open-policy-agent/opa/pull/3241">#3241</a>) -- see also <a href="https://github.com/open-policy-agent/opa/issues/2437">#2437</a>.</li>
<li>Add missing <code>discovery.service</code> field to <a href="https://www.openpolicyagent.org/docs/v0.27.1/configuration/#discovery" rel="nofollow">Discovery configuration</a> table (<a href="https://github.com/open-policy-agent/opa/pull/3237">#3237</a>).</li>
<li>Fix dead links to the Envoy pages (<a href="https://github.com/open-policy-agent/opa/pull/3248">#3248</a>).</li>
</ul>
<h3>WebAssembly</h3>
<ul>
<li>Executions using the internal Wasm SDK will now be interrupted when the provided context is done (cancelled or deadline reached).</li>
<li>The generated Wasm modules could become much smaller: unused functions are replaced by <code>unreachable</code> stubs, and the heavyweight runtime components related to regular expressions are excluded when none of the regex-related builtins are used: <code>glob.match</code>, <code>regex.is_valid</code>, <code>regex.match</code>, <code>regex.is_valid</code>, and <code>regex.find_all_string_submatch_n</code>.</li>
<li>The Wasm runtime now allows passing in the time to be used for evaluation, enabling callers to control the time-of-day observed by Wasm compiled policies.</li>
<li>Wasmtime runtime has been updated to the latest version (v0.24.0).</li>
</ul>

## v0.27.0
<p style="font-size:12px;"> 08, Mar 2021 
<a href="https://github.com/open-policy-agent/opa/releases/tag/v0.27.0" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release contains a number of enhancements and bug fixes.</p>
<h3>Tooling</h3>
<ul>
<li>The <code>eval</code> subcommand now supports a <code>-s</code>/<code>--schema</code> flag that accepts a JSON schema for the <code>input</code> document. The schema is used when type checking the policy so that invalid references to (or operations on) <code>input</code> data are caught at compile time. In the future, the schema support will be expanded to accept multiple schemas and rule-level annotations. See the new <a href="https://www.openpolicyagent.org/docs/edge/schemas/" rel="nofollow">Schemas</a> documentation for details. Authored by @<a href="https://github.com/aavarghese">aavarghese</a> and @<a href="https://github.com/vazirim">vazirim</a>.</li>
<li>The <code>eval</code>, <code>test</code>, <code>bench</code> and REPL subcommands now supports a <code>-t</code>/<code>--target</code> flag to set the evaluation engine to use. The default engine is <code>rego</code> referring to the standard Rego interpreter in OPA. Users can now select <code>wasm</code> to enable Wasm compilation and execution of policies (<a href="https://github.com/open-policy-agent/opa/issues/2878">#2878</a>).</li>
<li>The <code>eval</code> subcommand now supports a <code>raw</code> option for <code>-f</code>/<code>--format</code> that is useful in bash scripts. Authored by @<a href="https://github.com/jaspervdj-luminal">jaspervdj-luminal</a>.</li>
<li>The test framework now supports "skippable" tests. Prefix the test name with <code>todo_</code> to have the test runner skip the test, e.g., <code>todo_test_allow { ... }</code>.</li>
<li>The <code>eval</code> subcommand now correctly supports the <code>--ignore</code> flag. Previously the flag was not being applied.</li>
</ul>
<h3>Server</h3>
<ul>
<li>The <code>POST /v1/compile</code> API now supports a <code>?metrics</code> query parameter similar to other APIs. Authored by @<a href="https://github.com/jkbschmid">jkbschmid</a>.</li>
<li>The directory used for persisting downloaded bundles can now be configured. See the <a href="https://www.openpolicyagent.org/docs/latest/configuration/" rel="nofollow">Configuration</a> page for details.</li>
<li>The HTTP Decision Logger plugin no longer blocks server shutdown for the grace period when there are no logs to upload.</li>
<li>The Bundle plugin now unregisters listeners correctly. This issue would cause listeners to be invoked when bundle updates were dispatched even if the listener was unregistered (<a href="https://github.com/open-policy-agent/opa/issues/3190">#3190</a>).</li>
<li>The server now correctly decodes policy IDs in the HTTP request URL. Authored by @<a href="https://github.com/mattmahn">mattmahn</a> (<a href="https://github.com/open-policy-agent/opa/issues/2116">#2116</a>).</li>
<li>The server now configures the <code>http_request_duration_seconds</code> metric (for all of the server endpoitns) with smaller, more granular buckets that better map to actual response latencies from OPA.  Authored by @<a href="https://github.com/luong-komorebi">luong-komorebi</a> (<a href="https://github.com/open-policy-agent/opa/issues/3196">#3196</a>).</li>
</ul>
<h3>Security</h3>
<ul>
<li>PKCS8 keys are now supported when signing bundles and communicating with control plane services. Previously only PKCS1 keys were supported (<a href="https://github.com/open-policy-agent/opa/issues/3116">#3116</a>).</li>
<li>The built-in OPA HTTP API authorizer policy can now return a <em>reason</em> to explain why a request to the OPA API is denied (<a href="https://github.com/open-policy-agent/opa/issues/3056">#3056</a>). See the <a href="https://www.openpolicyagent.org/docs/edge/security/" rel="nofollow">Security</a> documentation for details. Thanks to @<a href="https://github.com/ajanthan">ajanthan</a> for helping improve this.</li>
</ul>
<h3>Compiler</h3>
<ul>
<li>The compiler can be configured to emit debug messages that explain comprehension indexing decisions. Debug messages can be enabled when running <code>opa build</code> with <code>--debug</code>.</li>
<li>A panic was fixed in one of the rewriting stages when comprehensions were used as object keys (<a href="https://github.com/open-policy-agent/opa/issues/2915">#2915</a>)</li>
</ul>
<h3>Evaluation</h3>
<ul>
<li>A bug in big integer comparison was fixed. This issue was discovered when comparing serial numbers from X.509 certificates. Authored by @<a href="https://github.com/andrehaland">andrehaland</a> (<a href="https://github.com/open-policy-agent/opa/issues/3147">#3147</a>).</li>
<li>The <code>io.jwt.decode_verify</code> function now uses the environment supplied time-of-day value instead of calling <code>time.Now()</code> (<a href="https://github.com/open-policy-agent/opa/issues/3105">#3105</a>).</li>
</ul>
<h3>Documentation</h3>
<ul>
<li>The documentation now includes a dedicated section the OPA-Envoy integration. See <a href="https://www.openpolicyagent.org/docs/latest/envoy-introduction/" rel="nofollow">https://www.openpolicyagent.org/docs/latest/envoy-introduction/</a> for details.</li>
<li>The ecosystem page now ranks integrations by number of unique domains instead of the sheer number of references.</li>
</ul>
<h3>WebAssembly</h3>
<ul>
<li>The <code>data</code> document no longer needs to be initialized to an empty object (<a href="https://github.com/open-policy-agent/opa/issues/3130">#3130</a>).</li>
<li>The mpd library is now initalized by the module's <code>Start</code> function (<a href="https://github.com/open-policy-agent/opa/issues/3110">#3110</a>).</li>
<li>The planner now longer re-plans rules blindly when <code>with</code> statements are encountered (<a href="https://github.com/open-policy-agent/opa/issues/3150">#3150</a>).</li>
<li>The planner and compiler now support dynamic dispatch. Previously the planner would enumerate all functions and invocation was controlled at runtime (<a href="https://github.com/open-policy-agent/opa/issues/2936">#2936</a>).</li>
<li>The compiler now inserts memoization instructions into function bodies instead of at callsites. This reduces the number of wasm instructions in the resulting binary (<a href="https://github.com/open-policy-agent/opa/pull/3169">#3169</a>).</li>
<li>The wasmtime runtime is now the default runtime used by OPA to execute compiled policies. The new runtime no longer leaks memory when policies are reloaded.</li>
<li>The planner and compiler now intern strings and booleans and implement a few micro-optimizations to reduce the size of the resulting binary.</li>
<li>The capabilities support has been updated to include an ABI major and minor version for tracking backwards compatibility on compiled policies (<a href="https://github.com/open-policy-agent/opa/issues/3120">#3120</a>).</li>
</ul>
<h3>Backwards Compatibility</h3>
<ul>
<li>The <code>opa test</code> subcommand previously supported a <code>-t</code> flag as shorthand for <code>--timeout</code>. With this release, the <code>-t</code> shorthand has been redefined for <code>--target</code>. After searching GitHub for examples of <code>opa test -t</code> (and finding nothing) we felt comfortable making this backwards incompatible change.</li>
<li>The Go version used to build the OPA release has been updated from <code>1.14.9</code> to <code>1.15.8</code>. Because of this, TLS certificates that rely on Common Name for verification are no longer supported and will not work. For more information see <a class="issue-link js-issue-link" href="https://github.com/golang/go/issues/39568">golang/go#39568</a>.</li>
</ul>

## v0.26.0
<p style="font-size:12px;"> 20, Jan 2021 
<a href="https://github.com/open-policy-agent/opa/releases/tag/v0.26.0" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release contains a number of enhancements and bug fixes.</p>
<h3>Built-in Functions</h3>
<ul>
<li>
<p>This release includes a number of built-in function improvements for Wasm compiled policies. The following built-in functions have been implemented natively and no longer need to be supplied by SDKs: <code>graph.reachable</code>, <code>json.filter</code>, <code>json.remove</code>, <code>object.get</code>, <code>object.remove</code>, and <code>object.union</code>.</p>
</li>
<li>
<p>This release fixes several bugs in the Wasm implementation of certain <code>regex</code> built-in functions (<a href="https://github.com/open-policy-agent/opa/issues/2962">#2962</a>), <code>format_int</code> (<a href="https://github.com/open-policy-agent/opa/issues/2923">#2923</a>) and <code>round</code> (<a href="https://github.com/open-policy-agent/opa/pull/2999">#2999</a>).</p>
</li>
<li>
<p>This release adds <code>ceil</code> and <code>floor</code> built-in functions. Previously these could be implemented in Rego using <code>round</code> however these are more convenient.</p>
</li>
</ul>
<h3>Enhancements</h3>
<ul>
<li>
<p>OPA has been extended support <a href="https://www.openpolicyagent.org/docs/latest/configuration/#oauth2-jwt-bearer-grant-type" rel="nofollow">OAuth2 JWT Bearer Grant Type</a> and <a href="https://www.openpolicyagent.org/docs/edge/configuration/#oauth2-client-credentials-jwt-authentication" rel="nofollow">OAuth2 Client Credential JWT</a> authentication options for communicating with control plane services. This change allows OPA to use services that rely on Ping Identity as well as GCP service accounts for authentication. OPA has also been extended to support <a href="https://www.openpolicyagent.org/docs/edge/configuration/#custom-plugin" rel="nofollow">custom authentication plugins</a> (thanks @<a href="https://github.com/gshively11">gshively11</a>).</p>
</li>
<li>
<p>OPA plugins can now enter a "WARN" state to indicate they are operating in a degraded capacity (thanks @<a href="https://github.com/gshively11">gshively11</a>).</p>
</li>
<li>
<p>The <code>opa bench</code> command can now benchmark partial evaluation queries. The options to enable partial evaluation are shared with <code>opa eval</code>. See <code>opa bench --help</code> for details.</p>
</li>
<li>
<p>Wasm compiled policies now contain source locations that are included inside of runtime error messages (such as object key conflicts.) In addition, Wasm compiled policies only export the minimal set of APIs described on the <a href="https://www.openpolicyagent.org/docs/latest/wasm/#exports" rel="nofollow">WebAssembly#exports</a> page.</p>
</li>
</ul>
<h3>Fixes</h3>
<ul>
<li>ast: Fix parsing of numbers to reject leading zeroes (<a href="https://github.com/open-policy-agent/opa/issues/2947">#2947</a>) authored by @<a href="https://github.com/LCartwright">LCartwright</a>.</li>
<li>bundle: Fix loader to only verify bundle keys if configured to do so (<a href="https://github.com/open-policy-agent/opa/issues/3028">#3028</a>).</li>
<li>cmd: Fix build to avoid packaging policy.wasm twice (<a href="https://github.com/open-policy-agent/opa/issues/3007">#3007</a>).</li>
<li>cmd: Fix pretty-printed PE output to hide spurious blank lines</li>
<li>server: Fix false-positive in bundle root check that would prevent data updates in some cases (<a href="https://github.com/open-policy-agent/opa/issues/2868">#2868</a>).</li>
<li>server: Fix query cache to respect ?instrument option (<a href="https://github.com/open-policy-agent/opa/issues/3000">#3000</a>).</li>
<li>server: Fix server to support discovery on inter-query cache configuration</li>
<li>topdown: Fix PE to avoid generating expressions that do not type check (<a href="https://github.com/open-policy-agent/opa/issues/3012">#3012</a>).</li>
<li>wasm: Fix planner to avoid generating a conflict error in some cases (<a href="https://github.com/open-policy-agent/opa/issues/2926">#2926</a>).</li>
<li>wasm: Fix planner to generate correct virtual document iteration instructions (<a href="https://github.com/open-policy-agent/opa/issues/3065">#3065</a>).</li>
<li>wasm, topdown: Fix with keyword handle to ensure last statement wins (<a class="issue-link js-issue-link" href="https://github.com/open-policy-agent/opa/pull/3010">#3010</a>).</li>
<li>wasm: Fix planner to handle assignment conflicts correctly when else keyword is used (<a class="issue-link js-issue-link" href="https://github.com/open-policy-agent/opa/pull/3031">#3031</a>).</li>
</ul>
<h3>Documentation</h3>
<ul>
<li>Add new section on integrating policies with OAuth2 and OIDC.</li>
<li>Update Kubernetes admission control tutorial to work as non-root user.</li>
<li>Fix link to signing documentation (<a href="https://github.com/open-policy-agent/opa/issues/3027">#3027</a>) authored by @<a href="https://github.com/princespaghetti">princespaghetti</a>.</li>
</ul>
<h3>Backwards Compatibility</h3>
<ul>
<li>Previously, OPA deduplicated sets and objects in all cases except when iterating over/referring directly to values generated by partial rules. This inconsistency would only be noticed when running ad-hoc queries or within policies when aggregating the results of array comprehensions (e.g., <code>count([1 | p[x]])</code> could observe duplicates in <code>p</code>.) This release removes the inconsistency by deduplicating sets and objects in all cases (<a href="https://github.com/open-policy-agent/opa/issues/429">#429</a>). This was the second oldest open issue on the project.</li>
</ul>
<h3>Deprecations</h3>
<ul>
<li>OPA now logs warnings when it receives legacy <code>bundle</code> config sections instead of the <code>bundles</code> section introduced in v0.13.0.</li>
</ul>

## v0.25.2
<p style="font-size:12px;"> 08, Dec 2020 
<a href="https://github.com/open-policy-agent/opa/releases/tag/v0.25.2" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release extends the HTTP server authorizer (<code>--authorization=basic</code>) to supply the HTTP message body in the <code>input</code> document. See the <a href="https://www.openpolicyagent.org/docs/edge/security/#authentication-and-authorization" rel="nofollow">Authentication and Authorization</a> section in the security documentation for details.</p>

## v0.25.1
<p style="font-size:12px;"> 07, Dec 2020 
<a href="https://github.com/open-policy-agent/opa/releases/tag/v0.25.1" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release contains a fix for running OPA under Docker with a non-default working directory (<a href="https://github.com/open-policy-agent/opa/issues/2974">#2974</a>):</p>
<pre><code>/opa: error while loading shared libraries: libwasmer.so: cannot open shared object file: No such file or directory
</code></pre>
