# TiKV

<div>
<demo-component app-code="tikv"/>
</div>


## tikv-server v4.0.13
<p style="font-size:12px;"> 27, May 2021 
<a href="https://github.com/tikv/tikv/releases/tag/v4.0.13" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Improvements</h2>
<ul>
<li>Make the calculation process of <code>store used size</code> more precise <a href="https://github.com/tikv/tikv/pull/9904">9904</a></li>
<li>Set more Regions in the <code>EpochNotMatch</code> message to reduce Region misses <a href="https://github.com/tikv/tikv/pull/9731">9731</a></li>
<li>Speed up freeing the memory accumulated in the long-running cluster <a href="https://github.com/tikv/tikv/pull/10035">10035</a></li>
</ul>
<h2>Bug Fixes</h2>
<ul>
<li>Fix a bug that TiKV cannot start if the <code>file_dict</code> file is not fully written into the disk that has been full <a href="https://github.com/tikv/tikv/pull/9963">9963</a></li>
<li>Limit TiCDC's scan speed at 128MB/s by default <a href="https://github.com/tikv/tikv/pull/9983">9983</a></li>
<li>Reduce the memory usage of TiCDC's initial scan <a href="https://github.com/tikv/tikv/pull/10133">10133</a></li>
<li>Support the back pressure for TiCDC's scan speed <a href="https://github.com/tikv/tikv/pull/10142">10142</a></li>
<li>Fix a potential OOM issue by avoiding unnecessary reads to get TiCDC old values <a href="https://github.com/tikv/tikv/pull/10031">10031</a></li>
<li>Fix a TiCDC OOM issue caused by reading old values <a href="https://github.com/tikv/tikv/pull/10197">10197</a></li>
<li>Add a timeout mechanism for S3 storages to avoid the client hanging without responses <a href="https://github.com/tikv/tikv/pull/10132">10132</a></li>
</ul>

## release v5.1.0-alpha
<p style="font-size:12px;"> 24, May 2021 
<a href="https://github.com/tikv/tikv/releases/tag/v5.1.0-alpha" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Release v5.1.0-alpha</p>

## v4.0.7-20210429: sst_importer: do not change block_cache_size in import mode (#6558) (…
<p style="font-size:12px;"> 29, Apr 2021 
<a href="https://github.com/tikv/tikv/releases/tag/v4.0.7-20210429" target="_blank"> 
Source </a><OutboundLink /></p>
<p>…<a class="issue-link js-issue-link" href="https://github.com/tikv/tikv/pull/9116">#9116</a>)</p>
<p>Signed-off-by: ti-srebot <a href="mailto:ti-srebot@pingcap.com">ti-srebot@pingcap.com</a><br />
Signed-off-by: kennytm <a href="mailto:kennytm@gmail.com">kennytm@gmail.com</a></p>

## tikv-server v5.0.1
<p style="font-size:12px;"> 23, Apr 2021 
<a href="https://github.com/tikv/tikv/releases/tag/v5.0.1" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Improvements</h2>
<ul>
<li>Use <code>zstd</code> to compress the Region snapshot <a href="https://github.com/tikv/tikv/pull/10005">#10005</a></li>
</ul>
<h2>Bug Fixes</h2>
<ul>
<li>Fix the issue that the coprocessor fails to properly handle the signed or unsigned integer types in the <code>IN</code> expression <a href="https://github.com/tikv/tikv/pull/10018">#10018</a></li>
<li>Fix the issue of many empty Regions after batch ingesting SST files <a href="https://github.com/tikv/tikv/pull/10015">#10015</a></li>
<li>Fix the potential panic that occurs when the input of <code>cast_string_as_time</code> is invalid UTF-8 bytes <a href="https://github.com/tikv/tikv/pull/9995">#9995</a></li>
<li>Fix a bug that TiKV cannot start up after the file dictionary file is damaged <a href="https://github.com/tikv/tikv/pull/9992">#9992</a></li>
</ul>

