# Prometheus

<div>
<demo-component app-code="prometheus"/>
</div>


## 2.27.1 / 2021-05-18
<p style="font-size:12px;"> 18, May 2021 
<a href="https://github.com/prometheus/prometheus/releases/tag/v2.27.1" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release contains a bug fix for a security issue in the API endpoint. An<br />
attacker can craft a special URL that redirects a user to any endpoint via an<br />
HTTP 302 response. See the <a href="https://github.com/prometheus/prometheus/security/advisories/GHSA-vx57-7f4q-fpc7">security advisory</a> for more details.</p>
<p>This vulnerability has been reported by Aaron Devaney from MDSec.</p>
<ul>
<li>[BUGFIX] SECURITY: Fix arbitrary redirects under the /new endpoint (CVE-2021-29622)</li>
</ul>

## 2.26.1 / 2021-05-18
<p style="font-size:12px;"> 18, May 2021 
<a href="https://github.com/prometheus/prometheus/releases/tag/v2.26.1" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release contains a bug fix for a security issue in the API endpoint. An<br />
attacker can craft a special URL that redirects a user to any endpoint via an<br />
HTTP 302 response. See the <a href="https://github.com/prometheus/prometheus/security/advisories/GHSA-vx57-7f4q-fpc7">security advisory</a> for more details.</p>
<p>This vulnerability has been reported by Aaron Devaney from MDSec.</p>
<ul>
<li>[BUGFIX] SECURITY: Fix arbitrary redirects under the /new endpoint (CVE-2021-29622)</li>
</ul>

## 2.27.0 / 2021-05-12
<p style="font-size:12px;"> 12, May 2021 
<a href="https://github.com/prometheus/prometheus/releases/tag/v2.27.0" target="_blank"> 
Source </a><OutboundLink /></p>
<ul>
<li>[FEATURE] Promtool: Retroactive rule evaluation functionality. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/7675">#7675</a></li>
<li>[FEATURE] Configuration: Environment variable expansion for external labels. Behind <code>--enable-feature=expand-external-labels</code> flag. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8649">#8649</a></li>
<li>[FEATURE] TSDB: Add a flag(<code>--storage.tsdb.max-block-chunk-segment-size</code>) to control the max chunks file size of the blocks for small Prometheus instances. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8478">#8478</a></li>
<li>[FEATURE] UI: Add a dark theme. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8604">#8604</a></li>
<li>[FEATURE] AWS Lightsail Discovery: Add AWS Lightsail Discovery. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8693">#8693</a></li>
<li>[FEATURE] Docker Discovery: Add Docker Service Discovery. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8629">#8629</a></li>
<li>[FEATURE] OAuth: Allow OAuth 2.0 to be used anywhere an HTTP client is used. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8761">#8761</a></li>
<li>[FEATURE] Remote Write: Send exemplars via remote write. Experimental and disabled by default. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8296">#8296</a></li>
<li>[ENHANCEMENT] Digital Ocean Discovery: Add <code>__meta_digitalocean_vpc</code> label. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8642">#8642</a></li>
<li>[ENHANCEMENT] Scaleway Discovery: Read Scaleway secret from a file. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8643">#8643</a></li>
<li>[ENHANCEMENT] Scrape: Add configurable limits for label size and count. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8777">#8777</a></li>
<li>[ENHANCEMENT] UI: Add 16w and 26w time range steps. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8656">#8656</a></li>
<li>[ENHANCEMENT] Templating: Enable parsing strings in <code>humanize</code> functions. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8682">#8682</a></li>
<li>[BUGFIX] UI: Provide errors instead of blank page on TSDB Status Page. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8654">#8654</a> <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8659">#8659</a></li>
<li>[BUGFIX] TSDB: Do not panic when writing very large records to the WAL. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8790">#8790</a></li>
<li>[BUGFIX] TSDB: Avoid panic when mmaped memory is referenced after the file is closed. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8723">#8723</a></li>
<li>[BUGFIX] Scaleway Discovery: Fix nil pointer dereference. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8737">#8737</a></li>
<li>[BUGFIX] Consul Discovery: Restart no longer required after config update with no targets. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8766">#8766</a></li>
</ul>

