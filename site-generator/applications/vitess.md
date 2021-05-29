# Vitess

<div>
<demo-component app-code="vitess"/>
</div>


## Vitess 10.0.2
<p style="font-size:12px;"> 27, May 2021 
<a href="https://github.com/vitessio/vitess/releases/tag/v10.0.2" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Bug fixes</h2>
<h3>Query Serving</h3>
<ul>
<li>Fixes encoding of sql strings <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8029">#8029</a></li>
<li>Fix for issue with information_schema queries with both table name and schema name predicates <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8099">#8099</a></li>
<li>PRIMARY in index hint list for release 10.0 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8159">#8159</a></li>
</ul>
<h3>VReplication</h3>
<ul>
<li>VReplication: Pad binlog values for binary() columns to match the value returned by mysql selects <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8137">#8137</a></li>
</ul>
<h2>CI/Build</h2>
<h3>Build/CI</h3>
<ul>
<li>update release notes with known issue <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8081">#8081</a></li>
</ul>
<h2>Documentation</h2>
<h3>Other</h3>
<ul>
<li>Post v10.0.1 updates <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8045">#8045</a></li>
</ul>
<h2>Enhancement</h2>
<h3>Build/CI</h3>
<ul>
<li>Added release script to the makefile <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8030">#8030</a></li>
</ul>
<h3>Other</h3>
<ul>
<li>Add optional TLS feature to gRPC servers <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8176">#8176</a></li>
</ul>
<h2>Other</h2>
<h3>Build/CI</h3>
<ul>
<li>Release 10.0.1 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8031">#8031</a></li>
</ul>
<p>The release includes 14 commits (excluding merges)<br />
Thanks to all our contributors: <a class="user-mention" href="https://github.com/GuptaManan100">@GuptaManan100</a>, <a class="user-mention" href="https://github.com/askdba">@askdba</a>, <a class="user-mention" href="https://github.com/deepthi">@deepthi</a>, <a class="user-mention" href="https://github.com/harshit-gangal">@harshit-gangal</a>, <a class="user-mention" href="https://github.com/noxiouz">@noxiouz</a>, <a class="user-mention" href="https://github.com/rohit-nayak-ps">@rohit-nayak-ps</a>, <a class="user-mention" href="https://github.com/systay">@systay</a></p>

## Vitess 9.0.2
<p style="font-size:12px;"> 25, May 2021 
<a href="https://github.com/vitessio/vitess/releases/tag/v9.0.2" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Bug fixes</h2>
<h3>Cluster management</h3>
<ul>
<li>Restore: Check disable_active_reparents properly before waiting for position update <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8114">#8114</a></li>
</ul>
<h3>Query Serving</h3>
<ul>
<li>Fix information_schema query with system schema in table_schema filter <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8095">#8095</a></li>
<li>Fix for issue with information_schema queries with both table name and schema name predicates <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8096">#8096</a></li>
<li>Fix for transactions not allowed to finish during PlannedReparentShard <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8098">#8098</a></li>
<li>PRIMARY in index hint list <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8158">#8158</a></li>
</ul>
<h2>CI/Build</h2>
<h3>Build/CI</h3>
<ul>
<li>Release 9.0.1 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8065">#8065</a></li>
<li>9.0.0: update release notes with known issue <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/issues/8080">#8080</a> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8082">#8082</a></li>
<li>Added release script to the makefile <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8182">#8182</a></li>
<li>Update do_release to work in the 9.0 branch <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8184">#8184</a></li>
</ul>
<h2>Performance</h2>
<h3>Cluster management</h3>
<ul>
<li>Revert "backup: Use pargzip instead of pgzip for compression." <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8174">#8174</a></li>
</ul>
<p>The release includes 17 commits (excluding merges)<br />
Thanks to all our contributors: <a class="user-mention" href="https://github.com/GuptaManan100">@GuptaManan100</a>, <a class="user-mention" href="https://github.com/deepthi">@deepthi</a>, <a class="user-mention" href="https://github.com/HARSHIT">@HARSHIT</a>, <a class="user-mention" href="https://github.com/rafael">@rafael</a>, <a class="user-mention" href="https://github.com/systay">@systay</a></p>

## Vitess 9.0.1
<p style="font-size:12px;"> 06, May 2021 
<a href="https://github.com/vitessio/vitess/releases/tag/v9.0.1" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release complies with VEP-3 which removes the upgrade order requirement. Components can be upgraded in any order. It is recommended that the upgrade order should still be followed if possible, except to canary test the new version of VTGate before upgrading the rest of the components.</p>
<h2>Bug fixes</h2>
<h3>Cluster management</h3>
<ul>
<li>Backport: Respect -disable_active_reparents in backup/restore <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8063">#8063</a></li>
</ul>
<h3>Other</h3>
<ul>
<li>[9.0] fix regression - should be able to plan subquery on top of subquery <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7683">#7683</a></li>
</ul>
<h3>Query Serving</h3>
<ul>
<li>[9.0] Fix for reserved connection usage with transaction <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7666">#7666</a></li>
<li>[9.0] Fix MySQL Workbench failure on login with <code>select current_user()</code> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7706">#7706</a></li>
<li>[9.0] make sure to handle subqueries on top of subqueries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7776">#7776</a></li>
<li>[9.0] make sure to not log sensitive information <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7778">#7778</a></li>
<li>[9.0] ddl bypass planner <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8035">#8035</a></li>
<li>[9.0] Memory Sort to close the goroutines when callback returns error <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8040">#8040</a></li>
<li>[9.0] Fix bug with reserved connections to stale tablets <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8041">#8041</a></li>
<li>[9.0] Fix for Query Serving when Toposerver is Down <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8046">#8046</a></li>
<li>ignore the error and log as warn if not able to validate the current system settings value <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8062">#8062</a></li>
</ul>
<h3>VReplication</h3>
<ul>
<li>VReplication: fix vreplication timing metrics <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8060">#8060</a></li>
<li>VReplication: Pad binlog values for binary() columns to match the value returned by mysql selects <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8061">#8061</a></li>
</ul>
<h2>Documentation</h2>
<h3>Other</h3>
<ul>
<li>9.0.0 Release Notes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7384">#7384</a></li>
</ul>
<h2>Other</h2>
<h3>Build/CI</h3>
<ul>
<li>Fix Dockerfiles for vtexplain and vtctlclient <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7418">#7418</a></li>
</ul>
<h3>Query Serving</h3>
<ul>
<li>Fix table parsing on VSchema generation <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7511">#7511</a></li>
<li>[9.0] Show anywhere plan fix to consider default keyspace <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7530">#7530</a></li>
<li>[9.0] Reset Session for Reserved Connection when the connection id is not found <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7544">#7544</a></li>
<li>Healthcheck: update healthy tablets correctly when a stream returns an error or times out <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7732">#7732</a></li>
</ul>
<h3>VReplication</h3>
<ul>
<li>MoveTables: Refresh SrvVSchema and source tablets on completion <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/8059">#8059</a></li>
</ul>
<p>The release includes 43 commits (excluding merges)<br />
Thanks to all our contributors: <a class="user-mention" href="https://github.com/askdba">@askdba</a>, <a class="user-mention" href="https://github.com/deepthi">@deepthi</a>, <a class="user-mention" href="https://github.com/dyv">@dyv</a>, <a class="user-mention" href="https://github.com/harshit-gangal">@harshit-gangal</a>, <a class="user-mention" href="https://github.com/rafael">@rafael</a>, <a class="user-mention" href="https://github.com/rohit-nayak-ps">@rohit-nayak-ps</a>, <a class="user-mention" href="https://github.com/shlomi-noach">@shlomi-noach</a>, <a class="user-mention" href="https://github.com/systay">@systay</a></p>

## Vitess 10.0.1 Release
<p style="font-size:12px;"> 04, May 2021 
<a href="https://github.com/vitessio/vitess/releases/tag/v10.0.1" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>Bugs Fixed</h2>
<ul>
<li>Running binaries with <code>--version</code> or running <code>select @@version</code> from a MySQL client still shows <code>10.0.0-RC1</code></li>
</ul>