## tikv-server v5.0.0
<p style="font-size:12px;"> 07, Apr 2021 
<a href="https://github.com/tikv/tikv/releases/tag/v5.0.0" target="_blank"> 
Source </a><OutboundLink /></p>
<ul>
<li>Compatibility changes
<ul>
<li>Replace the <code>rocksdb.auto-tuned</code> configuration item with <a href="https://github.com/tikv/tikv/blob/v5.0.0/tikv-configuration-file.md#rate-limiter-auto-tuned-new-in-v50"><code>rocksdb.rate-limiter-auto-tuned</code></a></li>
<li>Delete the <code>raftstore.sync-log</code> configuration item. By default, written data is forcibly spilled to the disk. Before v5.0, you can explicitly disable <code>raftstore.sync-log</code>. Since v5.0, the configuration value is forcibly set to <code>true</code></li>
<li>Change the default value of the <code>gc.enable-compaction-filter</code> configuration item from <code>false</code> to <code>true</code></li>
<li>Change the default value of the <a href="https://github.com/tikv/tikv/blob/v5.0.0/tikv-configuration-file.md#rate-limiter-auto-tuned-new-in-v50"><code>rate-limiter-auto-tuned</code></a> configuration item from <code>false</code> to <code>true</code></li>
</ul>
</li>
<li>New features
<ul>
<li>Support log redaction to desensitize the output log information. The configuration item <code>security.redact-info-log</code>. Its default value is <code>false</code>, which means that desensitization is disabled. To enable desensitization for tikv-server logs, set the variable value to <code>true</code></li>
<li>Support transaction async commit</li>
<li>Support Raft joint consensus</li>
</ul>
</li>
<li>Improvements
<ul>
<li>Enable the system to automatically adjust the data compaction speed by default to balance the contention for I/O resources between background tasks and foreground reads and writes</li>
<li>Enable the GC Compaction Filter feature by default to reduce GC’s consumption of CPU and I/O resources</li>
<li>Optimize load base split strategy to solve the performance problem that data cannot be split in some small table hotspot read scenarios</li>
</ul>
</li>
</ul>

## tikv-server v4.0.12
<p style="font-size:12px;"> 02, Apr 2021 
<a href="https://github.com/tikv/tikv/releases/tag/v4.0.12" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Improvements</h2>
<ul>
<li>Prevent a large number of reconnections in a short period of time <a href="https://github.com/tikv/tikv/pull/9879">#9879</a></li>
<li>Optimize the write operations in the scenarios of many tombstones <a href="https://github.com/tikv/tikv/pull/9729">#9729</a></li>
<li>Change the default value of <code>leader-transfer-max-log-lag</code> to <code>128</code> to increase the success rate of leader transfer <a href="https://github.com/tikv/tikv/pull/9605">#9605</a></li>
</ul>
<h2>Bug Fixes</h2>
<ul>
<li>Fix the issue that the <code>IN</code> expression does not properly handle unsigned/signed integers <a href="https://github.com/tikv/tikv/pull/9850">#9850</a></li>
<li>Fix the issue that the ingest operation is not re-entrant <a href="https://github.com/tikv/tikv/pull/9779">#9779</a></li>
<li>Fix the issue that the space is missed when converting JSON to string in TiKV coprocessor <a href="https://github.com/tikv/tikv/pull/9666">#9666</a></li>
</ul>

## v5.0.0-nightly: txn_types: Check overflow in timestamp computation (#9777) (#9812)
<p style="font-size:12px;"> 15, Mar 2021 
<a href="https://github.com/tikv/tikv/releases/tag/v5.0.0-nightly" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Signed-off-by: ti-srebot <a href="mailto:ti-srebot@pingcap.com">ti-srebot@pingcap.com</a></p>
<p>Co-authored-by: Zijie Lu <a href="mailto:wslzj40@gmail.com">wslzj40@gmail.com</a></p>