## 2.27.0-rc.0 / 2021-05-09
<p style="font-size:12px;"> 09, May 2021 
<a href="https://github.com/prometheus/prometheus/releases/tag/v2.27.0-rc.0" target="_blank"> 
Source </a><OutboundLink /></p>
<ul>
<li>[FEATURE] Promtool: Retroactive rule evaluation functionality. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/7675">#7675</a></li>
<li>[FEATURE] Configuration: Environment variable expansion for external labels. Behind <code>--enable-feature=expand-external-labels</code> flag. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8649">#8649</a></li>
<li>[FEATURE] TSDB: Add a flag(<code>-storage.tsdb.max-chunk-size</code>) to control chunk allocation size for small Prometheus instances. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8478">#8478</a></li>
<li>[FEATURE] UI: Add a dark theme. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8604">#8604</a></li>
<li>[FEATURE] AWS Lightsail Discovery: Add AWS Lightsail Discovery. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8693">#8693</a></li>
<li>[FEATURE] Docker Discovery: Add Docker Service Discovery. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8629">#8629</a></li>
<li>[FEATURE] OAuth: Allow OAuth 2.0 to be used anywhere an HTTP client is used. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8761">#8761</a></li>
<li>[FEATURE] Remote Write: Send exemplars via remote write. Experimental and disabled by default. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8296">#8296</a></li>
<li>[ENHANCEMENT] Digital Ocean Discovery: Add <code>__meta_digitalocean_vpc</code> label. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8642">#8642</a></li>
<li>[ENHANCEMENT] Scaleway Discovery: Read Scaleway secret from a file. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8643">#8643</a></li>
<li>[ENHANCEMENT] Scrape: Add configurable limits for label size and count. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8777">#8777</a></li>
<li>[ENHANCEMENT] UI: Add 16w and 26w time range steps. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8656">#8656</a></li>
<li>[ENHANCEMENT] Templating: Enable parsing strings in <code>humanize</code> functions. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8682">#8682</a></li>
<li>[BUGFIX] UI: Provide errors instead of blank page on TSDB Status Page. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8654">#8654</a> <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8659">#8659</a></li>
<li>[BUGFIX] TSDB: Do not panic when writing very large records to the WAL. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8790">#8790</a></li>
<li>[BUGFIX] TSDB: Avoid panic when mmaped memory is referenced after the file is closed. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8723">#8723</a></li>
<li>[BUGFIX] Scaleway Discovery: Fix nil pointer dereference. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8737">#8737</a></li>
<li>[BUGFIX] Consul Discovery: Restart no longer required after config update with no targets. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8766">#8766</a></li>
</ul>