## Vitess 10.0.0
<p style="font-size:12px;"> 07, May 2021 
<a href="https://github.com/vitessio/vitess/releases/tag/v10.0.0" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release complies with VEP-3 which removes the upgrade order requirement. Components can be upgraded in any order. It is recommended that the upgrade order should still be followed if possible, except to canary test the new version of VTGate before upgrading the rest of the components.</p>
<h2>Known Issues</h2>
<ul>
<li>Running binaries with <code>--version</code> or running <code>select @@version</code> from a MySQL client still shows <code>10.0.0-RC1</code></li>
<li>Online DDL <a href="https://github.com/vitessio/vitess/pull/7873#issuecomment-822798180">cannot be used</a> if you are using the keyspace filtering feature of VTGate</li>
<li>VReplication errors when a fixed-length binary column is used as the sharding key <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/issues/8080">#8080</a></li>
</ul>
<h2>Bugs Fixed</h2>
<h3>VTGate / MySQL compatibility</h3>
<ul>
<li>Remove printing of ENFORCED word so that statements remain compatible with mysql 5.7 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7458">#7458</a></li>
<li>Allow any ordering of generic options in column definitions <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7459">#7459</a></li>
<li>Corrects the comment handling in vitess <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7581">#7581</a></li>
<li>Fix regression - should be able to plan subquery on top of subquery <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7682">#7682</a></li>
<li>Nullable Timestamp Column Fix <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7740">#7740</a></li>
<li>VTGate: Fix the error messages in drop, create and alter database commands <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7397">#7397</a></li>
<li>VTGate: Fix information_schema query with system schema in table_schema filter <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7430">#7430</a></li>
<li>VTGate: Fix Set Statement in Tablet when executed with bindvars <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7431">#7431</a></li>
<li>VTGate: Fix for Query Serving when Toposerver is Down <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7484">#7484</a></li>
<li>VTGate: Add necessary bindvars when preparing queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7493">#7493</a></li>
<li>VTGate: Show anywhere plan fix to consider default keyspace <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7531">#7531</a></li>
<li>VTGate: Fix table parsing on VSchema generation <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7511">#7511</a></li>
<li>VTGate: Use the emulated MySQL version for special comments <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7510">#7510</a></li>
<li>VTGate: Reset Session for Reserved Connection when the connection id is not found <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7539">#7539</a></li>
<li>VTGate: Healthcheck: update healthy tablets correctly when a stream returns an error or timeout <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7732">#7732</a></li>
<li>VTGate: Fix for reserved connection usage with transaction <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7646">#7646</a></li>
<li>VTGate: Fix MySQL Workbench failure on login with <code>select current_user()</code> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7705">#7705</a></li>
<li>VTGate: Constraint names and database names with spaces. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7745">#7745</a></li>
<li>VTGate: Fix dual table query when system schema is selected database <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7734">#7734</a></li>
</ul>
<h3>Other</h3>
<ul>
<li>VTTablet: Correctly initialize statsTabletTypeCounts during startup <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7390">#7390</a></li>
<li>Backup/Restore: Respect -disable_active_reparents in backup/restore <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7576">#7576</a></li>
<li>Backup/Restore: check disable_active_reparents properly before waiting for position update <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7703">#7703</a></li>
</ul>
<h2>Functionality Added or Changed</h2>
<h3>VTGate / MySQL compatibility / Query Serving</h3>
<ul>
<li>VTGate: Gen4 Planner: AxB vs BxA <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7274">#7274</a></li>
<li>VTGAte: Gen4 fallback planning <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7370">#7370</a></li>
<li>VTGate: Support for CALL procedures <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7287">#7287</a></li>
<li>VTGate: Set default for @<a class="user-mention" href="https://github.com/workload">@workload</a> to OLTP <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7288">#7288</a></li>
<li>VTGate: Change @<a class="user-mention" href="https://github.com/Version">@Version</a> and @@version_comment <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7337">#7337</a></li>
<li>VTGate: Fix VitessAware system variables of type boolean return NULL when MySQL is not involved <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7353">#7353</a></li>
<li>VTGate: Add stats for RowsAffected similar to RowsReturned <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7380">#7380</a></li>
<li>VTGate: Added information_schema_stats_expiry to allowed list of set vars <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7435">#7435</a></li>
<li>VTGate: LFU Cache Implementation <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7439">#7439</a></li>
<li>VTGate: Describe table to route based on table name and qualifier <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7445">#7445</a></li>
<li>VTGate: Olap error message fix <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7448">#7448</a></li>
<li>VTGate: Temporary Table support in unsharded keyspace <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7411">#7411</a></li>
<li>VTGate: Publish table size on schema <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7444">#7444</a></li>
<li>VTGate: Support for caching_sha2_password plugin in mysql/client <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6716">#6716</a></li>
<li>VTGate: Moving Show plan from executor to planbuilder <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7475">#7475</a></li>
<li>VTGate: Adds another case to merge routes for information_schema queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7504">#7504</a></li>
<li>VTGate: Add innodb_read_rows as vttablet metric <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7520">#7520</a></li>
<li>VTGate: Adds support for Show variables <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7547">#7547</a></li>
<li>VTGate: gen4: fail unsupported queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7409">#7409</a></li>
<li>VTGate: Fix Metadata in SHOW queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7540">#7540</a></li>
<li>VTGate: Update AST helper generation <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7558">#7558</a></li>
<li>VTGate: Avoiding addition of redundant unary operators <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7579">#7579</a></li>
<li>VTGate: Optimise AST rewriting <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7583">#7583</a></li>
<li>VTGate: Add Show Status query to vtexplain and make asthelpergen/sizegen quiet <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7590">#7590</a></li>
<li>VTGate: Add support for SELECT ALL <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7593">#7593</a></li>
<li>VTGate: Empty statement error code change in sql parsing <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7618">#7618</a></li>
<li>VTGate: Socket system variable to return vitess mysql socket <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7637">#7637</a></li>
<li>VTGate: Make DROP/CREATE DATABASE pluggable <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7381">#7381</a></li>
<li>VTGate: Allow Select with lock to pass through in vttablet <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7584">#7584</a></li>
<li>VTGate: Fix ordering in SELECT INTO and printing of strings <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7655">#7655</a></li>
<li>VTGate: AST Equals code generator <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7672">#7672</a></li>
<li>VTGate:  [tabletserver] More resilient wait for schema changes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7684">#7684</a></li>
<li>VTGate: Fix flush statement planner <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7695">#7695</a></li>
<li>VTGate: Produce query warnings for using features not supported when sharded <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7538">#7538</a></li>
<li>VTGate: Support for ALTER VITESS_MIGRATION statements <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7663">#7663</a></li>
<li>VTGate: Solve I_S queries using CNF rewriting <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7677">#7677</a></li>
<li>VTGate: System schema queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7685">#7685</a></li>
<li>VTGate: Make the AST visitor faster <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7701">#7701</a></li>
<li>VTGate: COM_PREPARE - Single TCP response packet with all MySQL Packets <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7713">#7713</a></li>
<li>VTGate: Replace the database name in result fields only if needed <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7714">#7714</a></li>
<li>VTGate: Split ast_helper into individual gen files <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7727">#7727</a></li>
<li>VTGate: Adds support for ordering on character fields for sharded keyspace queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7678">#7678</a></li>
<li>VTGate: Show columns query on system schema <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7729">#7729</a></li>
<li>VTGate: Disallow foreign key constraint on ddl <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7780">#7780</a></li>
<li>VTGate: VTGate: support -enable_online_ddl flag <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7694">#7694</a></li>
<li>VTGate: Default to false for system settings to be changed per session at the database connection level <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7921">#7921</a></li>
<li>VTGate: vtctl: return error on invalid ddl_strategy <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7924">#7924</a></li>
<li>VTGate: [10.0] Squashed backport of <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7903">#7903</a> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7927">#7927</a></li>
<li>VTGate: [10.0] Fix bug with reserved connections to stale tablets <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7935">#7935</a></li>
<li>VTGate: [10.0] Fix for keyspaces_to_watch regression <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7936">#7936</a></li>
<li>VTGate: [10.0] Update healthy tablets correctly for primary down <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7937">#7937</a></li>
<li>VTGate: [10.0] Allow modification of tablet unhealthy_threshold via debugEnv <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7938">#7938</a></li>
</ul>
<h3>Testing</h3>
<ul>
<li>Fuzzing: Add vtctl fuzzer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7605">#7605</a></li>
<li>Fuzzing: Add more fuzzers <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7622">#7622</a></li>
<li>Fuzzing: Add 3 fuzzers for mysql endpoints <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7639">#7639</a></li>
<li>Fuzzing: Add oss-fuzz build script <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7591">#7591</a></li>
<li>Fuzzing: Add requirement for minimum length of input data <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7722">#7722</a></li>
<li>Fuzzing: Add new mysql fuzzer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7660">#7660</a></li>
<li>Fuzzing: Add [grpcvtgateconn]  fuzzer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7689">#7689</a></li>
<li>Fuzzing: Make mysql fuzzer more calls during each iteration <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7766">#7766</a></li>
</ul>
<h3>Performance</h3>
<ul>
<li>VTGate: [perf] zero-copy tokenizer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7619">#7619</a></li>
<li>VTGate: [perf: sqlparser faster formatting <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7710">#7710</a></li>
<li>VTGate :[perf] Cache reserved bind variables in queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7698">#7698</a></li>
<li>VTGate: [perf] sqlparser yacc codegen <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7669">#7669</a></li>
<li>VTGate: Making fast AST rewriter faster <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7726">#7726</a></li>
<li>VTGate: Cached Size Implementation <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7387">#7387</a></li>
<li>VTGate: Plan remove mutexes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7468">#7468</a></li>
<li>LFU Cache Bug Fixes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7479">#7479</a></li>
<li>[cache] Handle all possible initialization cases <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7556">#7556</a></li>
<li>VTGate: [servenv] provide a global flag for profiling <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7496">#7496</a></li>
<li>VTGate: [vttablet] Benchmarks and two small optimizations <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7560">#7560</a></li>
<li>[pprof]: allow stopping profiling early with a signal <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7594">#7594</a></li>
<li>perf: RPC Serialization <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7519">#7519</a></li>
<li>perf: keyword lookups in the tokenizer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7606">#7606</a></li>
</ul>
<h3>Cluster Management</h3>
<ul>
<li>[vtctld] Migrate topo management RPCs <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7395">#7395</a></li>
<li>[vtctldclient] Set <code>SilenceErrors</code> on the root command, so we don't double-log <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7404">#7404</a></li>
<li>[vtctldclient] Command line flags: dashes and underscores synonyms <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7406">#7406</a></li>
<li>Extract the <code>maxReplPosSearch</code> struct out to <code>topotools</code> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7420">#7420</a></li>
<li>Add protoutil package, refactor ISP to use it <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7421">#7421</a></li>
<li>Add <code>ErrorGroup</code> to package concurrency, use in <code>waitOnNMinusOneTablets</code> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7429">#7429</a></li>
<li>[vtctld / wrangler] Extract some reparent methods out to functions for shared use between wrangler and VtctldServer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7434">#7434</a></li>
<li>[vtctld/wrangler] Extract <code>EmergencyReparentShard</code> logic to dedicated struct and add unit tests <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7464">#7464</a></li>
<li>Provide named function for squashing usage errors; start using it <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7451">#7451</a></li>
<li>[concurrency] Add guard against potentially blocking forever in ErrorGroup.Wait() when NumGoroutines is 0 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7463">#7463</a></li>
<li>Add hook for statsd integration <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7417">#7417</a></li>
<li>[concurrency] Add guard against potentially blocking forever in ErrorGroup.Wait() when NumGoroutines is 0 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7463">#7463</a></li>
<li>Resilient rebuild keyspace graph check, tablet controls not in <code>RebuildKeyspaceGraph</code> command  <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7442">#7442</a></li>
<li>[reparentutil / ERS] confirm at least one replica succeeded to <code>SetMaster</code>, or fail <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7486">#7486</a></li>
<li>[reparentutil / wrangler] Extract PlannedReparentShard logic from wrangler to PlannedReparenter struct <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7501">#7501</a></li>
<li>Add backup/restore duration stats <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7512">#7512</a></li>
<li>Refresh replicas and rdonly after MigrateServedTypes except on skipRefreshState. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7327">#7327</a></li>
<li>[eparentutil] ERS should not attempt to WaitForRelayLogsToApply on primary tablets that were not running replication <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7523">#7523</a></li>
<li>[orchestrator] prevent XSS attack via 'orchestrator-msg' params <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7526">#7526</a></li>
<li>[vtctld] Add remaining reparent commands to VtctldServer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7536">#7536</a></li>
<li>[reparentutil] ERS should not attempt to WaitForRelayLogsToApply on primary tablets that were not running replication <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7523">#7523</a></li>
<li>Shutdown vttablet gracefully if tablet record disappears <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7563">#7563</a></li>
<li>ApplySchema: -skip_preflight <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7587">#7587</a></li>
<li>Table GC: disable binary logging on best effort basis <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7588">#7588</a></li>
<li>Addition of waitSig pprof argument to start recording on USR1 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7616">#7616</a></li>
<li>Add combine TLS certs feature <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7609">#7609</a></li>
<li>Check error response before attempting to access InitShardPrimary response <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7658">#7658</a></li>
<li>[vtctld] Migrate GetSrvKeyspace as GetSrvKeyspaces in VtctldServer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7680">#7680</a></li>
<li>[vtctld] Migrate ShardReplicationPositions <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7690">#7690</a></li>
<li>[reparentutil | ERS] Bind status variable to each goroutine in WaitForRelayLogsToApply <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7692">#7692</a></li>
<li>[servenv] Fix var shadowing caused by short variable declaration <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7702">#7702</a></li>
<li>[vtctl|vtctldserver] List/Get Tablets timeouts <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7715">#7715</a></li>
<li>vtctl ApplySchema supports '-request_context' flag <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7777">#7777</a></li>
</ul>
<h3>VReplication</h3>
<ul>
<li>VReplication: vstreamer to throttle on source endpoint <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7324">#7324</a></li>
<li>VReplication: Throttle on target tablet <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7364">#7364</a></li>
<li>VReplication: Throttler: fix to client usage in vreplication and table GC <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7422">#7422</a></li>
<li>VReplication: MoveTables/Reshard add flags to start workflows in a stopped state and to stop workflow once copy is completed <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7449">#7449</a></li>
<li>VReplication: Support for caching_sha2_password plugin in mysql/client <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6716">#6716</a></li>
<li>VReplication: Validate SrvKeyspace during Reshard/SwitchReads <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7481">#7481</a></li>
<li>VReplication: [MoveTables] Refresh SrvVSchema (for Routing Rules) and source tablets (for Blacklisted Tables) on completion <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7505">#7505</a></li>
<li>VReplication : Data migration from another Vitess cluster <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7546">#7546</a></li>
<li>VReplication : [materialize] Add cells and tablet_types parameters <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7562">#7562</a></li>
<li>VReplication:  JSON Columns: fix bug where vreplication of update statements were failing <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7640">#7640</a></li>
<li>VReplication: Make the frequency at which heartbeats update the _vt.vreplication table configurable <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7659">#7659</a></li>
<li>VReplication: Error out if binlog compression is turned on <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7670">#7670</a></li>
<li>VReplication: Tablet throttler: support for custom query &amp; threshold <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7541">#7541</a></li>
<li>VStream API: allow aligning streams from different shards to minimize skews across the streams <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7626">#7626</a></li>
<li>VReplication: Backport 7809: Update rowlog for the API change made for the vstream skew alignment feature <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7890">#7890</a></li>
</ul>
<h3>OnlineDDL</h3>
<ul>
<li>OnlineDDL: update gh-ost binary to v1.1.1 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7394">#7394</a></li>
<li>Online DDL via VReplication <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7419">#7419</a></li>
<li>Online DDL: VReplicatoin based mini stress test CI <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7492">#7492</a></li>
<li>OnlineDDL: Revert for VReplication based migrations <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7478">#7478</a></li>
<li>Online DDL: Internal support for eta_seconds <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7630">#7630</a></li>
<li>Online DDL: Support 'SHOW VITESS_MIGRATIONS' queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7638">#7638</a></li>
<li>Online DDL: Support for REVERT VITESS_MIGRATION statement <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7656">#7656</a></li>
<li>Online DDL: Declarative Online DDL <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7725">#7725</a></li>
</ul>
<h3>VTAdmin</h3>
<p>Vitess 10.0 introduces a highly-experimental multi-cluster admin API and web UI, called VTAdmin. Deploying the vtadmin-api and vtadmin-web components is completely opt-in. If you're interested in trying it out and providing early feedback, come find us in #feat-vtadmin in the Vitess slack. Note that VTAdmin relies on the new VtctldServer API, so you must be running the new grpc-vtctld service on your vtctlds in order to use it.</p>
<ul>
<li>VTAdmin: Add vtadmin-web build flag for configuring fetch credentials <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7414">#7414</a></li>
<li>VTAdmin: Add <code>cluster</code> field to vtadmin-api's /api/gates response <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7425">#7425</a></li>
<li>VTAdmin: Add /api/clusters endpoint to vtadmin-api <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7426">#7426</a></li>
<li>VTAdmin: Add /api/schemas endpoint to vtadmin-api <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7432">#7432</a></li>
<li>VTAdmin: [vtadmin-web] Add routes and simple tables for all entities <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7440">#7440</a></li>
<li>VTAdmin: [vtadmin-web] Set document.title from route components <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7450">#7450</a></li>
<li>VTAdmin: [vtadmin-web] Add DataTable component with URL pagination <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7487">#7487</a></li>
<li>VTAdmin: [vtadmin-api] Add shards to /api/keyspaces response <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7453">#7453</a></li>
<li>VTAdmin: [vtadmin-web] Add replaceQuery + pushQuery to useURLQuery hook <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7507">#7507</a></li>
<li>VTAdmin: [vtadmin-web] An initial pass for tablet filters <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7515">#7515</a></li>
<li>VTAdmin: [vtadmin-web] Add a Select component <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7524">#7524</a></li>
<li>VTAdmin: [vtadmin-api] Add /vtexplain endpoint <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7528">#7528</a></li>
<li>VTAdmin: [vtadmin-api] Reorganize tablet-related functions into vtadmin/cluster/cluster.go <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7553">#7553</a></li>
<li>VTAdmin: Three small bugfixes in Tablets table around stable sort order, display type lookup, and filtering by type <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7568">#7568</a></li>
<li>VTAdmin: [vtadmin] Add GetSchema endpoint <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7596">#7596</a></li>
<li>VTAdmin: [vtadmin/testutil] Add testutil helper to manage the complexity of recursively calling WithTestServer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7601">#7601</a></li>
<li>VTAdmin: [vtadmin] Add FindSchema route <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7610">#7610</a></li>
<li>VTAdmin: [vtadmin-web] Add simple /schema view with table definition <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7615">#7615</a></li>
<li>VTAdmin: [vtadmin] vschemas api endpoints <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7625">#7625</a></li>
<li>VTAdmin: [vtadmin] Add support for additional service healthchecks in grpcserver <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7635">#7635</a></li>
<li>VTAdmin: [vtadmin] test refactors <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7641">#7641</a></li>
<li>VTAdmin: [vtadmin] propagate error contexts <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7642">#7642</a></li>
<li>VTAdmin: [vtadmin] tracing refactor <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7649">#7649</a></li>
<li>VTAdmin: [vtadmin] GetWorkflow(s) endpoints <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7662">#7662</a></li>
<li>VTAdmin: [vitessdriver|vtadmin] Support Ping in vitessdriver, use in vtadmin to healthcheck connections during Dial <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7709">#7709</a></li>
<li>VTAdmin: [vtadmin]  Add to local example <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7699">#7699</a></li>
<li>VTAdmin: [vtexplain] lock <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7724">#7724</a></li>
<li>VTAdmin: [vtadmin] Aggregate schema sizes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7751">#7751</a></li>
<li>VTAdmin: [vtadmin-web] Add comments + 'options' parameter to API hooks <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7754">#7754</a></li>
<li>VTAdmin: [vtadmin-web] Add common max-width to infrastructure table views <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7760">#7760</a></li>
<li>VTAdmin: [vtadmin-web] Add hooks + skeleton view for workflows <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7762">#7762</a></li>
<li>VTAdmin: [vtadmin-web] Add a hasty filter input to the /schemas view <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7779">#7779</a></li>
</ul>
<h3>Other / Tools</h3>
<ul>
<li>[rulesctl] Implements CLI tool for rule management <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7712">#7712</a></li>
</ul>
<h2>Examples / Tutorials</h2>
<ul>
<li>Source correct shell script in README <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7749">#7749</a></li>
</ul>
<h2>Documentation</h2>
<ul>
<li>Add Severity Labels document <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7542">#7542</a></li>
<li>Remove Google Groups references <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7664">#7664</a></li>
<li>Move some commas around in README.md :) <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7671">#7671</a></li>
<li>Add Andrew Mason to Maintainers List <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7757">#7757</a></li>
</ul>
<h2>Build/CI Environment Changes</h2>
<ul>
<li>Update java build versions to vitess 10.0.0 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7383">#7383</a></li>
<li>CI: check run analysis to post JSON from file <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7386">#7386</a></li>
<li>Fix Dockerfiles for vtexplain and vtctlclient <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7418">#7418</a></li>
<li>CI: Add descriptive names to vrep shards. Update test generator script <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7454">#7454</a></li>
<li>CI: adding 'go mod tidy' test <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7461">#7461</a></li>
<li>Docker builds vitess/vtctlclient to install curl <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7466">#7466</a></li>
<li>Add VT_BASE_VER to vtexplain/Dockerfile <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7467">#7467</a></li>
<li>Enable -mysql_server_version in vttestserver, and utilize it in vttestserver container images <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7474">#7474</a></li>
<li>[vtctld | tests only] testtmclient refactor <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7518">#7518</a></li>
<li>CI: skip some tests on forked repos <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7527">#7527</a></li>
<li>Workflow to check make sizegen <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7535">#7535</a></li>
<li>Add mysqlctl docker image <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7557">#7557</a></li>
<li>Restore CI workflow shard 26, accidentally dropped <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7569">#7569</a></li>
<li>Update CODEOWNERS <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7586">#7586</a></li>
<li>CI: ci-workflow-gen  turn string to array to reduce conflicts <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7582">#7582</a></li>
<li>Add percona-toolkit (for pt-osc/pt-online-schema-change) to the docker/lite images <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7603">#7603</a></li>
<li>CI: Use ubuntu-18.04 in tests <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7614">#7614</a></li>
<li>[vttestserver] Fix to work with sharded keyspaces <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7617">#7617</a></li>
<li>Add tools.go <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7517">#7517</a></li>
<li>Make vttestserver compatible with persistent data directories <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7718">#7718</a></li>
<li>Add vtorc binary for rpm,deb builds <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7750">#7750</a></li>
<li>Fixes bug that prevents creation of logs directory <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7761">#7761</a></li>
<li>[Java] Guava update to 31.1.1 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7764">#7764</a></li>
<li>make: build vitess as static binaries by default <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7795">#7795</a> ← Potentially breaking change</li>
<li>make: build vitess as static binaries by default (10.0 backport) <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7808">#7808</a></li>
<li>java: prepare java version for release 10.0 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7922">#7922</a></li>
</ul>
<h2>Functionality Neutral Changes</h2>
<ul>
<li>VTGate: Remove unused key.Destination.IsUnique() <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7565">#7565</a></li>
<li>VTGate: Add information_schema query on prepare statement <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7746">#7746</a></li>
<li>VTGate: Tests for numeric_precision and numeric_scale columns in information_schema <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7763">#7763</a></li>
<li>Disable flaky test until it can be fixed <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7623">#7623</a></li>
<li>Tests: reset stat at the beginning of test <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7644">#7644</a></li>
<li>Cleanup mysql server_test <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7645">#7645</a></li>
<li>vttablet: fix flaky tests <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7543">#7543</a></li>
<li>Removed unused tests for Wordpress installation <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7516">#7516</a></li>
<li>Fix unit test fail after merge <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7550">#7550</a></li>
<li>Add test with NULL input values for vindexes that did not have any. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7552">#7552</a></li>
</ul>
<h2>VtctldServer</h2>
<p>As part of an ongoing effort to transition from the VtctlServer gRPC API to the newer VtctldServer gRPC API, we have updated the local example to use the corresponding new vtctldclient to perform InitShardPrimary (formerly, InitShardMaster) operations.</p>
<p>To enable the new VtctldServer in your vtctld components, update the -service_map flag to include grpc-vtctld. You may specify both grpc-vtctl,grpc-vtctld to gracefully transition.</p>
<p>The migration is still underway, but you may begin to transition to the new client for migrated commands. For a full listing, refer either to proto/vtctlservice.proto or consult vtctldclient --help.</p>

