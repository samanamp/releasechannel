# Jaeger

<div>
<demo-component app-code="jaeger"/>
</div>


## Release 1.22.0
<p style="font-size:12px;"> 23, Feb 2021 
<a href="https://github.com/jaegertracing/jaeger/releases/tag/v1.22.0" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Backend Changes</h3>
<h4>Breaking Changes</h4>
<ul>
<li>
<p>Remove deprecated TLS flags (<a href="https://github.com/jaegertracing/jaeger/issues/2790">#2790</a>, <a href="https://github.com/albertteoh">@albertteoh</a>):</p>
<ul>
<li><code>--cassandra.tls</code> is replaced by <code>--cassandra.tls.enabled</code></li>
<li><code>--cassandra-archive.tls</code> is replaced by <code>--cassandra-archive.tls.enabled</code></li>
<li><code>--collector.grpc.tls</code> is replaced by <code>--collector.grpc.tls.enabled</code></li>
<li><code>--collector.grpc.tls.client.ca</code> is replaced by <code>--collector.grpc.tls.client-ca</code></li>
<li><code>--es.tls</code> is replaced by <code>--es.tls.enabled</code></li>
<li><code>--es-archive.tls</code> is replaced by <code>--es-archive.tls.enabled</code></li>
<li><code>--kafka.consumer.tls</code> is replaced by <code>--kafka.consumer.tls.enabled</code></li>
<li><code>--kafka.producer.tls</code> is replaced by <code>--kafka.producer.tls.enabled</code></li>
<li><code>--reporter.grpc.tls</code> is replaced by <code>--reporter.grpc.tls.enabled</code></li>
</ul>
</li>
<li>
<p>Remove deprecated flags of Query Server  <code>--query.port</code> and <code>--query.host-port</code>, please use dedicated HTTP <code>--query.http-server.host-port</code> (defaults to <code>:16686</code>) and gRPC <code>--query.grpc-server.host-port</code> (defaults to <code>:16685</code>)  host-ports flags instead (<a href="https://github.com/jaegertracing/jaeger/pull/2772">#2772</a>, <a href="https://github.com/rjs211">@rjs211</a>)</p>
<ul>
<li>By default, if no flags are set, the query server starts on the dedicated ports.  To use common port for gRPC and  HTTP endpoints, the host-port flags have to be explicitly set</li>
</ul>
</li>
<li>
<p>Remove deprecated CLI flags (<a href="https://github.com/jaegertracing/jaeger/issues/2751">#2751</a>, <a href="https://github.com/LostLaser">@LostLaser</a>):</p>
<ul>
<li><code>--collector.http-port</code> is replaced by <code>--collector.http-server.host-port</code></li>
<li><code>--collector.grpc-port</code> is replaced by <code>--collector.grpc-server.host-port</code></li>
<li><code>--collector.zipkin.http-port</code> is replaced by <code>--collector.zipkin.host-port</code></li>
</ul>
</li>
<li>
<p>Remove deprecated flags <code>--health-check-http-port</code> &amp; <code>--admin-http-port</code>, please use <code>--admin.http.host-port</code> (<a href="https://github.com/jaegertracing/jaeger/pull/2752">#2752</a>, <a href="https://github.com/pradeepnnv">@pradeepnnv</a>)</p>
</li>
<li>
<p>Remove deprecated flag <code>--es.max-num-spans</code>, please use <code>--es.max-doc-count</code> (<a href="https://github.com/jaegertracing/jaeger/pull/2482">#2482</a>, <a href="https://github.com/BernardTolosajr">@BernardTolosajr</a>)</p>
</li>
<li>
<p>Remove deprecated flag <code>--jaeger.tags</code>, please use <code>--agent.tags</code> (<a href="https://github.com/jaegertracing/jaeger/pull/2753">#2753</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</p>
</li>
<li>
<p>Remove deprecated Cassandra flags (<a href="https://github.com/jaegertracing/jaeger/pull/2789">#2789</a>, <a href="https://github.com/albertteoh">@albertteoh</a>):</p>
<ul>
<li><code>--cassandra.enable-dependencies-v2</code> - Jaeger will automatically detect the version of the dependencies table</li>
<li><code>--cassandra.tls.verify-host</code> - please use <code>--cassandra.tls.skip-host-verify</code> instead</li>
</ul>
</li>
<li>
<p>Remove incorrectly scoped downsample flags from the query service (<a href="https://github.com/jaegertracing/jaeger/pull/2782">#2782</a>, <a href="https://github.com/joe-elliott">@joe-elliott</a>)</p>
<ul>
<li><code>--downsampling.hashsalt</code> removed from jaeger-query</li>
<li><code>--downsampling.ratio</code> removed from jaeger-query</li>
</ul>
</li>
</ul>
<h4>New Features</h4>
<ul>
<li>
<p>Add TLS Support for gRPC and HTTP endpoints of the Query and Collector servers (<a href="https://github.com/jaegertracing/jaeger/pull/2337">#2337</a>, <a href="https://github.com/jaegertracing/jaeger/pull/2772">#2772</a>, <a href="https://github.com/jaegertracing/jaeger/pull/2798">#2798</a>, <a href="https://github.com/rjs211">@rjs211</a>)</p>
<ul>
<li>If TLS in enabled on either or both of gRPC or HTTP endpoints, the gRPC host-port and the HTTP host-port have to be different</li>
<li>If TLS is disabled on both endpoints, common HTTP and gRPC host-port can be explicitly set using the following host-port flags respectively:
<ul>
<li>Query: <code>--query.http-server.host-port</code> and  <code>--query.grpc-server.host-port</code></li>
<li>Collector: <code>--collector.http-server.host-port</code> and <code>--collector.grpc-server.host-port</code></li>
</ul>
</li>
</ul>
</li>
<li>
<p>Add support for Kafka SASL/PLAIN authentication via SCRAM-SHA-256 or SCRAM-SHA-512 mechanism (<a href="https://github.com/jaegertracing/jaeger/pull/2724">#2724</a>, <a href="https://github.com/WalkerWang731">@WalkerWang731</a>)</p>
</li>
<li>
<p>[agent] Add metrics to show connections status between agent and collectors (<a href="https://github.com/jaegertracing/jaeger/pull/2657">#2657</a>, <a href="https://github.com/WalkerWang731">@WalkerWang731</a>)</p>
</li>
<li>
<p>Add plaintext as a supported kafka auth option (<a href="https://github.com/jaegertracing/jaeger/pull/2721">#2721</a>, <a href="https://github.com/pdepaepe">@pdepaepe</a>)</p>
</li>
<li>
<p>Add ability to use JS file for UI configuration (<a class="issue-link js-issue-link" href="https://github.com/jaegertracing/jaeger/issues/123">#123</a> from jaeger-ui) (<a href="https://github.com/jaegertracing/jaeger/pull/2707">#2707</a>, <a href="https://github.com/th3M1ke">@th3M1ke</a>)</p>
</li>
<li>
<p>Support Elasticsearch ILM for managing jaeger indices (<a href="https://github.com/jaegertracing/jaeger/pull/2796">#2796</a>, <a href="https://github.com/bhiravabhatla">@bhiravabhatla</a>)</p>
</li>
<li>
<p>Push official images to quay.io, in addition to Docker Hub (<a href="https://github.com/jaegertracing/jaeger/pull/2783">#2783</a>, <a href="https://github.com/Ashmita152">@Ashmita152</a>)</p>
</li>
<li>
<p>Add status command (<a href="https://github.com/jaegertracing/jaeger/pull/2684">#2684</a>, <a href="https://github.com/sniperking1234">@sniperking1234</a>)</p>
<ul>
<li>Usage:
<div class="highlight highlight-source-shell"><pre>$ ./cmd/collector/collector-darwin-amd64 status
{<span class="pl-s"><span class="pl-pds">"</span>status<span class="pl-pds">"</span></span>:<span class="pl-s"><span class="pl-pds">"</span>Server available<span class="pl-pds">"</span></span>,<span class="pl-s"><span class="pl-pds">"</span>upSince<span class="pl-pds">"</span></span>:<span class="pl-s"><span class="pl-pds">"</span>2021-02-19T17:57:12.671902+11:00<span class="pl-pds">"</span></span>,<span class="pl-s"><span class="pl-pds">"</span>uptime<span class="pl-pds">"</span></span>:<span class="pl-s"><span class="pl-pds">"</span>25.241233383s<span class="pl-pds">"</span></span>}</pre></div>
</li>
</ul>
</li>
<li>
<p>Support configurable date separator for Elasticsearch index names (<a href="https://github.com/jaegertracing/jaeger/pull/2637">#2637</a>, <a href="https://github.com/sniperking1234">@sniperking1234</a>)</p>
</li>
</ul>
<h4>Bug fixes, Minor Improvements</h4>
<ul>
<li>Use workaround for windows x509.SystemCertPool() (<a href="https://github.com/jaegertracing/jaeger/pull/2756">#2756</a>, <a href="https://github.com/Ashmita152">@Ashmita152</a>)</li>
<li>Guard against mal-formed payloads received by the agent, potentially causing high memory utilization (<a href="https://github.com/jaegertracing/jaeger/pull/2780">#2780</a>, <a href="https://github.com/jpkrohling">@jpkrohling</a>)</li>
<li>Expose cache TTL for ES span writer index+service (<a href="https://github.com/jaegertracing/jaeger/pull/2737">#2737</a>, <a href="https://github.com/necrolyte2">@necrolyte2</a>)</li>
<li>Copy spans from memory store (<a href="https://github.com/jaegertracing/jaeger/pull/2720">#2720</a>, <a href="https://github.com/bobrik">@bobrik</a>)</li>
<li>[pkg/queue] Add <code>StartConsumersWithFactory</code> function (<a href="https://github.com/jaegertracing/jaeger/pull/2714">#2714</a>, <a href="https://github.com/mx-psi">@mx-psi</a>)</li>
<li>Fix potential cross-site scripting issue (<a href="https://github.com/jaegertracing/jaeger/pull/2697">#2697</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Updated gRPC Storage Plugin README with example (<a href="https://github.com/jaegertracing/jaeger/pull/2687">#2687</a>, <a href="https://github.com/js8080">@js8080</a>)</li>
<li>Deduplicate collector tags (<a href="https://github.com/jaegertracing/jaeger/pull/2658">#2658</a>, <a href="https://github.com/Betula-L">@Betula-L</a>)</li>
<li>Add latency metrics on collector HTTP endpoints (<a href="https://github.com/jaegertracing/jaeger/pull/2664">#2664</a>, <a href="https://github.com/dimitarvdimitrov">@dimitarvdimitrov</a>)</li>
<li>Fix collector panic due to sarama sdk (<a href="https://github.com/jaegertracing/jaeger/pull/2654">#2654</a>, <a href="https://github.com/Betula-L">@Betula-L</a>)</li>
<li>Handle collector Start error (<a href="https://github.com/jaegertracing/jaeger/pull/2647">#2647</a>, <a href="https://github.com/albertteoh">@albertteoh</a>)</li>
<li>[anonymizer] Save trace in UI format (<a href="https://github.com/jaegertracing/jaeger/pull/2629">#2629</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
</ul>
<h3>UI Changes</h3>
<ul>
<li>UI pinned to version 1.13.0. The changelog is available here <a href="https://github.com/jaegertracing/jaeger-ui/blob/master/CHANGELOG.md#v1130-february-20-2021">v1.13.0</a></li>
</ul>

## Release 1.21.0
<p style="font-size:12px;"> 16, Nov 2020 
<a href="https://github.com/jaegertracing/jaeger/releases/tag/v1.21.0" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Backend Changes</h3>
<h4>New Features</h4>
<ul>
<li>New debug Docker images for Jaeger backends are included in the distribution (<a href="https://github.com/jaegertracing/jaeger/pull/2545">#2545</a>, <a href="https://github.com/Ashmita152">@Ashmita152</a>)</li>
<li>A utility to anonymize a trace for sharing publicly (<a href="https://github.com/jaegertracing/jaeger/pull/2621">#2621</a>, <a href="https://github.com/jaegertracing/jaeger/pull/2585">#2585</a>, <a href="https://github.com/Ashmita152">@Ashmita152</a>)</li>
<li>Sampling strategies file can be loaded from a URL, not just a file path (<a href="https://github.com/jaegertracing/jaeger/pull/2519">#2519</a>, <a href="https://github.com/goku321">@goku321</a>)</li>
<li>Configuration parameters can be inspected at runtime via <code>/debug/vars</code> admin endpoint (<a href="https://github.com/jaegertracing/jaeger/pull/2496">#2496</a>, <a href="https://github.com/dstdfx">@dstdfx</a>)</li>
<li>OTLP-proto encoding for Kafka supported in the OTEL Ingester (<a href="https://github.com/jaegertracing/jaeger/pull/2580">#2580</a>, <a href="https://github.com/XSAM">@XSAM</a>)</li>
<li>Display backend &amp; UI versions in Jaeger UI
<ul>
<li>Inject version info into index.html (<a href="https://github.com/jaegertracing/jaeger/pull/2547">#2547</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Added jaeger ui version to about menu (<a href="https://github.com/jaegertracing/jaeger-ui/pull/606">#606</a>, <a href="https://github.com/alanisaac">@alanisaac</a>)</li>
</ul>
</li>
</ul>
<h4>Bug fixes, Minor Improvements</h4>
<ul>
<li>Update x/text to v0.3.4 (<a href="https://github.com/jaegertracing/jaeger/pull/2625">#2625</a>, <a href="https://github.com/objectiser">@objectiser</a>)</li>
<li>Update CodeQL to latest best practices (<a href="https://github.com/jaegertracing/jaeger/pull/2615">#2615</a>, <a href="https://github.com/jhutchings1">@jhutchings1</a>)</li>
<li>Bump opentelemetry-collector to v0.14.0 (<a href="https://github.com/jaegertracing/jaeger/pull/2617">#2617</a>, <a href="https://github.com/Vemmy124">@Vemmy124</a>)</li>
<li>Bump Badger to v1.6.2 (<a href="https://github.com/jaegertracing/jaeger/pull/2613">#2613</a>, <a href="https://github.com/Ackar">@Ackar</a>)</li>
<li>Fix sarama consumer deadlock (<a href="https://github.com/jaegertracing/jaeger/pull/2587">#2587</a>, <a href="https://github.com/albertteoh">@albertteoh</a>)</li>
<li>Avoid deadlock if Stop is called before Serve (<a href="https://github.com/jaegertracing/jaeger/pull/2608">#2608</a>, <a href="https://github.com/chlunde">@chlunde</a>)</li>
<li>Return buffers to pool on network errors or queue overflow (<a href="https://github.com/jaegertracing/jaeger/pull/2609">#2609</a>, <a href="https://github.com/chlunde">@chlunde</a>)</li>
<li>Clarify deadlock panic message (<a href="https://github.com/jaegertracing/jaeger/pull/2605">#2605</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>fix: don't create tags w/ empty name for internal zipkin spans (<a href="https://github.com/jaegertracing/jaeger/pull/2596">#2596</a>, <a href="https://github.com/mzahor">@mzahor</a>)</li>
<li>TBufferedServer: Avoid channel close/send race on Stop (<a href="https://github.com/jaegertracing/jaeger/pull/2583">#2583</a>, <a href="https://github.com/chlunde">@chlunde</a>)</li>
<li>Bumped OpenTelemetry Collector to v0.12.0 (<a href="https://github.com/jaegertracing/jaeger/pull/2562">#2562</a>, <a href="https://github.com/jpkrohling">@jpkrohling</a>)</li>
<li>Disable Zipkin server if port/address is not configured (<a href="https://github.com/jaegertracing/jaeger/pull/2554">#2554</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>[hotrod] Add links to traces (<a href="https://github.com/jaegertracing/jaeger/pull/2536">#2536</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>OTel Cassandra/Elasticsearch Exporter queue defaults (<a href="https://github.com/jaegertracing/jaeger/pull/2533">#2533</a>, <a href="https://github.com/joe-elliott">@joe-elliott</a>)</li>
<li>[otel] Update jaeger-lib to v2.4.0 (<a href="https://github.com/jaegertracing/jaeger/pull/2538">#2538</a>, <a href="https://github.com/dstdfx">@dstdfx</a>)</li>
<li>Remove unnecessary ServiceName index seek if tags query is available (<a href="https://github.com/jaegertracing/jaeger/pull/2535">#2535</a>, <a href="https://github.com/burmanm">@burmanm</a>)</li>
<li>Update static UI assets path in contrib doc (<a href="https://github.com/jaegertracing/jaeger/pull/2548">#2548</a>, <a href="https://github.com/albertteoh">@albertteoh</a>)</li>
</ul>
<h3>UI Changes</h3>
<ul>
<li>UI pinned to version 1.12.0. The changelog is available here <a href="https://github.com/jaegertracing/jaeger-ui/blob/master/CHANGELOG.md#v1120-november-14-2020">v1.12.0</a></li>
</ul>

## Release 1.20.0
<p style="font-size:12px;"> 29, Sep 2020 
<a href="https://github.com/jaegertracing/jaeger/releases/tag/v1.20.0" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Backend Changes</h3>
<h4>Breaking Changes</h4>
<ul>
<li>
<p>Configurable ES doc count (<a href="https://github.com/jaegertracing/jaeger/pull/2453">#2453</a>, <a href="https://github.com/albertteoh">@albertteoh</a>)</p>
<p>The <code>--es.max-num-spans</code> flag has been deprecated in favour of <code>--es.max-doc-count</code>.<br />
<code>--es.max-num-spans</code> is marked for removal in v1.21.0 as indicated in the flag description.</p>
<p>If both <code>--es.max-num-spans</code> and <code>--es.max-doc-count</code> are set, the lesser of the two will be used.</p>
<p>The use of <code>--es.max-doc-count</code> (which defaults to 10,000) will limit the results from all Elasticsearch<br />
queries by the configured value, limiting counts for Jaeger UI:</p>
<ul>
<li>Services</li>
<li>Operations</li>
<li>Dependencies (edges in a dependency graph)</li>
<li>Span fetch size for a trace</li>
</ul>
</li>
<li>
<p>The default value for the flag <code>query.max-clock-skew-adjustment</code> has changed to <code>0s</code>, meaning that the clock skew adjustment is now disabled by default. See <a href="https://github.com/jaegertracing/jaeger/issues/1459">#1459</a>.</p>
</li>
</ul>
<h4>New Features</h4>
<ul>
<li>Grpc plugin archive storage support (<a href="https://github.com/jaegertracing/jaeger/pull/2317">#2317</a>, <a href="https://github.com/m8rge">@m8rge</a>)</li>
<li>Separate Ports for GRPC and HTTP requests in Query Server (<a href="https://github.com/jaegertracing/jaeger/pull/2387">#2387</a>, <a href="https://github.com/rjs211">@rjs211</a>)</li>
<li>Configurable ES doc count (<a href="https://github.com/jaegertracing/jaeger/pull/2453">#2453</a>, <a href="https://github.com/albertteoh">@albertteoh</a>)</li>
<li>Add storage metrics to OTEL, metrics by span service name (<a href="https://github.com/jaegertracing/jaeger/pull/2431">#2431</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
</ul>
<h4>Bug fixes, Minor Improvements</h4>
<ul>
<li>Increase coverage on otel/app/defaultconfig and otel/app/defaultcomponents (<a href="https://github.com/jaegertracing/jaeger/pull/2515">#2515</a>, <a href="https://github.com/joe-elliott">@joe-elliott</a>)</li>
<li>Use OTEL Kafka Exporter/Receiver Instead of Jaeger Core (<a href="https://github.com/jaegertracing/jaeger/pull/2494">#2494</a>, <a href="https://github.com/joe-elliott">@joe-elliott</a>)</li>
<li>Fix OTEL kafka receiver/ingester panic (<a href="https://github.com/jaegertracing/jaeger/pull/2512">#2512</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Disable clock-skew-adjustment by default. (<a href="https://github.com/jaegertracing/jaeger/pull/2513">#2513</a>, <a href="https://github.com/jpkrohling">@jpkrohling</a>)</li>
<li>Fix ES OTEL status code (<a href="https://github.com/jaegertracing/jaeger/pull/2501">#2501</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>OTel: Factored out Config Factory (<a href="https://github.com/jaegertracing/jaeger/pull/2495">#2495</a>, <a href="https://github.com/joe-elliott">@joe-elliott</a>)</li>
<li>Fix failing ServerInUseHostPort test on MacOS (<a href="https://github.com/jaegertracing/jaeger/pull/2477">#2477</a>, <a href="https://github.com/albertteoh">@albertteoh</a>)</li>
<li>Fix unmarshalling in OTEL badger (<a href="https://github.com/jaegertracing/jaeger/pull/2488">#2488</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Improve UI placeholder message (<a href="https://github.com/jaegertracing/jaeger/pull/2487">#2487</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Translate OTEL instrumentation library to ES DB model (<a href="https://github.com/jaegertracing/jaeger/pull/2484">#2484</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add partial retry capability to OTEL ES exporter. (<a href="https://github.com/jaegertracing/jaeger/pull/2456">#2456</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Log deprecation warning only when deprecated flags are set (<a href="https://github.com/jaegertracing/jaeger/pull/2479">#2479</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Clean-up Badger's trace-not-found check (<a href="https://github.com/jaegertracing/jaeger/pull/2481">#2481</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Run the jaeger-agent as a non-root user by default (<a href="https://github.com/jaegertracing/jaeger/pull/2466">#2466</a>, <a href="https://github.com/chgl">@chgl</a>)</li>
<li>Regenerate certificates to use SANs instead of Common Name (<a href="https://github.com/jaegertracing/jaeger/pull/2461">#2461</a>, <a href="https://github.com/albertteoh">@albertteoh</a>)</li>
<li>Support custom port in cassandra schema creation (<a href="https://github.com/jaegertracing/jaeger/pull/2472">#2472</a>, <a href="https://github.com/MarianZoll">@MarianZoll</a>)</li>
<li>Consolidated OTel ES IndexNameProviders (<a href="https://github.com/jaegertracing/jaeger/pull/2458">#2458</a>, <a href="https://github.com/joe-elliott">@joe-elliott</a>)</li>
<li>Add positive confirmation that Agent made a connection to Collector (… (<a href="https://github.com/jaegertracing/jaeger/pull/2423">#2423</a>, <a href="https://github.com/BernardTolosajr">@BernardTolosajr</a>)</li>
<li>Propagate TraceNotFound error from grpc storage plugins (<a href="https://github.com/jaegertracing/jaeger/pull/2455">#2455</a>, <a href="https://github.com/joe-elliott">@joe-elliott</a>)</li>
<li>Use new ES reader implementation in OTEL (<a href="https://github.com/jaegertracing/jaeger/pull/2441">#2441</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Updated grpc-go to v1.29.1 (<a href="https://github.com/jaegertracing/jaeger/pull/2445">#2445</a>, <a href="https://github.com/jpkrohling">@jpkrohling</a>)</li>
<li>Remove olivere elastic client from OTEL (<a href="https://github.com/jaegertracing/jaeger/pull/2448">#2448</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Use queue retry per exporter (<a href="https://github.com/jaegertracing/jaeger/pull/2444">#2444</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add context.Context to WriteSpan (<a href="https://github.com/jaegertracing/jaeger/pull/2436">#2436</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Fix mutex unlock in storage exporters (<a href="https://github.com/jaegertracing/jaeger/pull/2442">#2442</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add Grafana integration example (<a href="https://github.com/jaegertracing/jaeger/pull/2408">#2408</a>, <a href="https://github.com/fktkrt">@fktkrt</a>)</li>
<li>Fix TLS flags settings in jaeger OTEL receiver (<a href="https://github.com/jaegertracing/jaeger/pull/2438">#2438</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add context to dependencies endpoint (<a href="https://github.com/jaegertracing/jaeger/pull/2434">#2434</a>, <a href="https://github.com/yoave23">@yoave23</a>)</li>
<li>Fix error equals (<a href="https://github.com/jaegertracing/jaeger/pull/2429">#2429</a>, <a href="https://github.com/albertteoh">@albertteoh</a>)</li>
</ul>
<h3>UI Changes</h3>
<ul>
<li>UI pinned to version 1.11.0. The changelog is available here <a href="https://github.com/jaegertracing/jaeger-ui/blob/master/CHANGELOG.md#v1110-september-28-2020">v1.11.0</a></li>
</ul>

## Release 1.19.2
<p style="font-size:12px;"> 27, Aug 2020 
<a href="https://github.com/jaegertracing/jaeger/releases/tag/v1.19.2" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Upgrade to a working UI version before React refactoring.</p>

## Release 1.19.1
<p style="font-size:12px;"> 26, Aug 2020 
<a href="https://github.com/jaegertracing/jaeger/releases/tag/v1.19.1" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Revert UI back to 1.9 due to a bug <a class="issue-link js-issue-link" href="https://github.com/jaegertracing/jaeger-ui/issues/628">jaegertracing/jaeger-ui#628</a></p>

## Release 1.19.0
<p style="font-size:12px;"> 26, Aug 2020 
<a href="https://github.com/jaegertracing/jaeger/releases/tag/v1.19.0" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Known Issues</h3>
<p>The pull request <a href="https://github.com/jaegertracing/jaeger/pull/2297">#2297</a> aimed to add TLS support for the gRPC Query server but the flag registration is missing, so that this feature can't be used at the moment. A fix is planned for the next Jaeger version (1.20).</p>
<h3>Backend Changes</h3>
<h4>New Features</h4>
<ul>
<li>Reload TLS certificates on change (<a href="https://github.com/jaegertracing/jaeger/pull/2389">#2389</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add --kafka.producer.batch-min-messages collector flag (<a href="https://github.com/jaegertracing/jaeger/pull/2371">#2371</a>, <a href="https://github.com/prymitive">@prymitive</a>)</li>
<li>Make UDP socket buffer size configurable (<a href="https://github.com/jaegertracing/jaeger/pull/2336">#2336</a>, <a href="https://github.com/kbarukhov">@kbarukhov</a>)</li>
<li>Enable batch and queued retry processors by default (<a href="https://github.com/jaegertracing/jaeger/pull/2330">#2330</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add trace anonymizer prototype (<a href="https://github.com/jaegertracing/jaeger/pull/2328">#2328</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Add native OTEL ES exporter (<a href="https://github.com/jaegertracing/jaeger/pull/2295">#2295</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Define busy error type in processor (<a href="https://github.com/jaegertracing/jaeger/pull/2314">#2314</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Use gRPC instead of tchannel in hotrod (<a href="https://github.com/jaegertracing/jaeger/pull/2307">#2307</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>TLS support for gRPC Query server (<a href="https://github.com/jaegertracing/jaeger/pull/2297">#2297</a>, <a href="https://github.com/jan25">@jan25</a>)</li>
</ul>
<h4>Bug fixes, Minor Improvements</h4>
<ul>
<li>Check missing server URL in ES OTEL client (<a href="https://github.com/jaegertracing/jaeger/pull/2411">#2411</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Fix Elasticsearch version in ES OTEL writer (<a href="https://github.com/jaegertracing/jaeger/pull/2409">#2409</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Fix go vet warnings on Go 1.15 (<a href="https://github.com/jaegertracing/jaeger/pull/2401">#2401</a>, <a href="https://github.com/prymitive">@prymitive</a>)</li>
<li>Add new Elasticsearch reader implementation (<a href="https://github.com/jaegertracing/jaeger/pull/2364">#2364</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Only add the collector port if it was not explicitly set (<a href="https://github.com/jaegertracing/jaeger/pull/2396">#2396</a>, <a href="https://github.com/joe-elliott">@joe-elliott</a>)</li>
<li>Fix panic in collector when Zipkin server is shutdown  (<a href="https://github.com/jaegertracing/jaeger/pull/2392">#2392</a>, <a href="https://github.com/Sreevani871">@Sreevani871</a>)</li>
<li>Update validity of TLS certificates to 3650 days (<a href="https://github.com/jaegertracing/jaeger/pull/2390">#2390</a>, <a href="https://github.com/rjs211">@rjs211</a>)</li>
<li>Added span and trace id to hotrod logs (<a href="https://github.com/jaegertracing/jaeger/pull/2384">#2384</a>, <a href="https://github.com/joe-elliott">@joe-elliott</a>)</li>
<li>Jaeger agent logs "0" whenever sampling strategies are requested (<a href="https://github.com/jaegertracing/jaeger/pull/2382">#2382</a>, <a href="https://github.com/jpkrohling">@jpkrohling</a>)</li>
<li>Fix shutdown order for collector components (<a href="https://github.com/jaegertracing/jaeger/pull/2381">#2381</a>, <a href="https://github.com/Sreevani871">@Sreevani871</a>)</li>
<li>Serve jquery-3.1.1.min.js locally (<a href="https://github.com/jaegertracing/jaeger/pull/2378">#2378</a>, <a href="https://github.com/chaseSpace">@chaseSpace</a>)</li>
<li>Use a single shared set of CA, client &amp; server keys/certs for testing (<a href="https://github.com/jaegertracing/jaeger/pull/2343">#2343</a>, <a href="https://github.com/rjs211">@rjs211</a>)</li>
<li>fix null pointer in jaeger-spark-dependencies (<a href="https://github.com/jaegertracing/jaeger/pull/2327">#2327</a>, <a href="https://github.com/moolen">@moolen</a>)</li>
<li>Rename ARCH to TARGETARCH for multi platform build by docker buildx (<a href="https://github.com/jaegertracing/jaeger/pull/2320">#2320</a>, <a href="https://github.com/morlay">@morlay</a>)</li>
<li>Mask passwords when written as json (<a href="https://github.com/jaegertracing/jaeger/pull/2302">#2302</a>, <a href="https://github.com/objectiser">@objectiser</a>)</li>
</ul>
<h3>UI Changes</h3>
<ul>
<li>UI pinned to version 1.10.0. The changelog is available here <a href="https://github.com/jaegertracing/jaeger-ui/blob/master/CHANGELOG.md#v1100-august-25-2020">v1.10.0</a></li>
</ul>

## Release 1.18.1
<p style="font-size:12px;"> 19, Jun 2020 
<a href="https://github.com/jaegertracing/jaeger/releases/tag/v1.18.1" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Backend Changes</h3>
<h4>Security Fixes</h4>
<ul>
<li>CVE-2020-10750: jaegertracing/jaeger: credentials leaked to container logs (<a href="https://github.com/chlunde">@chlunde</a>)</li>
</ul>
<h4>New Features</h4>
<ul>
<li>Add ppc64le support (<a href="https://github.com/jaegertracing/jaeger/pull/2293">#2293</a>, <a href="https://github.com/Siddhesh-Ghadi">@Siddhesh-Ghadi</a>)</li>
<li>Expose option to enable TLS when sniffing an Elasticsearch Cluster (<a href="https://github.com/jaegertracing/jaeger/pull/2263">#2263</a>, <a href="https://github.com/jennynilsen">@jennynilsen</a>)</li>
<li>Enable OTEL receiver by default (<a href="https://github.com/jaegertracing/jaeger/pull/2279">#2279</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add Badger OTEL exporter (<a href="https://github.com/jaegertracing/jaeger/pull/2269">#2269</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add all-in-one OTEL component (<a href="https://github.com/jaegertracing/jaeger/pull/2262">#2262</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add arm64 support for binaries and docker images (<a href="https://github.com/jaegertracing/jaeger/pull/2176">#2176</a>, <a href="https://github.com/MrXinWang">@MrXinWang</a>)</li>
<li>Add Zipkin OTEL receiver (<a href="https://github.com/jaegertracing/jaeger/pull/2247">#2247</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
</ul>
<h4>Bug fixes, Minor Improvements</h4>
<ul>
<li>Remove experimental flag from rollover (<a href="https://github.com/jaegertracing/jaeger/pull/2290">#2290</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Move ES dependencies index mapping to JSON template file (<a href="https://github.com/jaegertracing/jaeger/pull/2285">#2285</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Bump go-plugin to 1.3 (<a href="https://github.com/jaegertracing/jaeger/pull/2261">#2261</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Ignore chmod events on UI config watcher. (<a href="https://github.com/jaegertracing/jaeger/pull/2254">#2254</a>, <a href="https://github.com/rubenvp8510">@rubenvp8510</a>)</li>
<li>Normalize CLI flags to use host:port addresses (<a href="https://github.com/jaegertracing/jaeger/pull/2212">#2212</a>, <a href="https://github.com/ohdearaugustin">@ohdearaugustin</a>)</li>
<li>Add kafka receiver flags to ingester (<a href="https://github.com/jaegertracing/jaeger/pull/2251">#2251</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Configure Jaeger receiver and exporter by flags (<a href="https://github.com/jaegertracing/jaeger/pull/2241">#2241</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
</ul>

## Relase 1.18.0
<p style="font-size:12px;"> 14, May 2020 
<a href="https://github.com/jaegertracing/jaeger/releases/tag/v1.18.0" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Backend Changes</h3>
<h4>Breaking Changes</h4>
<ul>
<li>
<p>Remove Tchannel between agent and collector (<a href="https://github.com/jaegertracing/jaeger/pull/2115">#2115</a>, <a href="https://github.com/jaegertracing/jaeger/pull/2112">#2112</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</p>
<p>Remove <code>Tchannel</code> port (14267) from collector and <code>Tchannel</code> reporter from agent.</p>
<p>These flags were removed from agent:</p>
<pre><code>--collector.host-port
--reporter.tchannel.discovery.conn-check-timeout
--reporter.tchannel.discovery.min-peers
--reporter.tchannel.host-port
--reporter.tchannel.report-timeout
</code></pre>
<p>These flags were removed from collector:</p>
<pre><code>--collector.port
</code></pre>
</li>
<li>
<p>Normalize CLI flags to use host:port addresses (<a href="https://github.com/jaegertracing/jaeger/pull/1827">#1827</a>, <a href="https://github.com/annanay25">@annanay25</a>)</p>
<p>Flags previously accepting listen addresses in any other format have been deprecated:</p>
<ul>
<li><code>collector.port</code> is superseded by <code>collector.tchan-server.host-port</code></li>
<li><code>collector.http-port</code> is superseded by <code>collector.http-server.host-port</code></li>
<li><code>collector.grpc-port</code> is superseded by <code>collector.grpc-server.host-port</code></li>
<li><code>collector.zipkin.http-port</code> is superseded by <code>collector.zipkin.host-port</code></li>
<li><code>admin-http-port</code> is superseded by <code>admin.http.host-port</code></li>
</ul>
</li>
</ul>
<h4>New Features</h4>
<ul>
<li>Add grpc storage plugin OTEL exporter (<a href="https://github.com/jaegertracing/jaeger/pull/2229">#2229</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add OTEL ingester component (<a href="https://github.com/jaegertracing/jaeger/pull/2225">#2225</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add Kafka OTEL receiver/ingester (<a href="https://github.com/jaegertracing/jaeger/pull/2221">#2221</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Create Jaeger OTEL agent component  (<a href="https://github.com/jaegertracing/jaeger/pull/2216">#2216</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Merge hardcoded/default configuration with OTEL config file (<a href="https://github.com/jaegertracing/jaeger/pull/2211">#2211</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Support periodic refresh of sampling strategies (<a href="https://github.com/jaegertracing/jaeger/pull/2188">#2188</a>, <a href="https://github.com/defool">@defool</a>)</li>
<li>Add Elasticsearch OTEL exporter (<a href="https://github.com/jaegertracing/jaeger/pull/2140">#2140</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add Cassandra OTEL exporter (<a href="https://github.com/jaegertracing/jaeger/pull/2139">#2139</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add Kafka OTEL storage exporter (<a href="https://github.com/jaegertracing/jaeger/pull/2135">#2135</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Clock skew config (<a href="https://github.com/jaegertracing/jaeger/pull/2119">#2119</a>, <a href="https://github.com/joe-elliott">@joe-elliott</a>)</li>
<li>Introduce OpenTelemetry collector (<a href="https://github.com/jaegertracing/jaeger/pull/2086">#2086</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Support regex tags search for Elasticseach backend (<a href="https://github.com/jaegertracing/jaeger/pull/2049">#2049</a>, <a href="https://github.com/annanay25">@annanay25</a>)</li>
</ul>
<h4>Bug fixes, Minor Improvements</h4>
<ul>
<li>Do not skip service/operation indexing for firehose spans (<a href="https://github.com/jaegertracing/jaeger/pull/2242">#2242</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Add build information to OTEL binaries (<a href="https://github.com/jaegertracing/jaeger/pull/2237">#2237</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Enable service default sampling param (<a href="https://github.com/jaegertracing/jaeger/pull/2230">#2230</a>, <a href="https://github.com/defool">@defool</a>)</li>
<li>Add Jaeger OTEL agent to docker image upload (<a href="https://github.com/jaegertracing/jaeger/pull/2227">#2227</a>, <a href="https://github.com/ning2008wisc">@ning2008wisc</a>)</li>
<li>Support adding process tags in OTEL via env variable (<a href="https://github.com/jaegertracing/jaeger/pull/2220">#2220</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Bump OTEL version and update exporters to use new API (<a href="https://github.com/jaegertracing/jaeger/pull/2196">#2196</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Support sampling startegies file flag in OTEL collector (<a href="https://github.com/jaegertracing/jaeger/pull/2195">#2195</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add zipkin receiver to OTEL collector (<a href="https://github.com/jaegertracing/jaeger/pull/2181">#2181</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Add Dockerfile for OTEL collector and publish latest tag (<a href="https://github.com/jaegertracing/jaeger/pull/2167">#2167</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Run OTEL collector without configuration file (<a href="https://github.com/jaegertracing/jaeger/pull/2148">#2148</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Update gocql to support AWS MCS (<a href="https://github.com/jaegertracing/jaeger/pull/2133">#2133</a>, <a href="https://github.com/johanneswuerbach">@johanneswuerbach</a>)</li>
<li>Return appropriate gRPC errors/codes to indicate request status (<a href="https://github.com/jaegertracing/jaeger/pull/2132">#2132</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Remove tchannel port from dockerfile and test (<a href="https://github.com/jaegertracing/jaeger/pull/2118">#2118</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Remove tchannel between agent and collector (<a href="https://github.com/jaegertracing/jaeger/pull/2115">#2115</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
<li>Move all tchannel packages to a single top level package (<a href="https://github.com/jaegertracing/jaeger/pull/2112">#2112</a>, <a href="https://github.com/pavolloffay">@pavolloffay</a>)</li>
</ul>
<h3>UI Changes</h3>
<ul>
<li>UI pinned to version 1.9.0. The changelog is available here <a href="https://github.com/jaegertracing/jaeger-ui/blob/master/CHANGELOG.md#v190-may-14-2020">v1.9.0</a></li>
</ul>

## Release 1.17.1
<p style="font-size:12px;"> 13, Mar 2020 
<a href="https://github.com/jaegertracing/jaeger/releases/tag/v1.17.1" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Backend Changes</h3>
<h4>Bug fixes, Minor Improvements</h4>
<ul>
<li>Fix enable Kafka TLS when TLS auth is specified <a href="https://github.com/jaegertracing/jaeger/pull/2107">#2107</a>, <a href="https://github.com/pavoloffay">@pavolloffay</a>)</li>
<li>Migrate project to go modules <a href="https://github.com/jaegertracing/jaeger/pull/2098">#2098</a>, <a href="https://github.com/pavoloffay">@pavolloffay</a>)</li>
<li>Do not skip service/operation indexing for firehose spans <a href="https://github.com/jaegertracing/jaeger/pull/2090">#2090</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Close the span writer on main (<a href="https://github.com/jaegertracing/jaeger/pull/2096">#2096</a>, <a href="https://github.com/jpkrohling">@jpkrohling</a>)</li>
<li>Improved graceful shutdown - Collector (<a href="https://github.com/jaegertracing/jaeger/pull/2076">#2076</a>, <a href="https://github.com/jpkrohling">@jpkrohling</a>)</li>
<li>Improved graceful shutdown - Agent (<a href="https://github.com/jaegertracing/jaeger/pull/2031">#2031</a>, <a href="https://github.com/jpkrohling">@jpkrohling</a>)</li>
</ul>
<h3>UI Changes</h3>
<ul>
<li>UI pinned to version 1.8.0. The changelog is available here <a href="https://github.com/jaegertracing/jaeger-ui/blob/master/CHANGELOG.md#v180-march-12-2020">v1.8.0</a></li>
</ul>

## Release 1.17.0
<p style="font-size:12px;"> 24, Feb 2020 
<a href="https://github.com/jaegertracing/jaeger/releases/tag/v1.17.0" target="_blank"> 
Source </a><OutboundLink /></p>
<h3>Backend Changes</h3>
<h4>New Features</h4>
<ul>
<li>[tracegen] Add service name as a command line option (<a href="https://github.com/jaegertracing/jaeger/pull/2080">#2080</a>, <a href="https://github.com/kevinearls">@kevinearls</a>)</li>
<li>Allow the Configuration of Additional Headers on the Jaeger Query HTTP API (<a href="https://github.com/jaegertracing/jaeger/pull/2056">#2056</a>, <a href="https://github.com/joe-elliott">@joe-elliott</a>)</li>
<li>Warn about time adjustment in tags (<a href="https://github.com/jaegertracing/jaeger/pull/2052">#2052</a>, <a href="https://github.com/bobrik">@bobrik</a>)</li>
<li>Add CLI flags for Kafka batching params (<a href="https://github.com/jaegertracing/jaeger/pull/2047">#2047</a>, <a href="https://github.com/apm-opentt">@apm-opentt</a>)</li>
<li>Added support for dynamic queue sizes (<a href="https://github.com/jaegertracing/jaeger/pull/1985">#1985</a>, <a href="https://github.com/jpkrohling">@jpkrohling</a>)</li>
<li>[agent] Process data loss stats from clients (<a href="https://github.com/jaegertracing/jaeger/pull/2010">#2010</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Add /api/sampling endpoint in collector (<a href="https://github.com/jaegertracing/jaeger/pull/1990">#1990</a>, <a href="https://github.com/RickyRajinder">@RickyRajinder</a>)</li>
<li>Add basic authentication to Kafka storage (<a href="https://github.com/jaegertracing/jaeger/pull/1983">#1983</a>, <a href="https://github.com/chandresh-pancholi">@chandresh-pancholi</a>)</li>
<li>Make operation_strategies part also be part of default_strategy  (<a href="https://github.com/jaegertracing/jaeger/pull/1749">#1749</a>, <a href="https://github.com/rutgerbrf">@rutgerbrf</a>)</li>
</ul>
<h4>Bug fixes, Minor Improvements</h4>
<ul>
<li>Upgrade gRPC to ^1.26 (<a href="https://github.com/jaegertracing/jaeger/pull/2077">#2077</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Remove pkg/errors from dependencies (<a href="https://github.com/jaegertracing/jaeger/pull/2073">#2073</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Update dependencies, pin grpc&lt;1.27 (<a href="https://github.com/jaegertracing/jaeger/pull/2072">#2072</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Refactor collector mains (<a href="https://github.com/jaegertracing/jaeger/pull/2060">#2060</a>, <a href="https://github.com/jpkrohling">@jpkrohling</a>)</li>
<li>Clarify that "kafka" is not a real storage backend (<a href="https://github.com/jaegertracing/jaeger/pull/2066">#2066</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Added -trimpath option to go build (<a href="https://github.com/jaegertracing/jaeger/pull/2064">#2064</a>, <a href="https://github.com/kadern0">@kadern0</a>)</li>
<li>Use memory size flag to activate dyn queue size feature (<a href="https://github.com/jaegertracing/jaeger/pull/2059">#2059</a>, <a href="https://github.com/jpkrohling">@jpkrohling</a>)</li>
<li>Add before you push to the queue to prevent race condition on size (<a href="https://github.com/jaegertracing/jaeger/pull/2044">#2044</a>, <a href="https://github.com/joe-elliott">@joe-elliott</a>)</li>
<li>Count received batches from conforming clients (<a href="https://github.com/jaegertracing/jaeger/pull/2030">#2030</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>[agent] Do not increment data loss counters on the first client batch (<a href="https://github.com/jaegertracing/jaeger/pull/2028">#2028</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Allow raw port numbers for UDP servers (<a href="https://github.com/jaegertracing/jaeger/pull/2025">#2025</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Publish tracegen (<a href="https://github.com/jaegertracing/jaeger/pull/2022">#2022</a>, <a href="https://github.com/jpkrohling">@jpkrohling</a>)</li>
<li>Build binaries for Linux on IBM Z / s390x architecture (<a href="https://github.com/jaegertracing/jaeger/pull/1982">#1982</a>, <a href="https://github.com/prankkelkar">@prankkelkar</a>)</li>
<li>Admin/Query: Log the real port instead of the provided one to enable the use of port 0 (<a href="https://github.com/jaegertracing/jaeger/pull/2002">#2002</a>, <a href="https://github.com/ChadiEM">@ChadiEM</a>)</li>
<li>Split agent's HTTP server and handler (<a href="https://github.com/jaegertracing/jaeger/pull/1996">#1996</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Clean-up collector handlers builder (<a href="https://github.com/jaegertracing/jaeger/pull/1991">#1991</a>, <a href="https://github.com/yurishkuro">@yurishkuro</a>)</li>
<li>Added 'resize' operation to BoundedQueue (<a href="https://github.com/jaegertracing/jaeger/pull/1949">#1948</a>, <a href="https://github.com/jpkrohling">@jpkrohling</a>)</li>
<li>Add common TLS configuration (<a href="https://github.com/jaegertracing/jaeger/pull/1838">#1838</a>, <a href="https://github.com/backjo">@backjo</a>)</li>
</ul>
<h3>UI Changes</h3>
<ul>
<li>UI pinned to version 1.7.0. The changelog is available here <a href="https://github.com/jaegertracing/jaeger-ui/blob/master/CHANGELOG.md#v170-february-21-2020">v1.7.0</a></li>
</ul>