## 2.26.0 / 2021-03-31
<p style="font-size:12px;"> 31, Mar 2021 
<a href="https://github.com/prometheus/prometheus/releases/tag/v2.26.0" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Prometheus is now built and supporting Go 1.16 (<a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8544">#8544</a>). This reverts the memory release pattern added in Go 1.12. This makes common RSS usage metrics showing more accurate number for actual memory used by Prometheus. You can read more details <a href="https://www.bwplotka.dev/2019/golang-memory-monitoring/" rel="nofollow">here</a>.</p>
<p>Note that from this release Prometheus is using Alertmanager v2 by default.</p>
<ul>
<li>[CHANGE] Alerting: Using Alertmanager v2 API by default. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8626">#8626</a></li>
<li>[CHANGE] Prometheus/Promtool: As agreed on dev summit, binaries are now printing help and usage to stdout instead of stderr. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8542">#8542</a></li>
<li>[FEATURE] Remote: Add support for AWS SigV4 auth method for remote_write. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8509">#8509</a></li>
<li>[FEATURE] Scaleway Discovery: Add Scaleway Service Discovery. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8555">#8555</a></li>
<li>[FEATURE] PromQL: Allow negative offsets. Behind <code>--enable-feature=promql-negative-offset</code> flag. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8487">#8487</a></li>
<li>[FEATURE] <strong>experimental</strong> Exemplars: Add in-memory storage for exemplars. Behind <code>--enable-feature=exemplar-storage</code> flag. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/6635">#6635</a></li>
<li>[FEATURE] UI: Add advanced auto-completion, syntax highlighting and linting to graph page query input. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8634">#8634</a></li>
<li>[ENHANCEMENT] Digital Ocean Discovery: Add <code>__meta_digitalocean_image</code> label. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8497">#8497</a></li>
<li>[ENHANCEMENT] PromQL: Add <code>last_over_time</code>, <code>sgn</code>, <code>clamp</code> functions. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8457">#8457</a></li>
<li>[ENHANCEMENT] Scrape: Add support for specifying type of Authorization header credentials with Bearer by default. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8512">#8512</a></li>
<li>[ENHANCEMENT] Scrape: Add <code>follow_redirects</code> option to scrape configuration. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8546">#8546</a></li>
<li>[ENHANCEMENT] Remote: Allow retries on HTTP 429 response code for remote_write. Disabled by default. See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write" rel="nofollow">configuration docs</a> for details. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8237">#8237</a> <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8477">#8477</a></li>
<li>[ENHANCEMENT] Remote: Allow configuring custom headers for remote_read. See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_read" rel="nofollow">configuration docs</a> for details. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8516">#8516</a></li>
<li>[ENHANCEMENT] UI: Hitting Enter now triggers new query. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8581">#8581</a></li>
<li>[ENHANCEMENT] UI: Better handling of long rule and names on the <code>/rules</code> and <code>/targets</code> pages. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8608">#8608</a> <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8609">#8609</a></li>
<li>[ENHANCEMENT] UI: Add collapse/expand all button on the <code>/targets</code> page. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8486">#8486</a></li>
<li>[BUGFIX] TSDB: Eager deletion of removable blocks on every compaction, saving disk peak space usage. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8007">#8007</a></li>
<li>[BUGFIX] PromQL: Fix parser support for special characters like<code>炬</code>. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8517">#8517</a></li>
<li>[BUGFIX] Rules: Update rule health for append/commit fails. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8619">#8619</a></li>
</ul>

## v2.26.0-rc.0
<p style="font-size:12px;"> 26, Mar 2021 
<a href="https://github.com/prometheus/prometheus/releases/tag/v2.26.0-rc.0" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Prometheus is now built with and supporting Go 1.16 (<a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8544">#8544</a>). This reverts the memory release pattern added in Go 1.12. This makes common RSS usage metrics showing more accurate number for actual memory used by Prometheus. You can read more details <a href="https://www.bwplotka.dev/2019/golang-memory-monitoring/" rel="nofollow">here</a>.</p>
<p>Note that from this release Prometheus is using Alertmanager v2 by default.</p>
<ul>
<li>[CHANGE] Alerting: Using Alertmanager v2 API by default. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8626">#8626</a></li>
<li>[CHANGE] Prometheus/Promtool: As agreed on dev summit, binaries are now printing help and usage to stdout instead of stderr. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8542">#8542</a></li>
<li>[FEATURE] Remote: Add support for AWS SigV4 auth method for remote_write. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8509">#8509</a></li>
<li>[FEATURE] Scaleway Discovery: Add Scaleway Service Discovery. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8555">#8555</a></li>
<li>[FEATURE] PromQL: Allow negative offsets. Behind <code>--enable-feature=promql-negative-offset</code> flag. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8487">#8487</a></li>
<li>[FEATURE] <strong>experimental</strong> Exemplars: Add in-memory storage for exemplars. Behind <code>--enable-feature=exemplar-storage</code> flag. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/6635">#6635</a></li>
<li>[FEATURE] UI: Add advanced auto-completion, syntax highlighting and linting to graph page query input. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8634">#8634</a></li>
<li>[ENHANCEMENT] Digital Ocean Discovery: Add <code>__meta_digitalocean_image</code> label. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8497">#8497</a></li>
<li>[ENHANCEMENT] PromQL: Add <code>last_over_time</code>, <code>sgn</code>, <code>clamp</code> functions. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8457">#8457</a></li>
<li>[ENHANCEMENT] Scrape: Add support for specifying type of Authorization header credentials with Bearer by default. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8512">#8512</a></li>
<li>[ENHANCEMENT] Scrape: Add <code>follow_redirects</code> option to scrape configuration. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8546">#8546</a></li>
<li>[ENHANCEMENT] Remote: Allow retries on HTTP 429 response code for remote_write. Disabled by default. See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write" rel="nofollow">configuration docs</a> for details. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8237">#8237</a> <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8477">#8477</a></li>
<li>[ENHANCEMENT] Remote: Allow configuring custom headers for remote_read. See <a href="https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_read" rel="nofollow">configuration docs</a> for details. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8516">#8516</a></li>
<li>[ENHANCEMENT] UI: Hitting Enter now triggers new query. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8581">#8581</a></li>
<li>[ENHANCEMENT] UI: Better handling of long rule and names on the <code>/rules</code> and <code>/targets</code> pages. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8608">#8608</a> <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8609">#8609</a></li>
<li>[ENHANCEMENT] UI: Add collapse/expand all button on the <code>/targets</code> page. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8486">#8486</a></li>
<li>[BUGFIX] TSDB: Eager deletion of removable blocks on every compaction, saving disk peak space usage. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8007">#8007</a></li>
<li>[BUGFIX] PromQL: Fix parser support for special characters like<code>炬</code>. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8517">#8517</a></li>
<li>[BUGFIX] Rules: Update rule health for append/commit fails. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8619">#8619</a></li>
</ul>

## 2.25.2 / 2021-03-16
<p style="font-size:12px;"> 16, Mar 2021 
<a href="https://github.com/prometheus/prometheus/releases/tag/v2.25.2" target="_blank"> 
Source </a><OutboundLink /></p>
<ul>
<li>[BUGFIX] Fix the ingestion of scrapes when the wall clock changes, e.g. on suspend. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8601">#8601</a></li>
</ul>

## 2.25.1 / 2021-03-14
<p style="font-size:12px;"> 14, Mar 2021 
<a href="https://github.com/prometheus/prometheus/releases/tag/v2.25.1" target="_blank"> 
Source </a><OutboundLink /></p>
<ul>
<li>[BUGFIX] Fix a crash in <code>promtool</code> when a subquery with default resolution is used. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8569">#8569</a></li>
<li>[BUGFIX] Fix a bug that could return duplicate datapoints in queries. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8591">#8591</a></li>
<li>[BUGFIX] Fix crashes with arm64 when compiled with go1.16. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8593">#8593</a></li>
</ul>

## 2.25.0 / 2021-02-17
<p style="font-size:12px;"> 17, Feb 2021 
<a href="https://github.com/prometheus/prometheus/releases/tag/v2.25.0" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release includes a new <code>--enable-feature=</code> flag that enables<br />
experimental features. Such features might be changed or removed in the future.</p>
<p>In the next minor release (2.26), Prometheus will use the Alertmanager API v2.<br />
It will be done by defaulting <code>alertmanager_config.api_version</code> to <code>v2</code>.<br />
Alertmanager API v2 was released in Alertmanager v0.16.0 (released in January<br />
2019).</p>
<ul>
<li>[FEATURE] <strong>experimental</strong> API: Accept remote_write requests. Behind the --enable-feature=remote-write-receiver flag. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8424">#8424</a></li>
<li>[FEATURE] <strong>experimental</strong> PromQL: Add '@ ' modifier. Behind the --enable-feature=promql-at-modifier flag. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8121">#8121</a> <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8436">#8436</a> <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8425">#8425</a></li>
<li>[ENHANCEMENT] Add optional name property to testgroup for better test failure output. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8440">#8440</a></li>
<li>[ENHANCEMENT] Add warnings into React Panel on the Graph page. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8427">#8427</a></li>
<li>[ENHANCEMENT] TSDB: Increase the number of buckets for the compaction duration metric. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8342">#8342</a></li>
<li>[ENHANCEMENT] Remote: Allow passing along custom remote_write HTTP headers. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8416">#8416</a></li>
<li>[ENHANCEMENT] Mixins: Scope grafana configuration. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8332">#8332</a></li>
<li>[ENHANCEMENT] Kubernetes SD: Add endpoint labels metadata. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8273">#8273</a></li>
<li>[ENHANCEMENT] UI: Expose total number of label pairs in head in TSDB stats page. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8343">#8343</a></li>
<li>[ENHANCEMENT] TSDB: Reload blocks every minute, to detect new blocks and enforce retention more often. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8343">#8343</a></li>
<li>[BUGFIX] API: Fix global URL when external address has no port. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8359">#8359</a></li>
<li>[BUGFIX] Backfill: Fix error message handling. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8432">#8432</a></li>
<li>[BUGFIX] Backfill: Fix "add sample: out of bounds" error when series span an entire block. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/issues/8476">#8476</a></li>
<li>[BUGFIX] Deprecate unused flag --alertmanager.timeout. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8407">#8407</a></li>
<li>[BUGFIX] Mixins: Support remote-write metrics renamed in v2.23 in alerts. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8423">#8423</a></li>
<li>[BUGFIX] Remote: Fix garbage collection of dropped series in remote write. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8387">#8387</a></li>
<li>[BUGFIX] Remote: Log recoverable remote write errors as warnings. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8412">#8412</a></li>
<li>[BUGFIX] TSDB: Remove pre-2.21 temporary blocks on start. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8353">#8353</a>.</li>
<li>[BUGFIX] UI: Fix duplicated keys on /targets page. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8456">#8456</a></li>
<li>[BUGFIX] UI: Fix label name leak into class name. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8459">#8459</a></li>
</ul>

## 2.25.0-rc.0 / 2021-02-12
<p style="font-size:12px;"> 12, Feb 2021 
<a href="https://github.com/prometheus/prometheus/releases/tag/v2.25.0-rc.0" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release includes a new <code>--enable-feature=</code> flag that enables<br />
experimental features. Such features might be changed or removed in the future.</p>
<ul>
<li>[FEATURE] <strong>experimental</strong> API: Accept remote_write requests. Behind the --enable-feature=remote-write-receiver flag. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8424">#8424</a></li>
<li>[FEATURE] <strong>experimental</strong> PromQL: Add '@ ' modifier. Behind the --enable-feature=promql-at-modifier flag. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8121">#8121</a> <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8436">#8436</a> <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8425">#8425</a></li>
<li>[ENHANCEMENT] Add optional name property to testgroup for better test failure output. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8440">#8440</a></li>
<li>[ENHANCEMENT] Add warnings into React Panel on the Graph page. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8427">#8427</a></li>
<li>[ENHANCEMENT] TSDB: Increase the number of buckets for the compaction duration metric. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8342">#8342</a></li>
<li>[ENHANCEMENT] Remote: Allow passing along custom remote_write HTTP headers. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8416">#8416</a></li>
<li>[ENHANCEMENT] Mixins: Scope grafana configuration. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8332">#8332</a></li>
<li>[ENHANCEMENT] Kubernetes SD: Add endpoint labels metadata. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8273">#8273</a></li>
<li>[ENHANCEMENT] UI: Expose total number of label pairs in head in TSDB stats page. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8343">#8343</a></li>
<li>[ENHANCEMENT] TSDB: Reload blocks every minute, to detect new blocks and enforce retention more often. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8343">#8343</a></li>
<li>[BUGFIX] API: Fix global URL when external address has no port. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8359">#8359</a></li>
<li>[BUGFIX] Backfill: Fix error message handling. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8432">#8432</a></li>
<li>[BUGFIX] Deprecate unused flag --alertmanager.timeout. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8407">#8407</a></li>
<li>[BUGFIX] Mixins: Support remote-write metrics renamed in v2.23 in alerts. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8423">#8423</a></li>
<li>[BUGFIX] Remote: Fix garbage collection of dropped series in remote write. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8387">#8387</a></li>
<li>[BUGFIX] Remote: Log recoverable remote write errors as warnings. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8412">#8412</a></li>
<li>[BUGFIX] TSDB: Remove pre-2.21 temporary blocks on start. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8353">#8353</a>.</li>
<li>[BUGFIX] UI: Fix duplicated keys on /targets page. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8456">#8456</a></li>
<li>[BUGFIX] UI: Fix label name leak into class name. <a class="issue-link js-issue-link" href="https://github.com/prometheus/prometheus/pull/8459">#8459</a></li>
</ul>