## v10.0.0-rc1-mysql80
<p style="font-size:12px;"> 15, Apr 2021 
<a href="https://github.com/vitessio/vitess/releases/tag/v10.0.0-rc1-mysql80" target="_blank"> 
Source </a><OutboundLink /></p>
<p>tag to trigger mysql80 build on dockerhub</p>

## Vitess 10.0.0-rc1
<p style="font-size:12px;"> 06, Apr 2021 
<a href="https://github.com/vitessio/vitess/releases/tag/v10.0.0-rc1" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release complies with VEP-3 which removes the upgrade order requirement. Components can be upgraded in any order. It is recommended that the upgrade order should still be followed if possible, except to canary test the new version of VTGate before upgrading the rest of the components.</p>
<p>The following PRs made changes to behaviors that clients might rely on. They should be reviewed carefully so that client code can be changed in concert with a Vitess release deployment.</p>
<h2>Bugs Fixed</h2>
<h3>VTGate / MySQL compatibility</h3>
<ul>
<li>Remove printing of ENFORCED word so that statements remain compatible with mysql 5.7 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7458">#7458</a></li>
<li>Allow any ordering of generic options in column definitions <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7459">#7459</a></li>
<li>Corrects the comment handling in vitess <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7581">#7581</a></li>
<li>Fix regression - should be able to plan subquery on top of subquery <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7682">#7682</a></li>
<li>Nullable Timestamp Column Fix <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7740">#7740</a></li>
<li>VTGate: Fix the error messages in drop, create and alter database commands <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7397">#7397</a></li>
<li>VTGate: Fix information_schema query with system schema in table_schema filter <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7430">#7430</a></li>
<li>VTGate: Fix Set Statement in Tablet when executed with bindvars <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7431">#7431</a></li>
<li>VTGate: Fix for Query Serving when Toposerver is Down <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7484">#7484</a></li>
<li>VTGate: Add necessary bindvars when preparing queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7493">#7493</a></li>
<li>VTGate: Show anywhere plan fix to consider default keyspace <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7531">#7531</a></li>
<li>VTGate: Fix table parsing on VSchema generation <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7511">#7511</a></li>
<li>VTGate: Use the emulated MySQL version for special comments <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7510">#7510</a></li>
<li>VTGate: Reset Session for Reserved Connection when the connection id is not found <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7539">#7539</a></li>
<li>VTGate: Healthcheck: update healthy tablets correctly when a stream returns an error or timeout <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7732">#7732</a></li>
<li>VTGate: Fix for reserved connection usage with transaction <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7646">#7646</a></li>
<li>VTGate: Fix MySQL Workbench failure on login with <code>select current_user()</code> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7705">#7705</a></li>
<li>VTGate: Constraint names and database names with spaces. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7745">#7745</a></li>
<li>VTGate: Fix dual table query when system schema is selected database <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7734">#7734</a></li>
</ul>
<h3>Other</h3>
<ul>
<li>VTTablet: Correctly initialize statsTabletTypeCounts during startup <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7390">#7390</a></li>
<li>Backup/Restore: Respect -disable_active_reparents in backup/restore <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7576">#7576</a></li>
<li>Backup/Restore: check disable_active_reparents properly before waiting for position update <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7703">#7703</a></li>
</ul>
<h2>Functionality Added or Changed</h2>
<h3>VTGate / MySQL compatibility / Query Serving</h3>
<ul>
<li>VTGate: Gen4 Planner: AxB vs BxA <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7274">#7274</a></li>
<li>VTGAte: Gen4 fallback planning <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7370">#7370</a></li>
<li>VTGate: Support for CALL procedures <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7287">#7287</a></li>
<li>VTGate: Set default for @<a class="user-mention" href="https://github.com/workload">@workload</a> to OLTP <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7288">#7288</a></li>
<li>VTGate: Change @<a class="user-mention" href="https://github.com/Version">@Version</a> and @@version_comment <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7337">#7337</a></li>
<li>VTGate: Fix VitessAware system variables of type boolean return NULL when MySQL is not involved <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7353">#7353</a></li>
<li>VTGate: Add stats for RowsAffected similar to RowsReturned <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7380">#7380</a></li>
<li>VTGate: Added information_schema_stats_expiry to allowed list of set vars <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7435">#7435</a></li>
<li>VTGate: LFU Cache Implementation <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7439">#7439</a></li>
<li>VTGate: Describe table to route based on table name and qualifier <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7445">#7445</a></li>
<li>VTGate: Olap error message fix <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7448">#7448</a></li>
<li>VTGate: Temporary Table support in unsharded keyspace <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7411">#7411</a></li>
<li>VTGate: Publish table size on schema <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7444">#7444</a></li>
<li>VTGate: Support for caching_sha2_password plugin in mysql/client <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6716">#6716</a></li>
<li>VTGate: Moving Show plan from executor to planbuilder <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7475">#7475</a></li>
<li>VTGate: Adds another case to merge routes for information_schema queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7504">#7504</a></li>
<li>VTGate: Add innodb_read_rows as vttablet metric <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7520">#7520</a></li>
<li>VTGate: Adds support for Show variables <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7547">#7547</a></li>
<li>VTGate: gen4: fail unsupported queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7409">#7409</a></li>
<li>VTGate: Fix Metadata in SHOW queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7540">#7540</a></li>
<li>VTGate: Update AST helper generation <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7558">#7558</a></li>
<li>VTGate: Avoiding addition of redundant unary operators <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7579">#7579</a></li>
<li>VTGate: Optimise AST rewriting <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7583">#7583</a></li>
<li>VTGate: Add Show Status query to vtexplain and make asthelpergen/sizegen quiet <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7590">#7590</a></li>
<li>VTGate: Add support for SELECT ALL <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7593">#7593</a></li>
<li>VTGate: Empty statement error code change in sql parsing <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7618">#7618</a></li>
<li>VTGate: Socket system variable to return vitess mysql socket <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7637">#7637</a></li>
<li>VTGate: Make DROP/CREATE DATABASE pluggable <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7381">#7381</a></li>
<li>VTGate: Allow Select with lock to pass through in vttablet <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7584">#7584</a></li>
<li>VTGate: Fix ordering in SELECT INTO and printing of strings <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7655">#7655</a></li>
<li>VTGate: AST Equals code generator <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7672">#7672</a></li>
<li>VTGate:  [tabletserver] More resilient wait for schema changes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7684">#7684</a></li>
<li>VTGate: Fix flush statement planner <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7695">#7695</a></li>
<li>VTGate: Produce query warnings for using features not supported when sharded <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7538">#7538</a></li>
<li>VTGate: Support for ALTER VITESS_MIGRATION statements <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7663">#7663</a></li>
<li>VTGate: Solve I_S queries using CNF rewriting <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7677">#7677</a></li>
<li>VTGate: System schema queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7685">#7685</a></li>
<li>VTGate: Make the AST visitor faster <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7701">#7701</a></li>
<li>VTGate: COM_PREPARE - Single TCP response packet with all MySQL Packets <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7713">#7713</a></li>
<li>VTGate: Replace the database name in result fields only if needed <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7714">#7714</a></li>
<li>VTGate: Split ast_helper into individual gen files <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7727">#7727</a></li>
<li>VTGate: Adds support for ordering on character fields for sharded keyspace queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7678">#7678</a></li>
<li>VTGate: Show columns query on system schema <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7729">#7729</a></li>
<li>VTGate: Disallow foreign key constraint on ddl <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7780">#7780</a></li>
<li>VTGate: VTGate: support -enable_online_ddl flag <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7694">#7694</a></li>
</ul>
<h3>Testing</h3>
<ul>
<li>Fuzzing: Add vtctl fuzzer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7605">#7605</a></li>
<li>Fuzzing: Add more fuzzers <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7622">#7622</a></li>
<li>Fuzzing: Add 3 fuzzers for mysql endpoints <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7639">#7639</a></li>
<li>Fuzzing: Add oss-fuzz build script <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7591">#7591</a></li>
<li>Fuzzing: Add requirement for minimum length of input data <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7722">#7722</a></li>
<li>Fuzzing: Add new mysql fuzzer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7660">#7660</a></li>
<li>Fuzzing: Add [grpcvtgateconn]  fuzzer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7689">#7689</a></li>
<li>Fuzzing: Make mysql fuzzer more calls during each iteration <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7766">#7766</a></li>
</ul>
<h3>Performance</h3>
<ul>
<li>VTGate: [perf] zero-copy tokenizer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7619">#7619</a></li>
<li>VTGate: [perf: sqlparser faster formatting <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7710">#7710</a></li>
<li>VTGate :[perf] Cache reserved bind variables in queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7698">#7698</a></li>
<li>VTGate: [perf] sqlparser yacc codegen <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7669">#7669</a></li>
<li>VTGate: Making fast AST rewriter faster <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7726">#7726</a></li>
<li>VTGate: Cached Size Implementation <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7387">#7387</a></li>
<li>VTGate: Plan remove mutexes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7468">#7468</a></li>
<li>LFU Cache Bug Fixes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7479">#7479</a></li>
<li>[cache] Handle all possible initialization cases <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7556">#7556</a></li>
<li>VTGate: [servenv] provide a global flag for profiling <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7496">#7496</a></li>
<li>VTGate: [vttablet] Benchmarks and two small optimizations <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7560">#7560</a></li>
<li>[pprof]: allow stopping profiling early with a signal <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7594">#7594</a></li>
<li>perf: RPC Serialization <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7519">#7519</a></li>
<li>perf: keyword lookups in the tokenizer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7606">#7606</a></li>
</ul>
<h3>Cluster Management</h3>
<ul>
<li>[vtctld] Migrate topo management RPCs <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7395">#7395</a></li>
<li>[vtctldclient] Set <code>SilenceErrors</code> on the root command, so we don't double-log <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7404">#7404</a></li>
<li>[vtctldclient] Command line flags: dashes and underscores synonyms <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7406">#7406</a></li>
<li>Extract the <code>maxReplPosSearch</code> struct out to <code>topotools</code> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7420">#7420</a></li>
<li>Add protoutil package, refactor ISP to use it <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7421">#7421</a></li>
<li>Add <code>ErrorGroup</code> to package concurrency, use in <code>waitOnNMinusOneTablets</code> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7429">#7429</a></li>
<li>[vtctld / wrangler] Extract some reparent methods out to functions for shared use between wrangler and VtctldServer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7434">#7434</a></li>
<li>[vtctld/wrangler] Extract <code>EmergencyReparentShard</code> logic to dedicated struct and add unit tests <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7464">#7464</a></li>
<li>Provide named function for squashing usage errors; start using it <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7451">#7451</a></li>
<li>[concurrency] Add guard against potentially blocking forever in ErrorGroup.Wait() when NumGoroutines is 0 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7463">#7463</a></li>
<li>Add hook for statsd integration <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7417">#7417</a></li>
<li>[concurrency] Add guard against potentially blocking forever in ErrorGroup.Wait() when NumGoroutines is 0 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7463">#7463</a></li>
<li>Resilient rebuild keyspace graph check, tablet controls not in <code>RebuildKeyspaceGraph</code> command  <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7442">#7442</a></li>
<li>[reparentutil / ERS] confirm at least one replica succeeded to <code>SetMaster</code>, or fail <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7486">#7486</a></li>
<li>[reparentutil / wrangler] Extract PlannedReparentShard logic from wrangler to PlannedReparenter struct <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7501">#7501</a></li>
<li>Add backup/restore duration stats <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7512">#7512</a></li>
<li>Refresh replicas and rdonly after MigrateServedTypes except on skipRefreshState. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7327">#7327</a></li>
<li>[eparentutil] ERS should not attempt to WaitForRelayLogsToApply on primary tablets that were not running replication <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7523">#7523</a></li>
<li>[orchestrator] prevent XSS attack via 'orchestrator-msg' params <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7526">#7526</a></li>
<li>[vtctld] Add remaining reparent commands to VtctldServer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7536">#7536</a></li>
<li>[reparentutil] ERS should not attempt to WaitForRelayLogsToApply on primary tablets that were not running replication <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7523">#7523</a></li>
<li>Shutdown vttablet gracefully if tablet record disappears <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7563">#7563</a></li>
<li>ApplySchema: -skip_preflight <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7587">#7587</a></li>
<li>Table GC: disable binary logging on best effort basis <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7588">#7588</a></li>
<li>Addition of waitSig pprof argument to start recording on USR1 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7616">#7616</a></li>
<li>Add combine TLS certs feature <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7609">#7609</a></li>
<li>Check error response before attempting to access InitShardPrimary response <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7658">#7658</a></li>
<li>[vtctld] Migrate GetSrvKeyspace as GetSrvKeyspaces in VtctldServer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7680">#7680</a></li>
<li>[vtctld] Migrate ShardReplicationPositions <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7690">#7690</a></li>
<li>[reparentutil | ERS] Bind status variable to each goroutine in WaitForRelayLogsToApply <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7692">#7692</a></li>
<li>[servenv] Fix var shadowing caused by short variable declaration <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7702">#7702</a></li>
<li>[vtctl|vtctldserver] List/Get Tablets timeouts <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7715">#7715</a></li>
<li>vtctl ApplySchema supports '-request_context' flag <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7777">#7777</a></li>
</ul>
<h3>VReplication</h3>
<ul>
<li>VReplication: vstreamer to throttle on source endpoint <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7324">#7324</a></li>
<li>VReplication: Throttle on target tablet <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7364">#7364</a></li>
<li>VReplication: Throttler: fix to client usage in vreplication and table GC <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7422">#7422</a></li>
<li>VReplication: MoveTables/Reshard add flags to start workflows in a stopped state and to stop workflow once copy is completed <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7449">#7449</a></li>
<li>VReplication: Support for caching_sha2_password plugin in mysql/client <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6716">#6716</a></li>
<li>VReplication: Validate SrvKeyspace during Reshard/SwitchReads <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7481">#7481</a></li>
<li>VReplication: [MoveTables] Refresh SrvVSchema (for Routing Rules) and source tablets (for Blacklisted Tables) on completion <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7505">#7505</a></li>
<li>VReplication : Data migration from another Vitess cluster <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7546">#7546</a></li>
<li>VReplication : [materialize] Add cells and tablet_types parameters <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7562">#7562</a></li>
<li>VReplication:  JSON Columns: fix bug where vreplication of update statements were failing <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7640">#7640</a></li>
<li>VReplication: Make the frequency at which heartbeats update the _vt.vreplication table configurable <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7659">#7659</a></li>
<li>VReplication: Error out if binlog compression is turned on <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7670">#7670</a></li>
<li>VReplication: Tablet throttler: support for custom query &amp; threshold <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7541">#7541</a></li>
<li>VStream API: allow aligning streams from different shards to minimize skews across the streams <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7626">#7626</a></li>
</ul>
<h3>OnlineDDL</h3>
<ul>
<li>OnlineDDL: update gh-ost binary to v1.1.1 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7394">#7394</a></li>
<li>Online DDL via VReplication <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7419">#7419</a></li>
<li>Online DDL: VReplicatoin based mini stress test CI <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7492">#7492</a></li>
<li>OnlineDDL: Revert for VReplication based migrations <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7478">#7478</a></li>
<li>Online DDL: Internal support for eta_seconds <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7630">#7630</a></li>
<li>Online DDL: Support 'SHOW VITESS_MIGRATIONS' queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7638">#7638</a></li>
<li>Online DDL: Support for REVERT VITESS_MIGRATION statement <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7656">#7656</a></li>
<li>Online DDL: Declarative Online DDL <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7725">#7725</a></li>
</ul>
<h3>VTAdmin</h3>
<ul>
<li>VTAdmin: Add vtadmin-web build flag for configuring fetch credentials <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7414">#7414</a></li>
<li>VTAdmin: Add <code>cluster</code> field to vtadmin-api's /api/gates response <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7425">#7425</a></li>
<li>VTAdmin: Add /api/clusters endpoint to vtadmin-api <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7426">#7426</a></li>
<li>VTAdmin: Add /api/schemas endpoint to vtadmin-api <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7432">#7432</a></li>
<li>VTAdmin: [vtadmin-web] Add routes and simple tables for all entities <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7440">#7440</a></li>
<li>VTAdmin: [vtadmin-web] Set document.title from route components <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7450">#7450</a></li>
<li>VTAdmin: [vtadmin-web] Add DataTable component with URL pagination <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7487">#7487</a></li>
<li>VTAdmin: [vtadmin-api] Add shards to /api/keyspaces response <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7453">#7453</a></li>
<li>VTAdmin: [vtadmin-web] Add replaceQuery + pushQuery to useURLQuery hook <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7507">#7507</a></li>
<li>VTAdmin: [vtadmin-web] An initial pass for tablet filters <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7515">#7515</a></li>
<li>VTAdmin: [vtadmin-web] Add a Select component <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7524">#7524</a></li>
<li>VTAdmin: [vtadmin-api] Add /vtexplain endpoint <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7528">#7528</a></li>
<li>VTAdmin: [vtadmin-api] Reorganize tablet-related functions into vtadmin/cluster/cluster.go <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7553">#7553</a></li>
<li>VTAdmin: Three small bugfixes in Tablets table around stable sort order, display type lookup, and filtering by type <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7568">#7568</a></li>
<li>VTAdmin: [vtadmin] Add GetSchema endpoint <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7596">#7596</a></li>
<li>VTAdmin: [vtadmin/testutil] Add testutil helper to manage the complexity of recursively calling WithTestServer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7601">#7601</a></li>
<li>VTAdmin: [vtadmin] Add FindSchema route <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7610">#7610</a></li>
<li>VTAdmin: [vtadmin-web] Add simple /schema view with table definition <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7615">#7615</a></li>
<li>VTAdmin: [vtadmin] vschemas api endpoints <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7625">#7625</a></li>
<li>VTAdmin: [vtadmin] Add support for additional service healthchecks in grpcserver <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7635">#7635</a></li>
<li>VTAdmin: [vtadmin] test refactors <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7641">#7641</a></li>
<li>VTAdmin: [vtadmin] propagate error contexts <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7642">#7642</a></li>
<li>VTAdmin: [vtadmin] tracing refactor <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7649">#7649</a></li>
<li>VTAdmin: [vtadmin] GetWorkflow(s) endpoints <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7662">#7662</a></li>
<li>VTAdmin: [vitessdriver|vtadmin] Support Ping in vitessdriver, use in vtadmin to healthcheck connections during Dial <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7709">#7709</a></li>
<li>VTAdmin: [vtadmin]  Add to local example <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7699">#7699</a></li>
<li>VTAdmin: vtexplain lock <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7724">#7724</a></li>
<li>VTAdmin: [vtadmin] Aggregate schema sizes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7751">#7751</a></li>
<li>VTAdmin: [vtadmin-web] Add comments + 'options' parameter to API hooks <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7754">#7754</a></li>
<li>VTAdmin: [vtadmin-web] Add common max-width to infrastructure table views <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7760">#7760</a></li>
<li>VTAdmin: [vtadmin-web] Add hooks + skeleton view for workflows <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7762">#7762</a></li>
<li>VTAdmin: [vtadmin-web] Add a hasty filter input to the /schemas view <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7779">#7779</a></li>
</ul>
<h3>Other / Tools</h3>
<ul>
<li>[rulesctl] Implements CLI tool for rule management <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7712">#7712</a></li>
</ul>
<h2>Examples / Tutorials</h2>
<ul>
<li>Source correct shell script in README <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7749">#7749</a></li>
</ul>
<h2>Documentation</h2>
<ul>
<li>Add Severity Labels document <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7542">#7542</a></li>
<li>Remove Google Groups references <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7664">#7664</a></li>
<li>Move some commas around in README.md :) <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7671">#7671</a></li>
<li>Add Andrew Mason to Maintainers List <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7757">#7757</a></li>
</ul>
<h2>Build/CI Environment Changes</h2>
<ul>
<li>Update java build versions to vitess 10.0.0 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7383">#7383</a></li>
<li>CI: check run analysis to post JSON from file <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7386">#7386</a></li>
<li>Fix Dockerfiles for vtexplain and vtctlclient <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7418">#7418</a></li>
<li>CI: Add descriptive names to vrep shards. Update test generator script <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7454">#7454</a></li>
<li>CI: adding 'go mod tidy' test <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7461">#7461</a></li>
<li>Docker builds vitess/vtctlclient to install curl <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7466">#7466</a></li>
<li>Add VT_BASE_VER to vtexplain/Dockerfile <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7467">#7467</a></li>
<li>Enable -mysql_server_version in vttestserver, and utilize it in vttestserver container images <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7474">#7474</a></li>
<li>[vtctld | tests only] testtmclient refactor <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7518">#7518</a></li>
<li>CI: skip some tests on forked repos <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7527">#7527</a></li>
<li>Workflow to check make sizegen <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7535">#7535</a></li>
<li>Add mysqlctl docker image <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7557">#7557</a></li>
<li>Restore CI workflow shard 26, accidentally dropped <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7569">#7569</a></li>
<li>Update CODEOWNERS <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7586">#7586</a></li>
<li>CI: ci-workflow-gen  turn string to array to reduce conflicts <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7582">#7582</a></li>
<li>Add percona-toolkit (for pt-osc/pt-online-schema-change) to the docker/lite images <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7603">#7603</a></li>
<li>CI: Use ubuntu-18.04 in tests <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7614">#7614</a></li>
<li>[vttestserver] Fix to work with sharded keyspaces <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7617">#7617</a></li>
<li>Add tools.go <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7517">#7517</a></li>
<li>Make vttestserver compatible with persistent data directories <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7718">#7718</a></li>
<li>Add vtorc binary for rpm,deb builds <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7750">#7750</a></li>
<li>Fixes bug that prevents creation of logs directory <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7761">#7761</a></li>
<li>[Java] Guava update to 31.1.1 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7764">#7764</a></li>
</ul>
<h2>Functionality Neutral Changes</h2>
<ul>
<li>VTGate: Remove unused key.Destination.IsUnique() <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7565">#7565</a></li>
<li>VTGate: Add information_schema query on prepare statement <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7746">#7746</a></li>
<li>VTGate: Tests for numeric_precision and numeric_scale columns in information_schema <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7763">#7763</a></li>
<li>Disable flaky test until it can be fixed <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7623">#7623</a></li>
<li>Tests: reset stat at the beginning of test <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7644">#7644</a></li>
<li>Cleanup mysql server_test <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7645">#7645</a></li>
<li>vttablet: fix flaky tests <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7543">#7543</a></li>
<li>Removed unused tests for Wordpress installation <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7516">#7516</a></li>
<li>Fix unit test fail after merge <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7550">#7550</a></li>
<li>Add test with NULL input values for vindexes that did not have any. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7552">#7552</a></li>
</ul>