## tikv-server v4.0.11
<p style="font-size:12px;"> 26, Feb 2021 
<a href="https://github.com/tikv/tikv/releases/tag/v4.0.11" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>New Features</h2>
<ul>
<li>Support the <code>utf8mb4_unicode_ci</code> collation <a href="https://github.com/tikv/tikv/pull/9577">#9577</a></li>
<li>Support the <code>cast_year_as_time</code> collation <a href="https://github.com/tikv/tikv/pull/9299">#9299</a></li>
</ul>
<h2>Improvements</h2>
<ul>
<li>Add metrics of server information for DBaaS <a href="https://github.com/tikv/tikv/pull/9591">#9591</a></li>
<li>Support multiple clusters in Grafana dashboards <a href="https://github.com/tikv/tikv/pull/9572">#9572</a></li>
<li>Report RocksDB metrics to TiDB <a href="https://github.com/tikv/tikv/pull/9316">#9316</a></li>
<li>Record the suspension time for Coprocessor tasks <a href="https://github.com/tikv/tikv/pull/9277">#9277</a></li>
<li>Add thresholds of key counts and key size for Load Base Split <a href="https://github.com/tikv/tikv/pull/9354">#9354</a></li>
<li>Check whether the file exists before data import <a href="https://github.com/tikv/tikv/pull/9544">#9544</a></li>
<li>Improve Fast Tune panels <a href="https://github.com/tikv/tikv/pull/9180">#9180</a></li>
</ul>
<h2>Bug Fixes</h2>
<ul>
<li>Fix the issue that TiKV is failed to build with <code>PROST=1</code> <a href="https://github.com/tikv/tikv/pull/9604">#9604</a></li>
<li>Fix the unmatched memory diagnostics <a href="https://github.com/tikv/tikv/pull/9589">#9589</a></li>
<li>Fix the issue that the end key of a partial RawKV-restore range is inclusive <a href="https://github.com/tikv/tikv/pull/9583">#9583</a></li>
<li>Fix the issue that TiKV might panic when loading the old value of a key of a rolled-back transaction during TiCDC's incremental scan <a href="https://github.com/tikv/tikv/pull/9569">#9569</a></li>
<li>Fix the configuration glitch of old values when changefeeds with different settings connect to one Region <a href="https://github.com/tikv/tikv/pull/9565">#9565</a></li>
<li>Fix a crash issue that occurs when running a TiKV cluster on a machine with a network interface that lacks the MAC address (introduced in v4.0.9) <a href="https://github.com/tikv/tikv/pull/9516">#9516</a></li>
<li>Fix the issue of TiKV OOM when backing up a huge Region <a href="https://github.com/tikv/tikv/pull/9448">#9448</a></li>
<li>Fix the issue that <code>region-split-check-diff</code> cannot be customized <a href="https://github.com/tikv/tikv/pull/9530">#9530</a></li>
<li>Fix the issue of TiKV panic when the system time goes back <a href="https://github.com/tikv/tikv/pull/9542">#9542</a></li>
</ul>

## tikv-server v4.0.10
<p style="font-size:12px;"> 15, Jan 2021 
<a href="https://github.com/tikv/tikv/releases/tag/v4.0.10" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Bug Fixes</h2>
<ul>
<li>Fix the wrong mapping between ready and peer <a href="https://github.com/tikv/tikv/pull/9409">#9409</a></li>
<li>Fix the issue that some logs are not redacted when <code>security.redact-info-log</code> is set to <code>true</code> <a href="https://github.com/tikv/tikv/pull/9314">#9314</a></li>
</ul>

## tikv-server v5.0.0-rc
<p style="font-size:12px;"> 12, Jan 2021 
<a href="https://github.com/tikv/tikv/releases/tag/v5.0.0-rc" target="_blank"> 
Source </a><OutboundLink /></p>
<ul>
<li>Security
<ul>
<li>Support desensitizing error messages and log files to avoid leaking sensitive information, such as ID information and credit card number. Users can enable the desensitization feature by setting the <code>security.redact-info-log = true</code> in the configuration.</li>
</ul>
</li>
<li>Transaction
<ul>
<li>Support async commit feature to significantly reduce the latency of transactions. Previously without the async commit feature, the statements being written were only returned to the client after the two-phase transaction commit finished. Now the async commit feature supports returning the result to the client after the first phase of the two-phase commit finishes. The second phase is then performed asynchronously in the background, thus reducing the latency of transaction commit. Note that this feature is only used with tidb-server.</li>
</ul>
</li>
<li>Engine
<ul>
<li>Introduce IO rate limiter and support dynamically changing auto-tuned mode of rate limiter. The system automatically adjusts the compaction rate to balance the contention for I/O resources between background tasks and foreground data reads and writes. After enabling this feature via the <code>rate-limiter-auto-tuned</code> configuration item, the delay jitter is greatly reduced than that when this feature is disabled.</li>
<li>Support GC Compaction Filter feature. When TiKV performs garbage collection (GC) and data compaction, partitions occupy CPU and I/O resources. Overlapping data exists during the execution of these two tasks. To reduce I/O usage, the GC Compaction Filter feature combines these two tasks into one and executes them in the same task. This feature is still experimental and you can enable it via <code>gc.enable-compaction-filter = ture</code>.</li>
<li>Enable compaction guard by default, to split rocksdb SST files at TiKV region boundaries, to reduce overall compaction IO.</li>
</ul>
</li>
<li>RaftStore
<ul>
<li>Support using joint consensus improving the availability during region membership change. "adding a member” and "deleting a member” operations during the membership change are combined into one operation and sent to all members. During the change process, Regions are in an intermediate state. If any modified member fails, the system is still available. Users can enable this feature by modifying the membership variable by executing <code>pd-ctl config set enable-joint-consensus true</code>.</li>
</ul>
</li>
</ul>