## v0.9.0
<p style="font-size:12px;"> 30, Jan 2021 
<a href="https://github.com/vitessio/vitess/releases/tag/v0.9.0" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Tagging v9.0.0 also as v0.9.0 for godoc/go modules</p>

## Vitess 9.0.0
<p style="font-size:12px;"> 07, May 2021 
<a href="https://github.com/vitessio/vitess/releases/tag/v9.0.0" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release complies with VEP-3 which removes the upgrade order requirement. Components can be upgraded in any order. It is recommended that the upgrade order should still be followed if possible, except to canary test the new version of VTGate before upgrading the rest of the components.</p>
<h2>Incompatible Changes</h2>
<p>The following PRs made changes to behaviors that clients might rely on. They should be reviewed carefully so that client code can be changed in concert with a Vitess release deployment.</p>
<ul>
<li>The update to golang 1.15 (<a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7204">#7204</a>) might break systems that use TLS certificates with a common name. A fix is documented here (<a class="issue-link js-issue-link" href="https://github.com/golang/go/issues/40748#issuecomment-673612108">golang/go#40748 (comment)</a>)</li>
</ul>
<p>Vitess 9.0 is not compatible with the previous release of the Vitess Kubernetes Operator (2.2.0). A new version of the Operator (2.3.0) is available that is compatible.</p>
<h2>Known Issue(s)</h2>
<ul>
<li>VReplication errors when a fixed-length binary column is used as the sharding key <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/issues/8080">#8080</a></li>
</ul>
<h2>Bugs Fixed</h2>
<h3>VTGate / MySQL compatibility</h3>
<ul>
<li>Set Global <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6957">#6957</a></li>
<li>Set udv allow more expressions <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6964">#6964</a></li>
<li>Bug which caused the connection to not close in case of error writing an error packet <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6977">#6977</a></li>
<li>Bug fix <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/issues/7048">#7048</a> for SelectNone in StreamExecute route engine <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7050">#7050</a></li>
</ul>
<h3>Other</h3>
<ul>
<li>Binary PK: fix bug where padding of binary columns was being done incorrectly <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6963">#6963</a></li>
<li>Pad non-fractional part of DECIMAL type <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6967">#6967</a></li>
<li>Bug fix regression in /healthz <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7090">#7090</a></li>
<li>Fix metadata related operation hangs when zk down <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7228">#7228</a></li>
<li>Fix accidentally-broken legacy vtctl output format <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7285">#7285</a></li>
</ul>
<h2>Functionality Added or Changed</h2>
<h3>VTGate / MySQL compatibility</h3>
<ul>
<li>VTGate: Allow INSERT with all defaults <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6969">#6969</a></li>
<li>VTGate: Allow YEAR column type with length specified <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6975">#6975</a></li>
<li>VTGate: Retry Execute when reserved connection is lost <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6983">#6983</a></li>
<li>VTGate: Use ephemeral buffer when reading rows <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6990">#6990</a></li>
<li>VTGate: Allow time_zone in reserved connection <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6998">#6998</a></li>
<li>VTGate: Improved support for UNION <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7007">#7007</a></li>
<li>VTGate: Add DDL parser support for FULLTEXT indexes. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7001">#7001</a></li>
<li>VTGate: Extend comparability of EvalResult to support hash codes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7016">#7016</a></li>
<li>VTGate: Use proto equal method <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7017">#7017</a></li>
<li>VTGate: Fix COM_STMT_EXECUTE packet decode <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7020">#7020</a></li>
<li>VTGate: Adds Planning and Parsing Support for Create Index of MySQL 5.7 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7024">#7024</a></li>
<li>VTGate: UNION DISTINCT support on vtgate <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7029">#7029</a></li>
<li>VTGate: Improve database ddl plan <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7034">#7034</a></li>
<li>VTGate: Support for hex &amp; shard in vindex query <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7044">#7044</a></li>
<li>VTGate: Use distinct primitive to solve more queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7047">#7047</a></li>
<li>VTGate: Route using vindex for composite IN clause <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7049">#7049</a></li>
<li>VTGate: Optimise struct field layout <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7052">#7052</a></li>
<li>VTGate: Refactoring of plan building <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7054">#7054</a></li>
<li>VTGate: Rewrite joins written with the USING construct <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6660">#6660</a></li>
<li>VTGate: Add option to GetSchema to only send the row count and data length over the wire<br />
<a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6985">#6985</a></li>
<li>VTGate: Adds Planning and Parsing Support for Create Database of MySQL 5.7 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7068">#7068</a></li>
<li>VTGate: Make sure to check all GROUP BY columns <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7080">#7080</a></li>
<li>VTGate: Separate sub-query and derived table into different structs <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7081">#7081</a></li>
<li>VTGate: Adds Planning and Parsing Support for Alter Database of MySQL 5.7 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7086">#7086</a></li>
<li>VTGate: Convert usages of DDL struct to DDLStatement interface <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7096">#7096</a></li>
<li>VTGate: Adds Planning and Parsing Support for Drop Database of MySQL 5.7 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7098">#7098</a></li>
<li>VTGate: Restore SHOW SCHEMAS support; fixes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/issues/7100">#7100</a> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7102">#7102</a></li>
<li>VTGate: Refactor Code to create a separate struct for CREATE TABLE <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7116">#7116</a></li>
<li>VTGate: Allows for vttestserver and vtcombo to respond to VtGateExecute. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7121">#7121</a></li>
<li>VTGate: Support for lock and unlock tables <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7139">#7139</a></li>
<li>VTGate: Merge SelectDBA routes when possible <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7140">#7140</a></li>
<li>VTGate: Adds support for all the rails queries using information_schema <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7143">#7143</a></li>
<li>VTGate: Add support for unary expression in order by column <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7163">#7163</a></li>
<li>VTGate: Skip query rewriting for dual table <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7164">#7164</a></li>
<li>VTGate: Refactor Code to create a separate struct for ALTER VSCHEMA <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7173">#7173</a></li>
<li>VTGate: Refactor Show plans <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7185">#7185</a></li>
<li>VTGate: Show privilege support <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7194">#7194</a></li>
<li>VTGate: Planning and Parsing Support for Drop Table, Drop View and Alter View <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7178">#7178</a></li>
<li>VTGate: Cache only dml and select plans <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7196">#7196</a></li>
<li>VTGate: Planning and Parsing Support for Alter Table <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7199">#7199</a></li>
<li>VTGate: Add FindAllShardsInKeyspace to vtctldserver <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7201">#7201</a></li>
<li>VTGate: improve-log: FAILED_PRECONDITION <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7215">#7215</a></li>
<li>VTGate: Planner refactoring <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7103">#7103</a></li>
<li>VTGate: Migrate <code>vtctlclient InitShardMaster</code> =&gt; <code>vtctldclient InitShardPrimary</code> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7220">#7220</a></li>
<li>VTGate: Add Planning and Parsing Support for Truncate, Rename, Drop Index and Flush <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7242">#7242</a></li>
<li>VTGate: Fix create table format function to include if not exists <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7250">#7250</a></li>
<li>VTGate: Added default databases when calling 'show databases' <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7256">#7256</a></li>
<li>VTGate : Add Update.AddWhere to mirror Select.AddWhere <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7277">#7277</a></li>
<li>VTGate :Rremoved resolver usage from StreamExecute <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7281">#7281</a></li>
<li>VTGate: Adding a MySQL connection at Vtgate to run queries on it directly in case of testing mode <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7291">#7291</a></li>
<li>VTGate: Added vitess_version as variable <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7295">#7295</a></li>
<li>VTGate: Default to false for system settings to be changed per session at the database connection level <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7299">#7299</a></li>
<li>VTGate: Gen4: Add Limit clause support <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7312">#7312</a></li>
<li>VTGate: Gen4: Handling subquery in query graph <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7313">#7313</a></li>
<li>VTGate: Addition of @@enable_system_settings <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7300">#7300</a></li>
<li>VTGate: Route INFORMATION_SCHEMA queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6932">#6932</a></li>
<li>VTGate: Adds Planning and Parsing Support for Create Index of MySQL 5.7 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7024">#7024</a></li>
<li>VTGate: Log sql which exceeds max memory rows <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7055">#7055</a></li>
<li>VTExplain: Add sequence table support for vtexplain <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7186">#7186</a></li>
<li>VSchema: Support back-quoted names <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7073">#7073</a></li>
<li>Healthcheck: healthy list should be recomputed when a tablet is removed <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7176">#7176</a></li>
</ul>
<h3>Set Statement Support</h3>
<p>Set statement support has been added in Vitess. There are <a href="https://github.com/vitessio/vitess/blob/master/go/vt/sysvars/sysvars.go#L147,L190">some system variables</a> which are disabled by default and can be enabled using flag <code>-enable_system_settings</code> on VTGate. These system variables are set on the mysql server. Because they change the mysql session, using them leads to the Vitess connection no longer using the connection pool and forcing dedicated connections.</p>
<h3>VReplication</h3>
<ul>
<li>VReplication: refactored and enhanced support for JSON columns <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6829">#6829</a></li>
<li>VReplication: Don't update tx timestamp on heartbeat <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6930">#6930</a></li>
<li>VReplication E2E Tests: Refactored tests for readability and attempting to fix flakiness <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6991">#6991</a></li>
<li>VRepl/Tablet Picker: improve observability of selected tablet <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6999">#6999</a></li>
<li>VReplication: Handle comment statement type in vstreamer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7092">#7092</a></li>
<li>VReplication e2e: Fine tuned test to reduce flakiness and added more logging to debug future flakiness <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7138">#7138</a></li>
<li>VReplication: Make relay log size &amp; rows configurable. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6992">#6992</a></li>
<li>VReplication: New workflows cli UX. Allow reads/writes to be switched independently <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7071">#7071</a></li>
<li>VReplication: DropSources: change table rename logic <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7230">#7230</a></li>
<li>VReplication: MoveTables: delete routing rules and update vschema on Complete and Abort <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7234">#7234</a></li>
<li>VReplication: V2 Workflow Start: wait for streams to start and report errors if any while starting a workflow <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7248">#7248</a></li>
<li>VReplication: Ignore temp tables created by onlineddl <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7159">#7159</a></li>
<li>VReplication V2 Workflows: rename Abort to Cancel <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7276">#7276</a></li>
<li>VReplication DryRun: Report current dry run results for v2 commands <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7255">#7255</a></li>
<li>VReplication: Miscellaneous improvements <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7275">#7275</a></li>
<li>VReplication: Tablet throttle support "/throttle/check-self" available on all tablets <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7319">#7319</a></li>
<li>VStreamer Events: remove preceding zeroes from decimals in Row Events <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7297">#7297</a></li>
<li>Workflow Show: use timeUpdated to calculate vreplication lag <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7342">#7342</a></li>
<li>vtctl: Add missing err checks for VReplication v2 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7361">#7361</a></li>
<li>VStreamer Field Event: add allowed values for set/enum <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6981">#6981</a></li>
<li>VDiff: lock keyspace while snapshoting, restart target in case of errors <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7012">#7012</a></li>
<li>[vtctld]: fix error state in Workflow Show <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6970">#6970</a></li>
<li>[vtctld] Workflow command: minor fixes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7008">#7008</a></li>
<li>[vtctl] Add missing err checks for VReplication v2 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7361">#7361</a></li>
</ul>
<h3>VTTablet</h3>
<ul>
<li>VTTablet: fast and reliable state transitions <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7011">#7011</a></li>
<li>VTTablet: don't shutdown on too many connections <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7039">#7039</a></li>
<li>VTTablet: debug/env page to change variables in real-time <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7189">#7189</a></li>
<li>VTTablet: Adds better errors when there are timeouts in resource pools <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7002">#7002</a></li>
<li>VTTablet: Return to re-using server IDs for binlog connections <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6941">#6941</a></li>
<li>VTTablet: Correctly initialize the TabletType stats <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6989">#6989</a></li>
<li>Backup: Use provided xtrabackup_root_path to find xbstream <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7359">#7359</a></li>
<li>Backup: Use pargzip instead of pgzip for compression. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7037">#7037</a></li>
<li>Backup: Add s3 server-side encryption and decryption with customer provided key <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7088">#7088</a></li>
</ul>
<h3>OnlineDDL</h3>
<ul>
<li>Online DDL: follow ups in multiple trajectories <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6901">#6901</a></li>
<li>Online DDL: cancel running migrations executed by another tablet <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7006">#7006</a></li>
<li>OnlineDDL: Adding <code>ddl_strategy</code> session variable <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7042">#7042</a></li>
<li>Online DDL: ddl_strategy session variable and vtctl command line argument <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7045">#7045</a></li>
<li>Online DDL:  Removing online ddl query hint from ALTER TABLE <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7069">#7069</a></li>
<li>Online DDL: vtgate -ddl-strategy flag renamed to -ddl_strategy <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7074">#7074</a><br />
Automatically retry migration that was interrupted during master failover<br />
Automatically terminate migrations run by a failed tablet</li>
<li>Online DDL:request_context/migration_context <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7082">#7082</a></li>
<li>Online DDL: Support CREATE, DROP statements in ApplySchema and online DDL <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7083">#7083</a></li>
<li>Online DDL: ddl_type column <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7097">#7097</a></li>
<li>OnlineDDL: "cancel-all" command to cancel all pending migrations in keyspace <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7099">#7099</a></li>
<li>OnlineDDL: Support <code>vtctl OnlineDDL &lt;keyspace&gt; show &lt;context&gt;</code> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7145">#7145</a></li>
<li>OnlineDDL: Normalizing Online-DDL queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7153">#7153</a></li>
<li>Online DDL: ddl_strategy=direct <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7172">#7172</a></li>
<li>Online DDL: Executor database pool size increase <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7206">#7206</a></li>
<li>Online DDL: DROP TABLE translated to RENAME TABLE statement <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7221">#7221</a></li>
<li>Online DDL: Adding @@session_uuid to vtgate; used as 'context' <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7263">#7263</a></li>
<li>Online DDL: ignore errors if extracted gh-ost binary is identical to installed binary <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6928">#6928</a></li>
<li>Online DDL: Table lifecycle: skip time hint for unspecified states <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7151">#7151</a></li>
</ul>
<h3>VTadmin</h3>
<ul>
<li>VTadmin: Initial vtadmin-api, clusters, and service discovery <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7187">#7187</a></li>
<li>VTadmin: The tiniest possible first implementation of vtadmin-web <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7218">#7218</a></li>
<li>VTadmin: Add cluster protos to discovery and vtsql package constructors <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7224">#7224</a></li>
<li>VTadmin: Add static file service discovery implementation <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7229">#7229</a></li>
<li>VTadmin: Query vtadmin-api from vtadmin-web with fetch + react-query <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7239">#7239</a></li>
<li>VTadmin: Add vtctld proxy to vtadmin API, add GetKeyspaces endpoint <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7266">#7266</a></li>
<li>VTadmin: [vtctld] Expose vtctld gRPC port in local Docker example + update VTAdmin README <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7306">#7306</a></li>
<li>VTadmin: Add CSS variables + fonts to VTAdmin <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7309">#7309</a></li>
<li>VTadmin: Add React Router + a skeleton /debug page to VTAdmin <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7310">#7310</a></li>
<li>VTadmin: Add NavRail component <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7316">#7316</a></li>
<li>VTadmin: Add Button + Icon components <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7350">#7350</a></li>
<li>[vtctld]:  vtctldclient generator <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7238">#7238</a></li>
<li>[vtctld] Migrate cell getters <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7302">#7302</a></li>
<li>[vtctld] Migrate tablet getters <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7311">#7311</a></li>
<li>[vtctld] Migrate GetSchema <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7346">#7346</a></li>
<li>[vtctld] vtctldclient command pkg <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7321">#7321</a></li>
<li>[vtctld] Add GetSrvVSchema command <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7334">#7334</a></li>
<li>[vtctld] Migrate ListBackups as GetBackups in new vtctld server <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7352">#7352</a><br />
Merged</li>
<li>[vtctld] Migrate GetVSchema to VtctldServer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7360">#7360</a></li>
</ul>
<h3>Other</h3>
<ul>
<li>Fix comment typo <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6974">#6974</a></li>
<li>Fix all occurrences of <code>fmt.Sprint(x)</code> where x is <code>int</code> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7244">#7244</a></li>
<li>Fix incorrect comments <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7257">#7257</a></li>
<li>Fix comment for IDPool <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7212">#7212</a></li>
<li>IsInternalOperationTableName: see if a table is used internally by vitess <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7104">#7104</a></li>
</ul>
<h2>Examples / Tutorials</h2>
<ul>
<li>Update demo <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7205">#7205</a></li>
<li>Delete select_commerce_data.sql <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7245">#7245</a></li>
<li>Docker/vttestserver: Add MYSQL_BIND_HOST env <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7293">#7293</a></li>
<li>Examples/operator: fix tags and add vtorc example <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7358">#7358</a></li>
<li>local docker: copy examples/common into /vt/common to match MoveTables user guide <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7252">#7252</a></li>
<li>Update docker-compose examples to take advantage of improvements in Vitess <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7009">#7009</a></li>
</ul>
<h2>Documentation</h2>
<ul>
<li>Vitess Slack Guidelines v1.0 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6961">#6961</a></li>
<li>Do vschema_customer_sharded.json before create_customer_sharded.sql <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7210">#7210</a></li>
<li>Added readme for the demo example <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7226">#7226</a></li>
<li>Pull Request template: link to contribution guide <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7314">#7314</a></li>
</ul>
<h2>Build Environment Changes</h2>
<ul>
<li>Clean up plan building test cases <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7057">#7057</a></li>
<li>Fix unit test error <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6953">#6953</a>, <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6993">#6993</a></li>
<li>Fixing the 5.6 builds of vitess/lite <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6960">#6960</a></li>
<li>Pin mariadb to use mariadb-server-10.2 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6966">#6966</a></li>
<li>Replace vitess:base with vitess:lite images for docker-compose services <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7004">#7004</a></li>
<li>Fix flakey TestParallelRunnerApprovalFirstRunningSecondRunning test <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7014">#7014</a></li>
<li>Allow custom image tags in compose <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7043">#7043</a></li>
<li>Support statsd for vitess <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7072">#7072</a></li>
<li>Add vtctl to make install-local <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7125">#7125</a></li>
<li>Updating Java unit tests for JDK9+ compatibility <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7144">#7144</a></li>
<li>Add Go Version to Bootstrap Image <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7182">#7182</a></li>
<li>Update Vitess v8.0 images <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7174">#7174</a></li>
<li>Fix broken package ref in UBI docker build <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7183">#7183</a></li>
<li>Convert CentOS extra packages installation to yum instead of downloading <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7188">#7188</a></li>
<li>Make docker_local: fix missing mysql_server package <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7213">#7213</a></li>
<li>Add unit test case to improve test coverage for go/sqltypes/result.go <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7227">#7227</a></li>
<li>Update Golang to 1.15 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7204">#7204</a></li>
<li>Add linter configuration <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7247">#7247</a></li>
<li>Tracking failed check runs <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7026">#7026</a></li>
<li>Github Actions CI Builds: convert matrix strategy for unit and cluster tests to individual tests <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7258">#7258</a></li>
<li>Add Update.AddWhere to mirror Select.AddWhere <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7277">#7277</a></li>
<li>Descriptive names for CI checks <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7289">#7289</a></li>
<li>Testing upgrade path from / downgrade path to v8.0.0 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7294">#7294</a></li>
<li>Add mysqlctl to docker images <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7326">#7326</a></li>
</ul>
<h2>Functionality Neutral Changes</h2>
<ul>
<li>Healthcheck: add unit test for multi-cell replica configurations <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6978">#6978</a></li>
<li>Adds timeout to checking for tablets. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7106">#7106</a></li>
<li>Remove deprecated vtctl commands, flags and vttablet rpcs <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7115">#7115</a></li>
<li>Fixes comment to mention the existence of reference tables. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7122">#7122</a></li>
<li>Updated pull request template to add more clarity <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7193">#7193</a></li>
<li>Redact password <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7198">#7198</a></li>
<li>action_repository: no need for http.Request <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7124">#7124</a></li>
<li>Testing version upgrade/downgrade path from/to 8.0 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7323">#7323</a></li>
<li>Use <code>context</code> from Go's standard library <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7235">#7235</a></li>
</ul>

## Vitess 9.0.0-rc1
<p style="font-size:12px;"> 07, Jan 2021 
<a href="https://github.com/vitessio/vitess/releases/tag/v9.0.0-rc1" target="_blank"> 
Source </a><OutboundLink /></p>
<p>This release complies with VEP-3 which removes the upgrade order requirement. Components can be upgraded in any order. It is recommended that the upgrade order should still be followed if possible, except to canary test the new version of VTGate before upgrading the rest of the components.</p>
<h2>Incompatible Changes</h2>
<p>The following PRs made changes to behaviors that clients might rely on. They should be reviewed carefully so that client code can be changed in concert with a Vitess release deployment.</p>
<ul>
<li>The update to golang 1.15 might break systems that use TLS certificates with a common name. A fix is documented here (<a class="issue-link js-issue-link" href="https://github.com/golang/go/issues/40748#issuecomment-673612108">golang/go#40748 (comment)</a>)</li>
</ul>
<h2>Bugs Fixed</h2>
<ul>
<li>Set Global <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6957">#6957</a></li>
<li>Binary PK: fix bug where padding of binary columns was being done incorrectly <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6963">#6963</a></li>
<li>Set udv allow more expressions <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6964">#6964</a></li>
<li>Pad non-fractional part of DECIMAL type <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6967">#6967</a></li>
<li>Bug which caused the connection to not close in case of error writing an error packet <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6976">#6976</a></li>
<li>Bug which caused the connection to not close in case of error writing an error packet <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6977">#6977</a></li>
<li>Bug fix <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/issues/7048">#7048</a> for SelectNone in StreamExecute route engine <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7050">#7050</a></li>
<li>Bug fix regression in /healthz <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7090">#7090</a></li>
<li>Fix metadata related operation hang when zk down <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7228">#7228</a></li>
</ul>
<h2>Functionality Added or Changed</h2>
<ul>
<li>Vtctld: fix error state in Workflow Show <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6970">#6970</a></li>
<li>Adds better error when there are timeouts in resource pools <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7002">#7002</a></li>
<li>Backup: Use pargzip instead of pgzip for compression. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7037">#7037</a></li>
<li>Vschema: Support back-quoted names <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7073">#7073</a></li>
<li>IsInternalOperationTableName: see if a table is used internally by vitess <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7104">#7104</a></li>
<li>Log sql which exceeds max memory rows <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7055">#7055</a></li>
<li>Add sequence table support for vtexplain <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7186">#7186</a></li>
<li>Vtctld:  vtctldclient generator <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7238">#7238</a></li>
</ul>
<h3>VTGate / MySQL compatibility</h3>
<ul>
<li>VTGate: Allow INSERT with all defaults <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6969">#6969</a></li>
<li>VTGate: Allow YEAR column type with length specified <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6975">#6975</a></li>
<li>VTGate: Retry Execute when reserved connection is lost <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6983">#6983</a></li>
<li>VTGate: Use ephemeral buffer when reading rows <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6990">#6990</a></li>
<li>VTGate: Allow time_zone in reserved connection <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6998">#6998</a></li>
<li>VTGate: Improved support for UNION <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7007">#7007</a></li>
<li>VTGate: Add DDL parser support for FULLTEXT indexes. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7001">#7001</a></li>
<li>VTGate: Extend comparability of EvalResult to support hash codes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7016">#7016</a></li>
<li>VTGate: Use proto equal method <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7017">#7017</a></li>
<li>VTGate: Fix COM_STMT_EXECUTE packet decode <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7020">#7020</a></li>
<li>VTGate: Adds Planning and Parsing Support for Create Index of MySQL 5.7 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7024">#7024</a></li>
<li>VTGate: UNION DISTINCT support on vtgate <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7029">#7029</a></li>
<li>VTGate: Improve database ddl plan <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7034">#7034</a></li>
<li>VTGate: Support for hex &amp; shard in vindex query <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7044">#7044</a></li>
<li>VTGate: Use distinct primitive to solve more queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7047">#7047</a></li>
<li>VTGate: Route using vindex for composite IN clause <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7049">#7049</a></li>
<li>VTGate: Optimise struct field layout <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7052">#7052</a></li>
<li>VTGate: Refactoring of plan building <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7054">#7054</a></li>
<li>VTGate: Rewrite joins written with the USING construct <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6660">#6660</a></li>
<li>VTGate: Add option to GetSchema to only send the row count and data length over the wire <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6985">#6985</a></li>
<li>VTGate: Adds Planning and Parsing Support for Create Database of MySQL 5.7 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7068">#7068</a></li>
<li>VTGate: Make sure to check all GROUP BY columns <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7080">#7080</a></li>
<li>VTGate: Separate sub-query and derived table into different structs <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7081">#7081</a></li>
<li>VTGate: Adds Planning and Parsing Support for Alter Database of MySQL 5.7 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7086">#7086</a></li>
<li>VTGate: Convert usages of DDL struct to DDLStatement interface <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7096">#7096</a></li>
<li>VTGate: Adds Planning and Parsing Support for Drop Database of MySQL 5.7 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7098">#7098</a></li>
<li>VTGate: Restore SHOW SCHEMAS support; fixes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/issues/7100">#7100</a> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7102">#7102</a></li>
<li>VTGate: Refactor Code to create a separate struct for CREATE TABLE <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7116">#7116</a></li>
<li>VTGate: Allows for vttestserver and vtcombo to respond to VtGateExecute. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7121">#7121</a></li>
<li>VTGate: Support for lock and unlock tables <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7139">#7139</a></li>
<li>VTGate: Merge SelectDBA routes when possible <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7140">#7140</a></li>
<li>VTGate: Adds support for all the rails queries using information_schema <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7143">#7143</a></li>
<li>VTGate: Add support for unary expression in order by column <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7163">#7163</a></li>
<li>VTGate: Skip query rewriting for dual table <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7164">#7164</a></li>
<li>VTGate: Refactor Code to create a separate struct for ALTER VSCHEMA <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7173">#7173</a></li>
<li>VTGate: Refactor Show plans <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7185">#7185</a></li>
<li>VTGate: Show privilege support <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7194">#7194</a></li>
<li>VTGate: Planning and Parsing Support for Drop Table, Drop View and Alter View <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7178">#7178</a></li>
<li>VTGate: Cache only dml and select plans <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7196">#7196</a></li>
<li>VTGate: Planning and Parsing Support for Alter Table <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7199">#7199</a></li>
<li>VTGate: Add FindAllShardsInKeyspace to vtctldserver <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7201">#7201</a></li>
<li>VTGate: improve-log: FAILED_PRECONDITION <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7215">#7215</a></li>
</ul>
<h3>VReplication</h3>
<ul>
<li>VReplication: refactored and enhanced support for JSON columns <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6829">#6829</a></li>
<li>VReplication: Don't update tx timestamp on heartbeat <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6930">#6930</a></li>
<li>VReplication E2E Tests: Refactored tests for readability and attempting to fix flakiness <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6991">#6991</a></li>
<li>VRepl/Tablet Picker: improve observability of selected tablet <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6999">#6999</a></li>
<li>VReplication: Handle comment statement type in vstreamer <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7092">#7092</a></li>
<li>VReplication e2e: Fine tuned test to reduce flakiness and added more logging to debug future flakiness <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7138">#7138</a></li>
<li>VReplication: Make relay log size &amp; rows configurable. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6992">#6992</a></li>
<li>VReplication: New workflows cli UX. Allow reads/writes to be switched independently <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7071">#7071</a></li>
<li>VReplication: DropSources: change table rename logic <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7230">#7230</a></li>
<li>VReplication: MoveTables: delete routing rules and update vschema on Complete and Abort <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7234">#7234</a></li>
<li>VReplication: V2 Workflow Start: wait for streams to start and report errors if any while starting a workflow <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7248">#7248</a></li>
</ul>
<h3>VTtablet</h3>
<ul>
<li>VTtablet: ignore errors if extracted gh-ost binary is identical to installed binary <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6928">#6928</a></li>
<li>VTtablet: fast and reliable state transitions <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7011">#7011</a></li>
<li>VTtablet: don't shutdown on too many connections <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7039">#7039</a></li>
<li>VTtablet: debug/env page to change variables in real-time <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7189">#7189</a></li>
</ul>
<h3>VStreamer</h3>
<ul>
<li>VStreamer Field Event: add allowed values for set/enum <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6981">#6981</a></li>
</ul>
<h3>VDiff</h3>
<ul>
<li>VDiff: lock keyspace while snapshoting, restart target in case of errors <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7012">#7012</a></li>
</ul>
<h3>OnlineDDL</h3>
<ul>
<li>Online DDL: follow ups in multiple trajectories <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6901">#6901</a></li>
<li>Online DDL: cancel running migrations executed by another tablet <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7006">#7006</a></li>
<li>OnlineDDL: Adding <code>ddl_strategy</code> session variable <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7042">#7042</a></li>
<li>Online DDL: ddl_strategy session variable and vtctl command line argument <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7045">#7045</a></li>
<li>Online DDL:  Removing online ddl query hint from ALTER TABLE <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7069">#7069</a></li>
<li>Online DDL: vtgate -ddl-strategy flag renamed to -ddl_strategy <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7074">#7074</a><br />
Automatically retry migration that was interrupted during master failover<br />
Automatically terminate migrations run by a failed tablet</li>
<li>Online DDL:request_context/migration_context <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7082">#7082</a></li>
<li>Online DDL: Support CREATE, DROP statements in ApplySchema and online DDL <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7083">#7083</a></li>
<li>Online DDL: ddl_type column <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7097">#7097</a></li>
<li>OnlineDDL: "cancel-all" command to cancel all pending migrations in keyspace <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7099">#7099</a></li>
<li>OnlineDDL: Support <code>vtctl OnlineDDL &lt;keyspace&gt; show &lt;context&gt;</code> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7145">#7145</a></li>
<li>OnlineDDL: Normalizing Online-DDL queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7153">#7153</a></li>
<li>Online DDL: ddl_strategy=direct <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7172">#7172</a></li>
<li>Online DDL: Executor database pool size increase <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7206">#7206</a></li>
<li>Online DDL: DROP TABLE translated to RENAME TABLE statement <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7221">#7221</a></li>
<li>Online DDL: Adding @@session_uuid to vtgate; used as 'context' <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7263">#7263</a></li>
</ul>
<h3>VTadmin</h3>
<ul>
<li>VTadmin: Initial vtadmin-api, clusters, and service discovery <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7187">#7187</a></li>
<li>VTadmin: The tiniest possible first implementation of vtadmin-web <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7218">#7218</a></li>
<li>VTadmin: Add cluster protos to discovery and vtsql package constructors <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7224">#7224</a></li>
<li>VTadmin: Add static file service discovery implementation <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7229">#7229</a></li>
<li>VTadmin: Query vtadmin-api from vtadmin-web with fetch + react-query <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7239">#7239</a></li>
</ul>
<h3>Other</h3>
<ul>
<li>Route INFORMATION_SCHEMA queries <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6932">#6932</a></li>
<li>Return to re-using server IDs for binlog connections <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6941">#6941</a></li>
<li>Fix comment typo <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6974">#6974</a></li>
<li>Correctly initialize the TabletType stats <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6989">#6989</a></li>
<li>Clean up plan building test cases <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7057">#7057</a></li>
<li>Add s3 server-side encryption and decryption with customer provided key <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7088">#7088</a></li>
<li>Fix all occurrences of <code>fmt.Sprint(x)</code> where x is <code>int</code> <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7244">#7244</a></li>
<li>local docker: copy examples/common into /vt/common to match MoveTables user guide <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7252">#7252</a></li>
<li>Fix incorrect comments <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7257">#7257</a></li>
</ul>
<h2>Examples / Tutorials</h2>
<ul>
<li></li>
</ul>
<h2>Documentation</h2>
<ul>
<li>Vitess Slack Guidelines v1.0 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6961">#6961</a></li>
<li>Update docker-compose examples to take advantage of improvements in Vitess <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7009">#7009</a></li>
<li>Adds Planning and Parsing Support for Create Index of MySQL 5.7 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7024">#7024</a></li>
<li>Do vschema_customer_sharded.json before create_customer_sharded.sql <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7210">#7210</a></li>
<li>Fix comment for IDPool <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7212">#7212</a></li>
<li>Added readme for the demo example <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7226">#7226</a></li>
</ul>
<h2>Build Environment Changes</h2>
<ul>
<li>Fix unit test error <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6953">#6953</a>, <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6993">#6993</a></li>
<li>Fixing the 5.6 builds of vitess/lite <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6960">#6960</a></li>
<li>Set udv allow more expressions <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6964">#6964</a></li>
<li>Pin mariadb to use mariadb-server-10.2 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6966">#6966</a></li>
<li>Replace vitess:base with vitess:lite images for docker-compose services <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7004">#7004</a></li>
<li>Fix flakey TestParallelRunnerApprovalFirstRunningSecondRunning test <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7014">#7014</a></li>
<li>Allow custom image tags in compose <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7043">#7043</a></li>
<li>Support statsd for vitess <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7072">#7072</a></li>
<li>Add vtctl to make install-local <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7125">#7125</a></li>
<li>Updating Java unit tests for JDK9+ compatibility <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7144">#7144</a></li>
<li>Add Go Version to Bootstrap Image <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7182">#7182</a></li>
<li>Update Vitess v8.0 images <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7174">#7174</a></li>
<li>Fix broken package ref in UBI docker build <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7183">#7183</a></li>
<li>Convert CentOS extra packages installation to yum instead of downloading <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7188">#7188</a></li>
<li>Make docker_local: fix missing mysql_server package <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7213">#7213</a></li>
<li>Add unit test case to improve test coverage for go/sqltypes/result.go <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7227">#7227</a></li>
<li>Use <code>context</code> from Go's standard library <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7235">#7235</a></li>
<li>Update Golang to 1.15 <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7204">#7204</a></li>
<li>Add linter configuration <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7247">#7247</a></li>
</ul>
<h2>Functionality Neutral Changes</h2>
<ul>
<li>Healthcheck: add unit test for multi-cell replica configurations <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/6978">#6978</a></li>
<li>Healthcheck: healthy list should be recomputed when a tablet is removed <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7176">#7176</a></li>
<li>Vtctld Workflow command: minor fixes <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7008">#7008</a></li>
<li>Adds timeout to checking for tablets. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7106">#7106</a></li>
<li>Remove deprecated vtctl commands, flags and vttablet rpcs <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7115">#7115</a></li>
<li>Fixes comment to mention the existence of reference tables. <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7122">#7122</a></li>
<li>Updated pull request template to add more clarity <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7193">#7193</a></li>
<li>Redact password <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7198">#7198</a></li>
<li>action_repository: no need for http.Request <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7124">#7124</a></li>
<li>Table lifecycle: skip time hint for unspecified states <a class="issue-link js-issue-link" href="https://github.com/vitessio/vitess/pull/7151">#7151</a></li>
</ul>
