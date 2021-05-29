# Helm

<div>
<demo-component app-code="helm"/>
</div>


## Helm v3.6.0
<p style="font-size:12px;"> 27, May 2021 
<a href="https://github.com/helm/helm/releases/tag/v3.6.0" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Helm v3.6.0 is a feature release. Users are encouraged to upgrade for the best experience.</p>
<p>The community keeps growing, and we'd love to see you there!</p>
<ul>
<li>Join the discussion in <a href="https://kubernetes.slack.com" rel="nofollow">Kubernetes Slack</a>:
<ul>
<li>for questions and just to hang out</li>
<li>for discussing PRs, code, and bugs</li>
</ul>
</li>
<li>Hang out at the Public Developer Call: Thursday, 9:30 Pacific via <a href="https://zoom.us/j/696660622" rel="nofollow">Zoom</a></li>
<li>Test, debug, and contribute charts: <a href="https://artifacthub.io/packages/search?kind=0" rel="nofollow">ArtifactHub/packages</a></li>
</ul>
<h2>Notable Changes</h2>
<ul>
<li>Apple silicon support</li>
<li>Continued OCI changes as the experiment is refined</li>
<li>Improved auto-completion</li>
<li>Helm create ingress updates</li>
</ul>
<h2>Installation and Upgrading</h2>
<p>Download Helm v3.6.0. The common platform binaries are here:</p>
<ul>
<li><a href="https://get.helm.sh/helm-v3.6.0-darwin-amd64.tar.gz" rel="nofollow">MacOS amd64</a> (<a href="https://get.helm.sh/helm-v3.6.0-darwin-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 7f6bcf15e5c828504dddbe733813a6d73e41abf28d649e7b9d698c4a77d412dd)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-darwin-arm64.tar.gz" rel="nofollow">MacOS arm64</a> (<a href="https://get.helm.sh/helm-v3.6.0-darwin-arm64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 7d49924d0badcf081370e129448f62dd6f33878fc5812ee87fea7ef4de4ae19c)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-linux-amd64.tar.gz" rel="nofollow">Linux amd64</a> (<a href="https://get.helm.sh/helm-v3.6.0-linux-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 0a9c80b0f211791d6a9d36022abd0d6fd125139abe6d1dcf4c5bf3bc9dcec9c8)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-linux-arm.tar.gz" rel="nofollow">Linux arm</a> (<a href="https://get.helm.sh/helm-v3.6.0-linux-arm.tar.gz.sha256sum" rel="nofollow">checksum</a> / 75cda02e463a325152af6758817fac4b796e8da0ff974af30c82174edc2bd31b)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-linux-arm64.tar.gz" rel="nofollow">Linux arm64</a> (<a href="https://get.helm.sh/helm-v3.6.0-linux-arm64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 8a16f23866b1e74b347bcdd7f8731ebcfa37f35fc27c75dd29b13e87aed8484c)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-linux-386.tar.gz" rel="nofollow">Linux i386</a> (<a href="https://get.helm.sh/helm-v3.6.0-linux-386.tar.gz.sha256sum" rel="nofollow">checksum</a> / e7091d31f65ade88246229a2e4f5baad1dafb314946ceaf9a6441fc04dcc9ce2)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-linux-ppc64le.tar.gz" rel="nofollow">Linux ppc64le</a> (<a href="https://get.helm.sh/helm-v3.6.0-linux-ppc64le.tar.gz.sha256sum" rel="nofollow">checksum</a> / 9772a27bfc999d5c79c75d72c54adc6ce1686d983172f69efd3fbb19a5db54f2)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-linux-s390x.tar.gz" rel="nofollow">Linux s390x</a> (<a href="https://get.helm.sh/helm-v3.6.0-linux-s390x.tar.gz.sha256sum" rel="nofollow">checksum</a> / 007f38c2a99d7e8e07b45ca9d71cf9824071aa1492ed4c24ade9f99b5cce5074)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-windows-amd64.zip" rel="nofollow">Windows amd64</a> (<a href="https://get.helm.sh/helm-v3.6.0-windows-amd64.zip.sha256sum" rel="nofollow">checksum</a> / 4e2a5303c551d7836b289fa1869bf89f6d672fe8da078d25b45ede0fb3fffbfe)</li>
</ul>
<p>This release was signed with <code>672C 657B E06B 4B30 969C 4A57 4614 49C2 5E36 B98E </code> and can be found at <a class="user-mention" href="https://github.com/mattfarina">@mattfarina</a> <a href="https://keybase.io/mattfarina" rel="nofollow">keybase account</a>. Please use the attached signatures for verifying this release using <code>gpg</code>.</p>
<p>The <a href="https://helm.sh/docs/intro/quickstart/" rel="nofollow">Quickstart Guide</a> will get you going from there. For <strong>upgrade instructions</strong> or detailed installation notes, check the <a href="https://helm.sh/docs/intro/install/" rel="nofollow">install guide</a>. You can also use a <a href="https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3" rel="nofollow">script to install</a> on any system with <code>bash</code>.</p>
<h2>What's Next</h2>
<ul>
<li>3.6.1 will contain only bug fixes and is planned for release on July 14, 2021</li>
<li>3.7.0 is the next feature release and will be released on September 8, 2021.</li>
</ul>
<h2>Changelog</h2>
<ul>
<li>bump version to v3.6.0 <a class="commit-link" href="https://github.com/helm/helm/commit/7f2df6467771a75f5646b7f12afb408590ed1755"><tt>7f2df64</tt></a> (Matt Farina)</li>
<li>chore: update testdata to use the new ingress template <a class="commit-link" href="https://github.com/helm/helm/commit/d5b4e1c5b84b255b49a60f0647338ed5ac32b2d2"><tt>d5b4e1c</tt></a> (Mark Sagi-Kazar)</li>
<li>feat: add networking.k8s.io/v1 support to ingress template <a class="commit-link" href="https://github.com/helm/helm/commit/6d9e15bd1abcaae9938c73ed12a874d68fd32c56"><tt>6d9e15b</tt></a> (Mark Sagi-Kazar)</li>
<li>Moving myself to maintainer emeritus <a class="commit-link" href="https://github.com/helm/helm/commit/637a11dc0e6a59fb89535efff1617150ce5a4985"><tt>637a11d</tt></a> (Taylor Thomas)</li>
<li>upgrade to kubernetes 1.21 <a class="commit-link" href="https://github.com/helm/helm/commit/257a427866883a9fb745be40800ffe8e9ceda82b"><tt>257a427</tt></a> (shoubhik)</li>
<li>Fix capabilities changes leaking into other tests <a class="commit-link" href="https://github.com/helm/helm/commit/0156ca61ca6999bcfb093d210a4ee597aece0edf"><tt>0156ca6</tt></a> (Thomas Dy)</li>
<li>Add tests for template --kube-version <a class="commit-link" href="https://github.com/helm/helm/commit/538670fda63c027c64a592e29e156d950ef21c94"><tt>538670f</tt></a> (Thomas Dy)</li>
<li>feat(helm): Support setting --kube-version <a class="commit-link" href="https://github.com/helm/helm/commit/47c8f48f209f363807c8fb9f17ef072d7ae32139"><tt>47c8f48</tt></a> (Thomas Dy)</li>
<li>fix(ci) update ci to use main branch <a class="commit-link" href="https://github.com/helm/helm/commit/db2aa1a8d633756ec0814cf2f58889d8a767a9a1"><tt>db2aa1a</tt></a> (Adam Reese)</li>
<li>Update references to default branch name as it has changed to main <a class="commit-link" href="https://github.com/helm/helm/commit/734f93b2451207f613b032e03c32663a3feea516"><tt>734f93b</tt></a> (Martin Hickey)</li>
<li>Add ReadyChecker to decouple ready check logic from --wait <a class="commit-link" href="https://github.com/helm/helm/commit/98d98369ed9abcaec9b75352e07dd6f759a8804f"><tt>98d9836</tt></a> (Joe Lanford)</li>
<li>chore(deps): Bump github.com/deislabs/oras from v0.10.0 to v0.11.1 and drop replace <a class="commit-link" href="https://github.com/helm/helm/commit/f94e5bd0f8529c07148388ee5aa55f5abe3570cf"><tt>f94e5bd</tt></a> (Morlay)</li>
<li>Add/update deprecation notices <a class="commit-link" href="https://github.com/helm/helm/commit/c50372a8c1b948f3a140cb6c47e94ba1f0c8438a"><tt>c50372a</tt></a> (Simon Croome)</li>
<li>Wrap validation error instead of recreating <a class="commit-link" href="https://github.com/helm/helm/commit/6c82c83b3ab7f7664048f70c79b302cc6f7c1475"><tt>6c82c83</tt></a> (Simon Croome)</li>
<li>Move default to avoid nil check <a class="commit-link" href="https://github.com/helm/helm/commit/54de1c1f2549fb84db7f021c08cad6acd80ce7da"><tt>54de1c1</tt></a> (Simon Croome)</li>
<li>Add name validation rules for object kinds <a class="commit-link" href="https://github.com/helm/helm/commit/ba325bdf7e1165f312456dfc3e52b9b9cce338e4"><tt>ba325bd</tt></a> (Simon Croome)</li>
<li>Improve description for version flag. <a class="commit-link" href="https://github.com/helm/helm/commit/171321bb6cb51198bfb63cee5f82cbfea029409a"><tt>171321b</tt></a> (Daniel Petró)</li>
<li>chore: Spelling (<a class="issue-link js-issue-link" href="https://github.com/helm/helm/pull/9410">#9410</a>) <a class="commit-link" href="https://github.com/helm/helm/commit/2bf8fdf45d5efd676bec114ce0f917515c297b26"><tt>2bf8fdf</tt></a> (Josh Soref)</li>
<li>chore(deps): Bump k8s.io/klog/v2 from 2.5.0 to 2.8.0 <a class="commit-link" href="https://github.com/helm/helm/commit/113c8d972d982a9fdd713c6502e95f15e3944e30"><tt>113c8d9</tt></a> (dependabot[bot])</li>
<li>chore(deps): Bump github.com/containerd/containerd from 1.4.3 to 1.4.4 <a class="commit-link" href="https://github.com/helm/helm/commit/f3ccacae9b4a67b0a1e1017b6b858379c7bb5d80"><tt>f3ccaca</tt></a> (dependabot[bot])</li>
<li>chore(deps): Bump github.com/lib/pq from 1.9.0 to 1.10.0 <a class="commit-link" href="https://github.com/helm/helm/commit/56453f69bbb9b928598005e848d8f4adc9656088"><tt>56453f6</tt></a> (dependabot[bot])</li>
<li>Bump github.com/spf13/cobra from 1.1.1 to 1.1.3 <a class="commit-link" href="https://github.com/helm/helm/commit/60c399d7fb3cdc85aca66684b420dd4494d675eb"><tt>60c399d</tt></a> (dependabot[bot])</li>
<li>Cleanup mpodule dependencies <a class="commit-link" href="https://github.com/helm/helm/commit/4d39d47be5208b61921cb00e8b36e3557178c08b"><tt>4d39d47</tt></a> (Martin Hickey)</li>
<li>feat(comp): Uninstall accepts multiple releases <a class="commit-link" href="https://github.com/helm/helm/commit/8854547d3518cf3c83eec80d9390a05c453f4b3e"><tt>8854547</tt></a> (Marc Khouzam)</li>
<li>new key for technosophos (<a class="issue-link js-issue-link" href="https://github.com/helm/helm/pull/9478">#9478</a>) <a class="commit-link" href="https://github.com/helm/helm/commit/543364fba59b0c7c30e38ebe0f73680db895abb6"><tt>543364f</tt></a> (Matt Butcher)</li>
<li>chore(deps): Bump github.com/sirupsen/logrus from 1.7.0 to 1.8.1 <a class="commit-link" href="https://github.com/helm/helm/commit/4096cfb60fc0a4e66e709fa52ffec3813162e71e"><tt>4096cfb</tt></a> (dependabot[bot])</li>
<li>add flag trimpath in the go build command <a class="commit-link" href="https://github.com/helm/helm/commit/03eec30907819bcb5b157a4d73849774ed73ec0e"><tt>03eec30</tt></a> (pallavJha)</li>
<li>stick to 0.20.4 <a class="commit-link" href="https://github.com/helm/helm/commit/0befcef3780f09db97dbc7292108f2051477d942"><tt>0befcef</tt></a> (Shoubhik Bose)</li>
<li>updated unit tests to conform with helm best practices <a class="commit-link" href="https://github.com/helm/helm/commit/592c338242deba41df6c684e6260daccb93acfc7"><tt>592c338</tt></a> (Matthew Luckam)</li>
<li>corrected order of helm lint coalescing of multiple values files <a class="commit-link" href="https://github.com/helm/helm/commit/f4029944611ed0d18374408c8d504ab17ecde257"><tt>f402994</tt></a> (Matthew Luckam)</li>
<li>upgrade to v0.21.0-beta.0 <a class="commit-link" href="https://github.com/helm/helm/commit/44bec199beac8ec5e44f873d0075c2e383b01c88"><tt>44bec19</tt></a> (Shoubhik Bose)</li>
<li>Fix the example for --time-format flag <a class="commit-link" href="https://github.com/helm/helm/commit/30f643ce6791b35afeff6b220afeb399cfee54cc"><tt>30f643c</tt></a> (mert)</li>
<li>Use kube libraries v0.20.4 <a class="commit-link" href="https://github.com/helm/helm/commit/1cf1e549cb472ab9de97046a2610c8298d373db9"><tt>1cf1e54</tt></a> (Shoubhik Bose)</li>
<li>Added s390x support to get script <a class="commit-link" href="https://github.com/helm/helm/commit/1fc6f650cb06a593c141a3088c2c7b109aff5e73"><tt>1fc6f65</tt></a> (Ajay Victor)</li>
<li>add test to ensure OCIGetter registryClient is set <a class="commit-link" href="https://github.com/helm/helm/commit/1c377f8c6204983ca37e8b7b2048669dfbef8b9e"><tt>1c377f8</tt></a> (Alex Sears)</li>
<li>initialize registry client in oci getter <a class="commit-link" href="https://github.com/helm/helm/commit/2d16a8135b13cfe092501e72ecce3808bfb419f2"><tt>2d16a81</tt></a> (Alex Sears)</li>
<li>feat(comp): Add descriptions for output format <a class="commit-link" href="https://github.com/helm/helm/commit/593b267ed57d6e1e52312dbe8c2145529ef88416"><tt>593b267</tt></a> (Marc Khouzam)</li>
<li>feat(comp): Add descriptions for --version comp <a class="commit-link" href="https://github.com/helm/helm/commit/430709170a94ac754faf936d67121c1d69a30f0e"><tt>4307091</tt></a> (Marc Khouzam)</li>
<li>feat(comp): Add descriptions for revision comp <a class="commit-link" href="https://github.com/helm/helm/commit/9856f056d439c911c60e3f603327c82f9e2398ec"><tt>9856f05</tt></a> (Marc Khouzam)</li>
<li>feat(comp): Add descriptions for kube-context comp <a class="commit-link" href="https://github.com/helm/helm/commit/7dee24daaeb55b46ad6793c0e11eaece7d3c0b0a"><tt>7dee24d</tt></a> (Marc Khouzam)</li>
<li>feat(comp): Add descriptions for plugin completion <a class="commit-link" href="https://github.com/helm/helm/commit/b0d567accddbeefc697042eb24c4ac9bd9ba3264"><tt>b0d567a</tt></a> (Marc Khouzam)</li>
<li>feat(comp): Add descriptions for release name comp <a class="commit-link" href="https://github.com/helm/helm/commit/a6b28348df809c8e53793c91d2194571ac60d2a9"><tt>a6b2834</tt></a> (Marc Khouzam)</li>
<li>feat(comp): Improve completion for plugin commands <a class="commit-link" href="https://github.com/helm/helm/commit/1f68f658a5bd0c77e2d01c22c35c8db39decde63"><tt>1f68f65</tt></a> (Marc Khouzam)</li>
<li>fix(cmd): Show that flags can be used for zsh/fish <a class="commit-link" href="https://github.com/helm/helm/commit/7b6dcfae98527c3ff7233fc16cbeac782dd82977"><tt>7b6dcfa</tt></a> (Marc Khouzam)</li>
<li>use relative linking <a class="commit-link" href="https://github.com/helm/helm/commit/abadc5468487f7dcd47035afe8591634ad2ffde4"><tt>abadc54</tt></a> (Matthew Fisher)</li>
<li>formatting <a class="commit-link" href="https://github.com/helm/helm/commit/b704e84dd1136da9fad38e712bd3c580c8d969d8"><tt>b704e84</tt></a> (Matthew Fisher)</li>
<li>more words <a class="commit-link" href="https://github.com/helm/helm/commit/6cea2847bedbac299351b87bbf6f2b375fc24787"><tt>6cea284</tt></a> (Matthew Fisher)</li>
<li>keep it concise <a class="commit-link" href="https://github.com/helm/helm/commit/2c114125a88d46a908fe42a05b5707360c8ca57a"><tt>2c11412</tt></a> (Matthew Fisher)</li>
<li>docs(CONTRIBUTING): writing a HIP <a class="commit-link" href="https://github.com/helm/helm/commit/41707a6b71100b038aef7a74bcc992f8ba4088b6"><tt>41707a6</tt></a> (Matthew Fisher)</li>
<li>update test expectation for new template error string <a class="commit-link" href="https://github.com/helm/helm/commit/f57c01cd9365d7f50a7e3d69b8c75a687392e74c"><tt>f57c01c</tt></a> (Joe Lanford)</li>
<li>Add darwin/arm64 (Apple Silicon) support <a class="commit-link" href="https://github.com/helm/helm/commit/ecdc34c5abd1d0242294ec95190f13044bd67504"><tt>ecdc34c</tt></a> (Joe Lanford)</li>
<li>fix windows tests <a class="commit-link" href="https://github.com/helm/helm/commit/4f1ab5a331d99370ff7bbd1f2004fe80878fbdaf"><tt>4f1ab5a</tt></a> (Christian)</li>
<li>fix(test): Increase golangci-lint timeout <a class="commit-link" href="https://github.com/helm/helm/commit/8d33624520375f5c7d60b15e9ff24a59232f336f"><tt>8d33624</tt></a> (Marc Khouzam)</li>
<li>fix(helm): get/get-helm-3 whitespace support in runAsRoot <a class="commit-link" href="https://github.com/helm/helm/commit/784782013a11c5f1640fb454ec7b9ea0fbf2c389"><tt>7847820</tt></a> (Michael Musenbrock)</li>
<li>fix release sha256 <a class="commit-link" href="https://github.com/helm/helm/commit/24925c4ca384145706c59da8c5605177c4f0f31a"><tt>24925c4</tt></a> (houfangdong)</li>
<li>feat(comp): Completion for the docs --type flag <a class="commit-link" href="https://github.com/helm/helm/commit/3c4ccade13d7557be1bd0185056ee89e708b8d7f"><tt>3c4ccad</tt></a> (Marc Khouzam)</li>
<li>Bump github.com/jmoiron/sqlx from 1.2.0 to 1.3.1 <a class="commit-link" href="https://github.com/helm/helm/commit/74c49d49be16ea8842da9a9caaee38c5beb7a97f"><tt>74c49d4</tt></a> (dependabot[bot])</li>
<li>Updating golangci-lint to 1.36.0 <a class="commit-link" href="https://github.com/helm/helm/commit/1cf95890517d0c343cf0c366e67d16bb5150e70b"><tt>1cf9589</tt></a> (Matt Farina)</li>
<li>chore(go.mod): bump Masterminds/{spring,goutils} and deislabs/oras <a class="commit-link" href="https://github.com/helm/helm/commit/3dbb1614c94c96b34122c8ef788c1c899ff391d4"><tt>3dbb161</tt></a> (Adam Reese)</li>
<li>fix(*): Validate metadata semver and printable characters <a class="commit-link" href="https://github.com/helm/helm/commit/657ce552cb6e582976c08cccc9605e42c242084e"><tt>657ce55</tt></a> (Adam Reese)</li>
<li>Bump github.com/mitchellh/copystructure from 1.0.0 to 1.1.1 <a class="commit-link" href="https://github.com/helm/helm/commit/bb4286579413ebcffa759e768bc8f194372dcb19"><tt>bb42865</tt></a> (dependabot[bot])</li>
<li>closes <a class="issue-link js-issue-link" href="https://github.com/helm/helm/issues/9312">#9312</a> <a class="commit-link" href="https://github.com/helm/helm/commit/54410194a6380e82352dec63d1ab43a718243728"><tt>5441019</tt></a> (James McElwain)</li>
<li>Fix-9253: Change the deprecated charts repo URL in release notes <a class="commit-link" href="https://github.com/helm/helm/commit/64e2d596cf17688d4db1446c62255b07c755db64"><tt>64e2d59</tt></a> (Jack Whitter-Jones)</li>
<li>Fix <code>helm list --offset</code> cli help string <a class="commit-link" href="https://github.com/helm/helm/commit/f9200231813d1804038a602deb0f979ec60a56b8"><tt>f920023</tt></a> (Krish)</li>
<li>Define GPG_PUBRING to make pubring configurable <a class="commit-link" href="https://github.com/helm/helm/commit/03d1f3d9d9def8bc2b6bce4ebfa846895b6979bc"><tt>03d1f3d</tt></a> (Ma Xinjian)</li>
<li>Bump github.com/mattn/go-shellwords from 1.0.10 to 1.0.11 <a class="commit-link" href="https://github.com/helm/helm/commit/e8817d7a186749527406356e3a256b467961059b"><tt>e8817d7</tt></a> (dependabot[bot])</li>
<li>Bump k8s.io/klog/v2 from 2.4.0 to 2.5.0 <a class="commit-link" href="https://github.com/helm/helm/commit/59791a2753c70ddf0d164ab8771dc8176c040af9"><tt>59791a2</tt></a> (dependabot[bot])</li>
<li>Upgrade to oras v0.9.0 (<a class="issue-link js-issue-link" href="https://github.com/helm/helm/pull/9269">#9269</a>) <a class="commit-link" href="https://github.com/helm/helm/commit/0b2fec08ac2270a027fa3d9c216d269081c0b08d"><tt>0b2fec0</tt></a> (Josh Dolitsky)</li>
<li>use kube libraries v0.20.2 <a class="commit-link" href="https://github.com/helm/helm/commit/7e41f7005297260c65624db7126118c99931fdb1"><tt>7e41f70</tt></a> (Shoubhik Bose)</li>
<li>print warning message instead of debug message when ~/.config exists but is not accessible <a class="commit-link" href="https://github.com/helm/helm/commit/5cd2a93725efbee136e7298584a4d4ea0f722a1b"><tt>5cd2a93</tt></a> (wawa0210)</li>
<li>Update default ingress values section to correspond with template <a class="commit-link" href="https://github.com/helm/helm/commit/042567808f2f39d49a9ab9399797b7ffde05aee7"><tt>0425678</tt></a> (Nick Jones)</li>
<li>chore(Makefile): add target to generate golden files <a class="commit-link" href="https://github.com/helm/helm/commit/b4010b7782c4c15d15f3dc3299e62b42e86f11ea"><tt>b4010b7</tt></a> (Adam Reese)</li>
<li>Fix dep build with OCI based charts <a class="commit-link" href="https://github.com/helm/helm/commit/1135392b482f26f244c3c69f51511a1d82590eb7"><tt>1135392</tt></a> (Matt Farina)</li>
<li>Fix typo in comment <a class="commit-link" href="https://github.com/helm/helm/commit/fee2257e3493e9d06ca6caa4be7ef7660842cbdb"><tt>fee2257</tt></a> (Guangwen Feng)</li>
<li>bump version to <a class="commit-link" href="https://github.com/helm/helm/commit/8082f6db45d60663ee1540e36b067ae2cc75459e"><tt>8082f6d</tt></a> (Matt Farina)</li>
<li>fix(Makefile): rebuild the binary if go.mod has changed <a class="commit-link" href="https://github.com/helm/helm/commit/a58209dfa41d291c49dcb42b123b336c782356f3"><tt>a58209d</tt></a> (Adam Reese)</li>
<li>fix(pkg/storage): If storage.Create fails to clean up recent release versions, return an error <a class="commit-link" href="https://github.com/helm/helm/commit/00cf10d360de3fbe440789ee51662c2894e041ce"><tt>00cf10d</tt></a> (Daniel Lipovetsky)</li>
<li>test(pkg/storage): Verify that storage.Create returns an error if it fails to clean up least-recent release versions <a class="commit-link" href="https://github.com/helm/helm/commit/8c28da65676a190623ac1d10711780e58e574a04"><tt>8c28da6</tt></a> (Daniel Lipovetsky)</li>
<li>Bump github.com/containerd/containerd from 1.3.4 to 1.4.3 <a class="commit-link" href="https://github.com/helm/helm/commit/a9e23805692167d432a56cc30becf9ab83c2344b"><tt>a9e2380</tt></a> (dependabot[bot])</li>
<li>Improve the console output for resource policy keep to align with helm2. <a class="commit-link" href="https://github.com/helm/helm/commit/87040536fb7593873f8acffb320617a7baae09b0"><tt>8704053</tt></a> (Du Zheng)</li>
</ul>

## v3.6.0-rc.1
<p style="font-size:12px;"> 18, May 2021 
<a href="https://github.com/helm/helm/releases/tag/v3.6.0-rc.1" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Helm v3.6.0-rc.1 is a pre-release. It is to help gather feedback from the community as well as give users a chance to test Helm in staging environments before v3.6.0 is officially released.</p>
<p>The official changelog will come out with the v3.6.0 release. For now, you can see the commit changes from v3.5.4 <a href="https://github.com/helm/helm/compare/v3.5.4...v3.6.0-rc.1">here</a>.</p>
<h2>Installation and Upgrading</h2>
<p>Download Helm v3.6.0-rc.1. The common platform binaries are here:</p>
<ul>
<li><a href="https://get.helm.sh/helm-v3.6.0-rc.1-darwin-amd64.tar.gz" rel="nofollow">MacOS amd64</a> (<a href="https://get.helm.sh/helm-v3.6.0-rc.1-darwin-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / a7469c2cabc8a6c771c33789257f729d3c9b29a68a10717478614a87d4b2cc73)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-rc.1-darwin-arm64.tar.gz" rel="nofollow">MacOS arm64</a> (<a href="https://get.helm.sh/helm-v3.6.0-rc.1-darwin-arm64.tar.gz.sha256sum" rel="nofollow">checksum</a> / e4a0b8a17784cc6d5f43d349b34d2b26514f4e73c9594cc3b18139f886fa559d)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-rc.1-linux-amd64.tar.gz" rel="nofollow">Linux amd64</a> (<a href="https://get.helm.sh/helm-v3.6.0-rc.1-linux-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 509ddd39cf55f398c960c03f0b580ae202bbc89bbf86acaa559724510344122b)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-rc.1-linux-arm.tar.gz" rel="nofollow">Linux arm</a> (<a href="https://get.helm.sh/helm-v3.6.0-rc.1-linux-arm.tar.gz.sha256sum" rel="nofollow">checksum</a> / e49641fac4be90b79a3830bd69871eb3a9bd4007a858502bba8f271aff632ab4)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-rc.1-linux-arm64.tar.gz" rel="nofollow">Linux arm64</a> (<a href="https://get.helm.sh/helm-v3.6.0-rc.1-linux-arm64.tar.gz.sha256sum" rel="nofollow">checksum</a> / f20c0c76cf99d4078c85b877870d19e25b3a969fe9d3d6349a2093915f91bba7)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-rc.1-linux-386.tar.gz" rel="nofollow">Linux i386</a> (<a href="https://get.helm.sh/helm-v3.6.0-rc.1-linux-386.tar.gz.sha256sum" rel="nofollow">checksum</a> / d4e3555eb61c3777e7bcdfc1497053bc0333534b2b87f1379e441732cf97e877)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-rc.1-linux-ppc64le.tar.gz" rel="nofollow">Linux ppc64le</a> (<a href="https://get.helm.sh/helm-v3.6.0-rc.1-linux-ppc64le.tar.gz.sha256sum" rel="nofollow">checksum</a> / 1589073919459a8c55bf42fe127a100d18a92e3f448392165d0dff09d144528e)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-rc.1-linux-s390x.tar.gz" rel="nofollow">Linux s390x</a> (<a href="https://get.helm.sh/helm-v3.6.0-rc.1-linux-s390x.tar.gz.sha256sum" rel="nofollow">checksum</a> / 2ec4b11875beb73c9ece393b621884c6e6c046990eb371fbe783dc878c81fb79)</li>
<li><a href="https://get.helm.sh/helm-v3.6.0-rc.1-windows-amd64.zip" rel="nofollow">Windows amd64</a> (<a href="https://get.helm.sh/helm-v3.6.0-rc.1-windows-amd64.zip.sha256sum" rel="nofollow">checksum</a> / 0bf1b3f1881f7b9e343955c02acc22f725f05d4a11e751f1e7d4d087554bd5f5)</li>
</ul>
<p>This release was signed with <code>672C 657B E06B 4B30 969C 4A57 4614 49C2 5E36 B98E </code> and can be found at <a class="user-mention" href="https://github.com/mattfarina">@mattfarina</a> <a href="https://keybase.io/mattfarina" rel="nofollow">keybase account</a>. Please use the attached signatures for verifying this release using <code>gpg</code>.</p>

## Helm v3.5.4
<p style="font-size:12px;"> 14, Apr 2021 
<a href="https://github.com/helm/helm/releases/tag/v3.5.4" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Helm v3.5.4 is a patch release. Users are encouraged to upgrade for the best experience.</p>
<p>The community keeps growing, and we'd love to see you there!</p>
<ul>
<li>Join the discussion in <a href="https://kubernetes.slack.com" rel="nofollow">Kubernetes Slack</a>:
<ul>
<li>for questions and just to hang out</li>
<li>for discussing PRs, code, and bugs</li>
</ul>
</li>
<li>Hang out at the Public Developer Call: Thursday, 9:30 Pacific via <a href="https://zoom.us/j/696660622" rel="nofollow">Zoom</a></li>
<li>Test, debug, and contribute charts: <a href="https://artifacthub.io/packages/search?kind=0" rel="nofollow">ArtifactHub/packages</a></li>
</ul>
<h2>Installation and Upgrading</h2>
<p>Download Helm v3.5.4. The common platform binaries are here:</p>
<ul>
<li><a href="https://get.helm.sh/helm-v3.5.4-darwin-amd64.tar.gz" rel="nofollow">MacOS amd64</a> (<a href="https://get.helm.sh/helm-v3.5.4-darwin-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 072c40c743d30efdb8231ca03bab55caee7935e52175e42271a0c3bc37ec0b7b)</li>
<li><a href="https://get.helm.sh/helm-v3.5.4-linux-amd64.tar.gz" rel="nofollow">Linux amd64</a> (<a href="https://get.helm.sh/helm-v3.5.4-linux-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / a8ddb4e30435b5fd45308ecce5eaad676d64a5de9c89660b56face3fe990b318)</li>
<li><a href="https://get.helm.sh/helm-v3.5.4-linux-arm.tar.gz" rel="nofollow">Linux arm</a> (<a href="https://get.helm.sh/helm-v3.5.4-linux-arm.tar.gz.sha256sum" rel="nofollow">checksum</a> / 1a9cc09ef06db29a0232d265f73625056a0cb089e5a16b0a5ef8e810e0533157)</li>
<li><a href="https://get.helm.sh/helm-v3.5.4-linux-arm64.tar.gz" rel="nofollow">Linux arm64</a> (<a href="https://get.helm.sh/helm-v3.5.4-linux-arm64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 9db01522150a83a5d65b420171147448d8396c142d2c91af95e5ee77c1694176)</li>
<li><a href="https://get.helm.sh/helm-v3.5.4-linux-386.tar.gz" rel="nofollow">Linux i386</a> (<a href="https://get.helm.sh/helm-v3.5.4-linux-386.tar.gz.sha256sum" rel="nofollow">checksum</a> / 0a8366cfd6a51a66122c8705c153b06202a4c13bf590f31dcf15c54f40975267)</li>
<li><a href="https://get.helm.sh/helm-v3.5.4-linux-ppc64le.tar.gz" rel="nofollow">Linux ppc64le</a> (<a href="https://get.helm.sh/helm-v3.5.4-linux-ppc64le.tar.gz.sha256sum" rel="nofollow">checksum</a> / 228dee9d5799cdeb92a7bc575c2177d2f4367f91dd3ee6ce506c45089fe929f8)</li>
<li><a href="https://get.helm.sh/helm-v3.5.4-linux-s390x.tar.gz" rel="nofollow">Linux s390x</a> (<a href="https://get.helm.sh/helm-v3.5.4-linux-s390x.tar.gz.sha256sum" rel="nofollow">checksum</a> / 18e6c761943b9862704dfe8c914a574e313e4628c0bee6f37176a423b47d46d2)</li>
<li><a href="https://get.helm.sh/helm-v3.5.4-windows-amd64.zip" rel="nofollow">Windows amd64</a> (<a href="https://get.helm.sh/helm-v3.5.4-windows-amd64.zip.sha256sum" rel="nofollow">checksum</a> / 830da2a8fba060ceff95486b3166b11c517035092e213f8d775be4ae2f7c13e0)</li>
</ul>
<p>This release was signed with <code>672C 657B E06B 4B30 969C 4A57 4614 49C2 5E36 B98E </code> and can be found at <a class="user-mention" href="https://github.com/mattfarina">@mattfarina</a> <a href="https://keybase.io/mattfarina" rel="nofollow">keybase account</a>. Please use the attached signatures for verifying this release using <code>gpg</code>.</p>
<p>The <a href="https://helm.sh/docs/intro/quickstart/" rel="nofollow">Quickstart Guide</a> will get you going from there. For <strong>upgrade instructions</strong> or detailed installation notes, check the <a href="https://helm.sh/docs/intro/install/" rel="nofollow">install guide</a>. You can also use a <a href="https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3" rel="nofollow">script to install</a> on any system with <code>bash</code>.</p>
<h2>What's Next</h2>
<ul>
<li>3.6.0 is the next feature release and will be released on May 26, 2021.</li>
</ul>
<h2>Changelog</h2>
<ul>
<li>Add/update deprecation notices <a class="commit-link" href="https://github.com/helm/helm/commit/1b5edb69df3d3a08df77c9902dc17af864ff05d1"><tt>1b5edb6</tt></a> (Simon Croome)</li>
<li>Wrap validation error instead of recreating <a class="commit-link" href="https://github.com/helm/helm/commit/29fc83554130762a6f5d70c886891fef1ebea018"><tt>29fc835</tt></a> (Simon Croome)</li>
<li>Move default to avoid nil check <a class="commit-link" href="https://github.com/helm/helm/commit/9b7322861d651ea5be5b42df6cb84fa934d5d428"><tt>9b73228</tt></a> (Simon Croome)</li>
<li>Add name validation rules for object kinds <a class="commit-link" href="https://github.com/helm/helm/commit/dacb65d7f43723dca43ef4303534127b1fe91d1c"><tt>dacb65d</tt></a> (Simon Croome)</li>
<li>Use kube libraries v0.20.4 <a class="commit-link" href="https://github.com/helm/helm/commit/c409cf1e987cf5d786ebfbcc3bfaa1d56cdf1c95"><tt>c409cf1</tt></a> (Shoubhik Bose)</li>
</ul>

## Helm 3.5.3
<p style="font-size:12px;"> 10, Mar 2021 
<a href="https://github.com/helm/helm/releases/tag/v3.5.3" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Helm v3.5.3 is a patch release. Users are encouraged to upgrade for the best experience.</p>
<p>The community keeps growing, and we'd love to see you there!</p>
<ul>
<li>Join the discussion in <a href="https://kubernetes.slack.com" rel="nofollow">Kubernetes Slack</a>:
<ul>
<li>for questions and just to hang out</li>
<li>for discussing PRs, code, and bugs</li>
</ul>
</li>
<li>Hang out at the Public Developer Call: Thursday, 9:30 Pacific via <a href="https://zoom.us/j/696660622" rel="nofollow">Zoom</a></li>
<li>Test, debug, and contribute charts: <a href="https://artifacthub.io/packages/search?kind=0" rel="nofollow">ArtifactHub/packages</a></li>
</ul>
<h2>Installation and Upgrading</h2>
<p>Download Helm v3.5.3. The common platform binaries are here:</p>
<ul>
<li><a href="https://get.helm.sh/helm-v3.5.3-darwin-amd64.tar.gz" rel="nofollow">MacOS amd64</a> (<a href="https://get.helm.sh/helm-v3.5.3-darwin-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 451ad70dfe286e3979c78ecf7074f4749d93644da8aa2cc778e2f969771f1794)</li>
<li><a href="https://get.helm.sh/helm-v3.5.3-linux-amd64.tar.gz" rel="nofollow">Linux amd64</a> (<a href="https://get.helm.sh/helm-v3.5.3-linux-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 2170a1a644a9e0b863f00c17b761ce33d4323da64fc74562a3a6df2abbf6cd70)</li>
<li><a href="https://get.helm.sh/helm-v3.5.3-linux-arm.tar.gz" rel="nofollow">Linux arm</a> (<a href="https://get.helm.sh/helm-v3.5.3-linux-arm.tar.gz.sha256sum" rel="nofollow">checksum</a> / fd9c1e1eaa6d8d2c9df6027524e80b8bfde0ea49de5f324845256b3e9cc2edb0)</li>
<li><a href="https://get.helm.sh/helm-v3.5.3-linux-arm64.tar.gz" rel="nofollow">Linux arm64</a> (<a href="https://get.helm.sh/helm-v3.5.3-linux-arm64.tar.gz.sha256sum" rel="nofollow">checksum</a> / e1348d94ce4caace43689ee2dfa5f8bcd8687c12053d9c13d79875b65d6b72aa)</li>
<li><a href="https://get.helm.sh/helm-v3.5.3-linux-386.tar.gz" rel="nofollow">Linux i386</a> (<a href="https://get.helm.sh/helm-v3.5.3-linux-386.tar.gz.sha256sum" rel="nofollow">checksum</a> / e1458691d6a2da96a5d7ab10de4deaa2166d3bc6d6bb3303377278719ae4da95)</li>
<li><a href="https://get.helm.sh/helm-v3.5.3-linux-ppc64le.tar.gz" rel="nofollow">Linux ppc64le</a> (<a href="https://get.helm.sh/helm-v3.5.3-linux-ppc64le.tar.gz.sha256sum" rel="nofollow">checksum</a> / 579f903f0579d156a7f0cceff4a14306cdc5daa1d8839aabaf20edd3f1569577)</li>
<li><a href="https://get.helm.sh/helm-v3.5.3-linux-s390x.tar.gz" rel="nofollow">Linux s390x</a> (<a href="https://get.helm.sh/helm-v3.5.3-linux-s390x.tar.gz.sha256sum" rel="nofollow">checksum</a> / 57e1a137352247abdfabd2e69304a34b5dbf42f30c6405b2a0ea7755063f87c7)</li>
<li><a href="https://get.helm.sh/helm-v3.5.3-windows-amd64.zip" rel="nofollow">Windows amd64</a> (<a href="https://get.helm.sh/helm-v3.5.3-windows-amd64.zip.sha256sum" rel="nofollow">checksum</a> / 33fef4740b255b58a52e5504622068fd8a7d9aea19f1a84438f5cc1c5aade0d6)</li>
</ul>
<p>This release was signed with <code>672C 657B E06B 4B30 969C 4A57 4614 49C2 5E36 B98E </code> and can be found at <a class="user-mention" href="https://github.com/mattfarina">@mattfarina</a> <a href="https://keybase.io/mattfarina" rel="nofollow">keybase account</a>. Please use the attached signatures for verifying this release using <code>gpg</code>.</p>
<p>The <a href="https://helm.sh/docs/intro/quickstart/" rel="nofollow">Quickstart Guide</a> will get you going from there. For <strong>upgrade instructions</strong> or detailed installation notes, check the <a href="https://helm.sh/docs/intro/install/" rel="nofollow">install guide</a>. You can also use a <a href="https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3" rel="nofollow">script to install</a> on any system with <code>bash</code>.</p>
<h2>What's Next</h2>
<ul>
<li>3.5.4 will contain only bug fixes and be released on April 14, 2021</li>
<li>3.6.0 is the next feature release and will be released on May 26, 2021.</li>
</ul>
<h2>Changelog</h2>
<ul>
<li>Fix the example for --time-format flag <a class="commit-link" href="https://github.com/helm/helm/commit/041ce5a2c17a58be0fcd5f5e16fb3e7e95fea622"><tt>041ce5a</tt></a> (mert)</li>
<li>Improve the console output for resource policy keep to align with helm2. <a class="commit-link" href="https://github.com/helm/helm/commit/5487664480b74a3abac845e0592d29c1adc87912"><tt>5487664</tt></a> (Du Zheng)</li>
<li>test(pkg/storage): Verify that storage.Create returns an error if it fails to clean up least-recent release versions <a class="commit-link" href="https://github.com/helm/helm/commit/de2787c794986f275c8e370dc71b0dcdf8f82997"><tt>de2787c</tt></a> (Daniel Lipovetsky)</li>
<li>fix(pkg/storage): If storage.Create fails to clean up recent release versions, return an error <a class="commit-link" href="https://github.com/helm/helm/commit/d552cb3b1d491f4a1aa170d9903a897c1e9ffc7f"><tt>d552cb3</tt></a> (Daniel Lipovetsky)</li>
<li>fix(test): Increase golangci-lint timeout <a class="commit-link" href="https://github.com/helm/helm/commit/bc3cd84eda51a2732d323f21aa67999eb4b9f4a7"><tt>bc3cd84</tt></a> (Marc Khouzam)</li>
<li>fix release sha256 <a class="commit-link" href="https://github.com/helm/helm/commit/dc3971631e1032b6d79c09513a9c3741b3ea6dba"><tt>dc39716</tt></a> (houfangdong)</li>
<li>Fix-9253: Change the deprecated charts repo URL in release notes <a class="commit-link" href="https://github.com/helm/helm/commit/ec560e5f2b3405413a025d031a16c7f7f24ff547"><tt>ec560e5</tt></a> (Jack Whitter-Jones)</li>
<li>Update default ingress values section to correspond with template <a class="commit-link" href="https://github.com/helm/helm/commit/1e126ff4d1f09b806c1952757516f6fc67506ce0"><tt>1e126ff</tt></a> (Nick Jones)</li>
<li>use kube libraries v0.20.2 <a class="commit-link" href="https://github.com/helm/helm/commit/773008a4e76a1f460517b88d0bd7129540204fbd"><tt>773008a</tt></a> (Shoubhik Bose)</li>
</ul>

## Helm 3.5.2
<p style="font-size:12px;"> 09, Feb 2021 
<a href="https://github.com/helm/helm/releases/tag/v3.5.2" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Helm v3.5.2 is a security (patch) release. Users are strongly recommended to update to this release. It fixes two security issues in upstream dependencies and one security issue in the Helm codebase.</p>
<p>Please review the following security advisories for context:</p>
<ul>
<li>During an audit, Helm core maintainers discovered sanitization issues <a href="https://github.com/helm/helm/security/advisories/GHSA-c38g-469g-cmgx">described in a security advisory</a>. These have been fixed.</li>
<li>GoUtils (via Sprig) updated the <a href="https://github.com/Masterminds/goutils/security/advisories/GHSA-xg2h-wx96-xgxr">random alphanumeric functions</a> used in Helm templates. Thanks to Open Source Developer Erik Sundell of Sundell Open Source Consulting AB for reporting this issue.</li>
<li>ORAS had a <a href="https://github.com/helm/helm/security/advisories/GHSA-c38g-469g-cmgx">security release</a> that does not appear to directly impact Helm. However, we have merged it as a precaution.</li>
<li>The Go team renamed a crypto library (golang.org/x/crypto/ssh/terminal to golang.org/x/term). This was NOT a security fix. But it was a breaking change to the Helm build.</li>
</ul>
<blockquote>
<p><strong>WARNING:</strong> Helm is now stricter about sanitizing data in <code>Chart.yaml</code>, <code>index.yaml</code>, and <code>plugin.yaml</code>. In particular, we are stricter about SemVer strings.</p>
</blockquote>
<p>The community keeps growing, and we'd love to see you there!</p>
<ul>
<li>Join the discussion in <a href="https://kubernetes.slack.com" rel="nofollow">Kubernetes Slack</a>:
<ul>
<li>for questions and just to hang out</li>
<li>for discussing PRs, code, and bugs</li>
</ul>
</li>
<li>Hang out at the Public Developer Call: Thursday, 9:30 Pacific via <a href="https://zoom.us/j/696660622" rel="nofollow">Zoom</a></li>
<li>Test, debug, and contribute charts: <a href="https://github.com/helm/charts">GitHub/helm/charts</a></li>
</ul>
<h2>Installation and Upgrading</h2>
<p>Download Helm v3.5.2. The common platform binaries are here:</p>
<ul>
<li><a href="https://get.helm.sh/helm-v3.5.2-darwin-amd64.tar.gz" rel="nofollow">MacOS amd64</a> (<a href="https://get.helm.sh/helm-v3.5.2-darwin-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 68040e9a2f147a92c2f66ce009069826df11f9d1e1c6b78c7457066080ad3229)</li>
<li><a href="https://get.helm.sh/helm-v3.5.2-linux-amd64.tar.gz" rel="nofollow">Linux amd64</a> (<a href="https://get.helm.sh/helm-v3.5.2-linux-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 01b317c506f8b6ad60b11b1dc3f093276bb703281cb1ae01132752253ec706a2)</li>
<li><a href="https://get.helm.sh/helm-v3.5.2-linux-arm.tar.gz" rel="nofollow">Linux arm</a> (<a href="https://get.helm.sh/helm-v3.5.2-linux-arm.tar.gz.sha256sum" rel="nofollow">checksum</a> / 98d090fc1769f5bf7451c15f6ed5a173a1ce5175eca32070ac19064d36470f1b)</li>
<li><a href="https://get.helm.sh/helm-v3.5.2-linux-arm64.tar.gz" rel="nofollow">Linux arm64</a> (<a href="https://get.helm.sh/helm-v3.5.2-linux-arm64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 126a72e2b209194fd2735861f0cf8bd5b5d1386eedd6aed6e0e050dca80d493e)</li>
<li><a href="https://get.helm.sh/helm-v3.5.2-linux-386.tar.gz" rel="nofollow">Linux i386</a> (<a href="https://get.helm.sh/helm-v3.5.2-linux-386.tar.gz.sha256sum" rel="nofollow">checksum</a> / c237ea10af6227c71cff745b3ed3f5653ca1cd5887903ae078ab1b62fbdd45ba)</li>
<li><a href="https://get.helm.sh/helm-v3.5.2-linux-ppc64le.tar.gz" rel="nofollow">Linux ppc64le</a> (<a href="https://get.helm.sh/helm-v3.5.2-linux-ppc64le.tar.gz.sha256sum" rel="nofollow">checksum</a> / 1940d66a05fcf06cc52f55011b81d9c075c234644336d28c14a501f5ca15350d)</li>
<li><a href="https://get.helm.sh/helm-v3.5.2-linux-s390x.tar.gz" rel="nofollow">Linux s390x</a> (<a href="https://get.helm.sh/helm-v3.5.2-linux-s390x.tar.gz.sha256sum" rel="nofollow">checksum</a> / 5240797c2dee43222a1fbed4c4659521578538f20f3626d7c1aeddee7a8ec526)</li>
<li><a href="https://get.helm.sh/helm-v3.5.2-windows-amd64.zip" rel="nofollow">Windows amd64</a> (<a href="https://get.helm.sh/helm-v3.5.2-windows-amd64.zip.sha256sum" rel="nofollow">checksum</a> / 079711eeadd3276da0d946a116f4dc08d58b015ca1874d7b3f3cd633e079589e)</li>
</ul>
<p>This release was signed with <code>672C 657B E06B 4B30 969C 4A57 4614 49C2 5E36 B98E </code> and can be found at <a class="user-mention" href="https://github.com/mattfarina">@mattfarina</a> <a href="https://keybase.io/mattfarina" rel="nofollow">keybase account</a>. Please use the attached signatures for verifying this release using <code>gpg</code>.</p>
<p>The <a href="https://helm.sh/docs/intro/quickstart/" rel="nofollow">Quickstart Guide</a> will get you going from there. For <strong>upgrade instructions</strong> or detailed installation notes, check the <a href="https://helm.sh/docs/intro/install/" rel="nofollow">install guide</a>. You can also use a <a href="https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3" rel="nofollow">script to install</a> on any system with <code>bash</code>.</p>
<h2>What's Next</h2>
<ul>
<li>3.5.3 will contain only bug fixes and be released on March 10, 2021.</li>
<li>3.6.0 is the next feature release and will be released on May 26, 2021.</li>
</ul>
<h2>Changelog</h2>
<ul>
<li>Upgrade to oras v0.9.0 (<a class="issue-link js-issue-link" href="https://github.com/helm/helm/pull/9269">#9269</a>) <a class="commit-link" href="https://github.com/helm/helm/commit/167aac70832d3a384f65f9745335e9fb40169dc2"><tt>167aac7</tt></a> (Josh Dolitsky)</li>
<li>Adding missing replace directive for oras <a class="commit-link" href="https://github.com/helm/helm/commit/bb44eae0a1144ce672486a5468a8211dee4ab8a7"><tt>bb44eae</tt></a> (Matt Farina)</li>
<li>chore(go.mod): bump Masterminds/{spring,goutils} and deislabs/oras <a class="commit-link" href="https://github.com/helm/helm/commit/09fa6b268d940b079c2413f28fac5c8562dd6677"><tt>09fa6b2</tt></a> (Adam Reese)</li>
<li>fix(*): Validate metadata semver and printable characters <a class="commit-link" href="https://github.com/helm/helm/commit/2bf5c280d56e0043bf1870f84d63e82d5c5d4230"><tt>2bf5c28</tt></a> (Adam Reese)</li>
</ul>

## Helm 3.5.1
<p style="font-size:12px;"> 28, Jan 2021 
<a href="https://github.com/helm/helm/releases/tag/v3.5.1" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Helm v3.5.1 is a patch release. This release is the same Helm source as v3.5.0 but is built using Go 1.15.7. <a href="https://groups.google.com/g/golang-dev/c/uYcPPYV2jLY" rel="nofollow">Go 1.15.7 is a security release</a>. Users are encouraged to upgrade for the best experience.</p>
<p>The community keeps growing, and we'd love to see you there!</p>
<ul>
<li>Join the discussion in <a href="https://kubernetes.slack.com" rel="nofollow">Kubernetes Slack</a>:
<ul>
<li>for questions and just to hang out</li>
<li>for discussing PRs, code, and bugs</li>
</ul>
</li>
<li>Hang out at the Public Developer Call: Thursday, 9:30 Pacific via <a href="https://zoom.us/j/696660622" rel="nofollow">Zoom</a></li>
<li>Test, debug, and contribute charts: <a href="https://github.com/helm/charts">GitHub/helm/charts</a></li>
</ul>
<h2>Installation and Upgrading</h2>
<p>Download Helm v3.5.1. The common platform binaries are here:</p>
<ul>
<li><a href="https://get.helm.sh/helm-v3.5.1-darwin-amd64.tar.gz" rel="nofollow">MacOS amd64</a> (<a href="https://get.helm.sh/helm-v3.5.1-darwin-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / c9b09c7184d95ec6cb3eaddafdc5268688b54359e47d912b0c54068784d8c7eb)</li>
<li><a href="https://get.helm.sh/helm-v3.5.1-linux-amd64.tar.gz" rel="nofollow">Linux amd64</a> (<a href="https://get.helm.sh/helm-v3.5.1-linux-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / cad8f2f55a87cfd4d79312625c6af62c1e22eb1dab750f00aa1d394c601a2e6b)</li>
<li><a href="https://get.helm.sh/helm-v3.5.1-linux-arm.tar.gz" rel="nofollow">Linux arm</a> (<a href="https://get.helm.sh/helm-v3.5.1-linux-arm.tar.gz.sha256sum" rel="nofollow">checksum</a> / 0b86a5a68df7376484babb6d7ffe1bae36012b4d65f1bcddb4255fb3bbe811db)</li>
<li><a href="https://get.helm.sh/helm-v3.5.1-linux-arm64.tar.gz" rel="nofollow">Linux arm64</a> (<a href="https://get.helm.sh/helm-v3.5.1-linux-arm64.tar.gz.sha256sum" rel="nofollow">checksum</a> / d0ada80576f8016d1cc38a06d225a4379a53e88e3e26b417e6de5db05a090ce4)</li>
<li><a href="https://get.helm.sh/helm-v3.5.1-linux-386.tar.gz" rel="nofollow">Linux i386</a> (<a href="https://get.helm.sh/helm-v3.5.1-linux-386.tar.gz.sha256sum" rel="nofollow">checksum</a> / f446ed424de9a177a4d5bb4a81f5086738527ab6aaded10243f28af9fc4d52cb)</li>
<li><a href="https://get.helm.sh/helm-v3.5.1-linux-ppc64le.tar.gz" rel="nofollow">Linux ppc64le</a> (<a href="https://get.helm.sh/helm-v3.5.1-linux-ppc64le.tar.gz.sha256sum" rel="nofollow">checksum</a> / 10ba07fc773a241037e4f8d0b653000a357edd8e7819ae2e4101caa302c23426)</li>
<li><a href="https://get.helm.sh/helm-v3.5.1-linux-s390x.tar.gz" rel="nofollow">Linux s390x</a> (<a href="https://get.helm.sh/helm-v3.5.1-linux-s390x.tar.gz.sha256sum" rel="nofollow">checksum</a> / c9b09c7184d95ec6cb3eaddafdc5268688b54359e47d912b0c54068784d8c7eb)</li>
<li><a href="https://get.helm.sh/helm-v3.5.1-windows-amd64.zip" rel="nofollow">Windows amd64</a> (<a href="https://get.helm.sh/helm-v3.5.1-windows-amd64.zip.sha256sum" rel="nofollow">checksum</a> / 793298194038eacce3b0a2e5cefcf104ae3f595740f03f5894e0484e2955d5a9)</li>
</ul>
<p>This release was signed with <code>672C 657B E06B 4B30 969C 4A57 4614 49C2 5E36 B98E </code> and can be found at <a class="user-mention" href="https://github.com/mattfarina">@mattfarina</a> <a href="https://keybase.io/mattfarina" rel="nofollow">keybase account</a>. Please use the attached signatures for verifying this release using <code>gpg</code>.</p>
<p>The <a href="https://helm.sh/docs/intro/quickstart/" rel="nofollow">Quickstart Guide</a> will get you going from there. For <strong>upgrade instructions</strong> or detailed installation notes, check the <a href="https://helm.sh/docs/intro/install/" rel="nofollow">install guide</a>. You can also use a <a href="https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3" rel="nofollow">script to install</a> on any system with <code>bash</code>.</p>
<h2>What's Next</h2>
<ul>
<li>3.5.2 will contain only bug fixes and be released on February 10, 2021.</li>
<li>3.6.0 is the next feature release and will be released on May 26, 2021.</li>
</ul>

## Helm 3.5.0
<p style="font-size:12px;"> 13, Jan 2021 
<a href="https://github.com/helm/helm/releases/tag/v3.5.0" target="_blank"> 
Source </a><OutboundLink /></p>
<h2>v3.5.0</h2>
<p>Helm v3.5.0 is a feature release. This release, we focused on OCI support and template functions. Users are encouraged to upgrade for the best experience.</p>
<p>The community keeps growing, and we'd love to see you there!</p>
<ul>
<li>Join the discussion in <a href="https://kubernetes.slack.com" rel="nofollow">Kubernetes Slack</a>:
<ul>
<li>for questions and just to hang out</li>
<li>for discussing PRs, code, and bugs</li>
</ul>
</li>
<li>Hang out at the Public Developer Call: Thursday, 9:30 Pacific via <a href="https://zoom.us/j/696660622" rel="nofollow">Zoom</a></li>
<li>Test, debug, and contribute charts: <a href="https://github.com/helm/charts">GitHub/helm/charts</a></li>
</ul>
<h2>Notable Changes</h2>
<ul>
<li>Added more than 20 new template functions. See <a href="https://github.com/Masterminds/sprig/releases/tag/v3.2.0">sprig release notes</a> for details.</li>
<li><code>oci://</code> can now be used as a scheme to pull dependencies from OCI registries and used to specify repositories in dependency lists. Note, the experiment needs to be enabled before this will work.</li>
<li>Added <code>--skip-refresh</code> flag to the <code>helm dep build</code> command.</li>
<li>Added <code>--wait-for-jobs</code> flag that can be paired with <code>--wait</code> to ensure jobs complete when waiting.</li>
<li>Added <code>--kube-cafile</code> flag and environment variable <code>HELM_KUBECAFILE</code> to override the system wide certificate authority.</li>
</ul>
<h2>Installation and Upgrading</h2>
<p>Download Helm v3.5.0. The common platform binaries are here:</p>
<ul>
<li><a href="https://get.helm.sh/helm-v3.5.0-darwin-amd64.tar.gz" rel="nofollow">MacOS amd64</a> (<a href="https://get.helm.sh/helm-v3.5.0-darwin-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 53378d8de087395ece3876795111a8077f2451f080ec6150d777cc3105214520)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-linux-amd64.tar.gz" rel="nofollow">Linux amd64</a> (<a href="https://get.helm.sh/helm-v3.5.0-linux-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 3fff0354d5fba4c73ebd5db59a59db72f8a5bbe1117a0b355b0c2983e98db95b)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-linux-arm.tar.gz" rel="nofollow">Linux arm</a> (<a href="https://get.helm.sh/helm-v3.5.0-linux-arm.tar.gz.sha256sum" rel="nofollow">checksum</a> / ca8792da269b72235987ea7245d1450a859b2c0658f591737d74b6c56cd9b1fa)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-linux-arm64.tar.gz" rel="nofollow">Linux arm64</a> (<a href="https://get.helm.sh/helm-v3.5.0-linux-arm64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 87811b648ed9f4c84d3cb67bbea9b666bb7f6dd0ff6aca148b65f91058f73953)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-linux-386.tar.gz" rel="nofollow">Linux i386</a> (<a href="https://get.helm.sh/helm-v3.5.0-linux-386.tar.gz.sha256sum" rel="nofollow">checksum</a> / 7461c478d25870422e3cb4198bc3b42ffdb0961e05cf05967ada35ccfd2d9a0f)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-linux-ppc64le.tar.gz" rel="nofollow">Linux ppc64le</a> (<a href="https://get.helm.sh/helm-v3.5.0-linux-ppc64le.tar.gz.sha256sum" rel="nofollow">checksum</a> / a0e0e4c2090789a3a86b144e84626fa577e8e692247b87261be985bda324d044)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-linux-s390x.tar.gz" rel="nofollow">Linux s390x</a> (<a href="https://get.helm.sh/helm-v3.5.0-linux-s390x.tar.gz.sha256sum" rel="nofollow">checksum</a> / 53378d8de087395ece3876795111a8077f2451f080ec6150d777cc3105214520)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-windows-amd64.zip" rel="nofollow">Windows amd64</a> (<a href="https://get.helm.sh/helm-v3.5.0-windows-amd64.zip.sha256sum" rel="nofollow">checksum</a> / 8253aa42b747a17fa868b00bfaf8b55f26170bcfc6cdb1b909942e01537a756c)</li>
</ul>
<p>This release was signed with <code>672C 657B E06B 4B30 969C 4A57 4614 49C2 5E36 B98E </code> and can be found at <a class="user-mention" href="https://github.com/mattfarina">@mattfarina</a> <a href="https://keybase.io/mattfarina" rel="nofollow">keybase account</a>. Please use the attached signatures for verifying this release using <code>gpg</code>.</p>
<p>The <a href="https://helm.sh/docs/intro/quickstart/" rel="nofollow">Quickstart Guide</a> will get you going from there. For <strong>upgrade instructions</strong> or detailed installation notes, check the <a href="https://helm.sh/docs/intro/install/" rel="nofollow">install guide</a>. You can also use a <a href="https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3" rel="nofollow">script to install</a> on any system with <code>bash</code>.</p>
<h2>What's Next</h2>
<ul>
<li>3.5.1 will contain only bug fixes and be released on February 10, 2021.</li>
<li>3.6.0 is the next feature release and will be released on May 26, 2021.</li>
</ul>
<h2>Changelog</h2>
<ul>
<li>Fix dep build with OCI based charts <a class="commit-link" href="https://github.com/helm/helm/commit/32c22239423b3b4ba6706d450bd044baffdcf9e6"><tt>32c2223</tt></a> (Matt Farina)</li>
<li>bump version to <a class="commit-link" href="https://github.com/helm/helm/commit/f546ebb1aca7c45a09a71886b720b6e11d45e9d8"><tt>f546ebb</tt></a> (Matt Farina)</li>
<li>Adding apiserver to mod/sum <a class="commit-link" href="https://github.com/helm/helm/commit/da4c40c5421773de1a28624c50e2cbebfb5fc11f"><tt>da4c40c</tt></a> (Matt Farina)</li>
<li>Reduce linting severity for users of out-of-date kubernetes (<a class="issue-link js-issue-link" href="https://github.com/helm/helm/pull/8608">#8608</a>) <a class="commit-link" href="https://github.com/helm/helm/commit/fdcd22ef589d781090e704a8c366e89be4dbc1e4"><tt>fdcd22e</tt></a> (Joe Julian)</li>
<li>Bumping kubernetes to 1.20.1 <a class="commit-link" href="https://github.com/helm/helm/commit/b880fc5c0fa9dcdfdd8b3ca43be6b463937ec280"><tt>b880fc5</tt></a> (Matt Farina)</li>
<li>Add explanatory comments to action.List and action.History <a class="commit-link" href="https://github.com/helm/helm/commit/1da2212a9de64671edb17f727b937215cc252309"><tt>1da2212</tt></a> (Daniel Lipovetsky)</li>
<li>Address error on deletion of old dependencies <a class="commit-link" href="https://github.com/helm/helm/commit/beda5e1e2be460543c32e2267982d6a7333be483"><tt>beda5e1</tt></a> (Peter Engelbert)</li>
<li>Fixed bug - The flags --cert-file/--key-file where ignored when --insecure-skip-tls-verify flag is set (<a class="issue-link js-issue-link" href="https://github.com/helm/helm/pull/9070">#9070</a>) <a class="commit-link" href="https://github.com/helm/helm/commit/a202fb0c0b73a1093609251476e0d8a1b76b3b8f"><tt>a202fb0</tt></a> (Dinu Mathai)</li>
<li>Replace Helm Hub with Artifact Hub (<a class="issue-link js-issue-link" href="https://github.com/helm/helm/pull/8626">#8626</a>) <a class="commit-link" href="https://github.com/helm/helm/commit/c495e88250a74f5e55e8c5eabfe8ae52ce248121"><tt>c495e88</tt></a> (Scott Rigby)</li>
<li>fix(pkg/chartutil): Remove warning for nils <a class="commit-link" href="https://github.com/helm/helm/commit/bed1a42a398b30a63a279d68cc7319ceb4618ec3"><tt>bed1a42</tt></a> (Marc Khouzam)</li>
<li>Updating to sprig 3.2.0 <a class="commit-link" href="https://github.com/helm/helm/commit/fb0345a07f160220cbddd767e61a3a23705abbdb"><tt>fb0345a</tt></a> (Matt Farina)</li>
<li>Updating to Kuberentes 1.20 packages <a class="commit-link" href="https://github.com/helm/helm/commit/363fb1edf1b74acca93df93714fabbb101569e28"><tt>363fb1e</tt></a> (Matt Farina)</li>
<li>Bump github.com/Masterminds/semver/v3 from 3.1.0 to 3.1.1 (<a class="issue-link js-issue-link" href="https://github.com/helm/helm/pull/9109">#9109</a>) <a class="commit-link" href="https://github.com/helm/helm/commit/21078d4794a0c4ae2fc3ab4baef03e9b72e6aba6"><tt>21078d4</tt></a> (dependabot[bot])</li>
<li>Bump github.com/Masterminds/squirrel from 1.4.0 to 1.5.0 (<a class="issue-link js-issue-link" href="https://github.com/helm/helm/pull/9108">#9108</a>) <a class="commit-link" href="https://github.com/helm/helm/commit/87ed57b5e07918244fa202126f957b6dd70d04d1"><tt>87ed57b</tt></a> (dependabot[bot])</li>
<li>Bump github.com/lib/pq from 1.8.0 to 1.9.0 (<a class="issue-link js-issue-link" href="https://github.com/helm/helm/pull/9107">#9107</a>) <a class="commit-link" href="https://github.com/helm/helm/commit/937d688f5ca66f3d1e539c144a692099e09617c4"><tt>937d688</tt></a> (dependabot[bot])</li>
<li>Remove OCI boolean from  struct <a class="commit-link" href="https://github.com/helm/helm/commit/f666fceb30a1033f3309a4e47bedb6193791619e"><tt>f666fce</tt></a> (Peter Engelbert)</li>
<li>Clean up imports and add doc comments <a class="commit-link" href="https://github.com/helm/helm/commit/3028c5585892860975c416965a2aa4f75b023853"><tt>3028c55</tt></a> (Peter Engelbert)</li>
<li>Implement <code>helm pull</code> for OCI registries <a class="commit-link" href="https://github.com/helm/helm/commit/3ad08f3ea9c09d16ddf6519d65f3f6f2ceee2c37"><tt>3ad08f3</tt></a> (Peter Engelbert)</li>
<li>Adds the option kube-cafile and env variable HELM_KUBECAFILE for a overwrite of the certificate authority file <a class="commit-link" href="https://github.com/helm/helm/commit/cc1d2d62e97ab296e698633d2b81d1455fdfca93"><tt>cc1d2d6</tt></a> (Lüchinger Dominic)</li>
<li>Builds with go 1.15 <a class="commit-link" href="https://github.com/helm/helm/commit/65ed70341d0cd1d93cc053a12c09f3d3a7f732e0"><tt>65ed703</tt></a> (Matt Farina)</li>
<li>Updating to Kubernetes 1.19.4 package versions <a class="commit-link" href="https://github.com/helm/helm/commit/7c4e0b17df40cd90a1a53e4e171a4c664abf3f0e"><tt>7c4e0b1</tt></a> (Matt Farina)</li>
<li>Add CodeQL Security Scanning <a class="commit-link" href="https://github.com/helm/helm/commit/78604539237e732b56e41459a053c07eddc136d7"><tt>7860453</tt></a> (Chris Aniszczyk)</li>
<li>Fix test <a class="commit-link" href="https://github.com/helm/helm/commit/f30badd5709ebc1afbc809716c8aae3c9ebcc7fc"><tt>f30badd</tt></a> (rimas)</li>
<li>Fixes <a class="issue-link js-issue-link" href="https://github.com/helm/helm/issues/9083">#9083</a> <a class="commit-link" href="https://github.com/helm/helm/commit/ce1a46899f5b1e7ba9d485d7800d0d23313d7d7b"><tt>ce1a468</tt></a> (rimas)</li>
<li>[COMMENT]fix comment <a class="commit-link" href="https://github.com/helm/helm/commit/7c4932c485edb49874919c2cd6bb171506497c3d"><tt>7c4932c</tt></a> (Scaat Feng)</li>
<li>Fix typo <a class="commit-link" href="https://github.com/helm/helm/commit/5d08a0d00e4f0d31d6db55e71bccbcd665366c9a"><tt>5d08a0d</tt></a> (Jon Huhn)</li>
<li>fix: ingress path issue <a class="commit-link" href="https://github.com/helm/helm/commit/50144aad0332692059534acd574fcf141307ef2d"><tt>50144aa</tt></a> (Salim Salaues)</li>
<li>Revert "Add support to judge whether desired version is available or not" <a class="commit-link" href="https://github.com/helm/helm/commit/0fe547c8e7ad19a45a1fcaf8ccd1fc20730f44da"><tt>0fe547c</tt></a> (Matthew Fisher)</li>
<li>Cleanup tempfiles introduced by unit tests under pkg/ <a class="commit-link" href="https://github.com/helm/helm/commit/1aa6e928ce14a1496cebfc877a3790b9773a4d88"><tt>1aa6e92</tt></a> (Ma Xinjian)</li>
<li>bump actions/stale to v3.0.14 <a class="commit-link" href="https://github.com/helm/helm/commit/8592029379611dc847b1a4eeee33c9202a0a9877"><tt>8592029</tt></a> (Matthew Fisher)</li>
<li>increase number of operations per run to 100 <a class="commit-link" href="https://github.com/helm/helm/commit/b79134a91df8c62206317b30cc651344377dde05"><tt>b79134a</tt></a> (Matthew Fisher)</li>
<li>feat(helm): Allow generating markdown docs headers <a class="commit-link" href="https://github.com/helm/helm/commit/d9c5754dfc0a0f42d8b11b9562540d17bd9d639b"><tt>d9c5754</tt></a> (Marc Khouzam)</li>
<li>chore(comp): Remove unnecessary completion code <a class="commit-link" href="https://github.com/helm/helm/commit/b266c2ef0f2dcdb7d02049c69771cd1df3d52de6"><tt>b266c2e</tt></a> (Marc Khouzam)</li>
<li>Added tests for PR 8948 <a class="commit-link" href="https://github.com/helm/helm/commit/82002c3cfba61c5fbe0dac7bead7fc5e44f4d1ae"><tt>82002c3</tt></a> (Matt Farina)</li>
<li>add unittes for 'helm dep build' with --skip-refresh flag. <a class="commit-link" href="https://github.com/helm/helm/commit/4b229cc2151cacd055c45331cab4160956b0c03a"><tt>4b229cc</tt></a> (yxxhero)</li>
<li>Updating to k8s 1.19.3 based packages <a class="commit-link" href="https://github.com/helm/helm/commit/e413c34ddeae75041416b7b9e4828be929c906fb"><tt>e413c34</tt></a> (Matt Farina)</li>
<li>lint: lint all documents in a multi-doc yaml file <a class="commit-link" href="https://github.com/helm/helm/commit/dfb5a5e8ccc2ae41c50159e8cdcf5066b63ec931"><tt>dfb5a5e</tt></a> (Nandor Kracser)</li>
<li>fix(helm): flag descriptions start with lowercase <a class="commit-link" href="https://github.com/helm/helm/commit/e16d26717b1b7588ab24fa0a87e48dc1940c80d2"><tt>e16d267</tt></a> (Marc Khouzam)</li>
<li>List either incubator or stable. <a class="commit-link" href="https://github.com/helm/helm/commit/4a3ffd53ca3991450cc6a45cc4e7538a111139f8"><tt>4a3ffd5</tt></a> (Bridget Kromhout)</li>
<li>add waitwithjobs instead of changing wait api <a class="commit-link" href="https://github.com/helm/helm/commit/bfc575dec2f6ed5ce897c38d0d89b0fe936606c0"><tt>bfc575d</tt></a> (zh168654)</li>
<li>add wait-for-jobs flag <a class="commit-link" href="https://github.com/helm/helm/commit/957d2a2bf978b06cb148b9429b8dd9258c24b887"><tt>957d2a2</tt></a> (zh168654)</li>
<li>fix style conformance <a class="commit-link" href="https://github.com/helm/helm/commit/bd03e1b5c70cffd13e740f40ef1c0e8c3a49e092"><tt>bd03e1b</tt></a> (zhangye15)</li>
<li>fix test-style error <a class="commit-link" href="https://github.com/helm/helm/commit/c96dc48f21adbc79e410fafc63f6f6daa221c424"><tt>c96dc48</tt></a> (zhangye15)</li>
<li>add test cases <a class="commit-link" href="https://github.com/helm/helm/commit/8d498d58e7b383b6c50d43cc5a55eae4955d354e"><tt>8d498d5</tt></a> (zh168654)</li>
<li>helm upgrade with --wait support jobs in manifest to be completed <a class="commit-link" href="https://github.com/helm/helm/commit/5825112a8b385ca48e67c4782ba77656c6f4fba5"><tt>5825112</tt></a> (zh168654)</li>
<li>completion: move to native zshCompletion <a class="commit-link" href="https://github.com/helm/helm/commit/0490c288f5aa02c26c03eb8472b9aff235bed1ed"><tt>0490c28</tt></a> (knrt10)</li>
<li>Add remaining tests in TestDependentChartAliases <a class="commit-link" href="https://github.com/helm/helm/commit/babc8c9a704c1cf4a6307bb4f8f7c02f20ebd9fb"><tt>babc8c9</tt></a> (Aayush Joglekar)</li>
<li>Clarifies action needed to list new stable repo <a class="commit-link" href="https://github.com/helm/helm/commit/86af591e00ac638734b4e7c5d8a53effad4d6bdc"><tt>86af591</tt></a> (Bridget Kromhout)</li>
<li>feat: Allow helm test to run a subset of tests <a class="commit-link" href="https://github.com/helm/helm/commit/2a7a98ae5acc943f798ca78fcb1de44b6252a0d4"><tt>2a7a98a</tt></a> (Chris Wells)</li>
<li>Fix that the invalid version number of the helm package command will escape <a class="commit-link" href="https://github.com/helm/helm/commit/2c19838295b9b1efd7fb548d047eaff53095ab52"><tt>2c19838</tt></a> (wawa0210)</li>
<li>Updating descriptions <a class="commit-link" href="https://github.com/helm/helm/commit/84b02bbee3ec2415cdddc0b52f85d120f2d4a592"><tt>84b02bb</tt></a> (Bridget Kromhout)</li>
<li>Add support to judge whether desired version is available or not <a class="commit-link" href="https://github.com/helm/helm/commit/24107e6afee108ac42d0ce5b6020475862cd2837"><tt>24107e6</tt></a> (Ma Xinjian)</li>
<li>Add test case for LoadFiles <a class="commit-link" href="https://github.com/helm/helm/commit/9cc00eea246555e30bd06574382e60eb77233413"><tt>9cc00ee</tt></a> (Zhengyi Lai)</li>
<li>Fixes Error: could not find protocol handler for <a class="commit-link" href="https://github.com/helm/helm/commit/882db2543c90bb6e50ffe98083963b65a47cc662"><tt>882db25</tt></a> (Matt Farina)</li>
<li>[<a class="issue-link js-issue-link" href="https://github.com/helm/helm/issues/7696">#7696</a>] Avoid crash in chart loader on unexpected file sequence <a class="commit-link" href="https://github.com/helm/helm/commit/27807e1bb5f37248c59b26e6ac2e4e47bfe5fe9f"><tt>27807e1</tt></a> (Lehel Gyuro)</li>
<li>helm search supports semver pre version numbers starting with 0 <a class="commit-link" href="https://github.com/helm/helm/commit/da6b240fe702d7c1bcdf86b9503191f873fe37dd"><tt>da6b240</tt></a> (wawa0210)</li>
<li>added test for <a class="issue-link js-issue-link" href="https://github.com/helm/helm/pull/8913">#8913</a> related to <a class="issue-link js-issue-link" href="https://github.com/helm/helm/issues/8621">#8621</a> <a class="commit-link" href="https://github.com/helm/helm/commit/8a4c0bc7b1d7f17dededd6167ad4d500073f8842"><tt>8a4c0bc</tt></a> (Christophe VILA)</li>
<li>[<a class="issue-link js-issue-link" href="https://github.com/helm/helm/issues/7696">#7696</a>] Avoid crash in chart loader on unexpected file sequence <a class="commit-link" href="https://github.com/helm/helm/commit/8abb44f2180ae32ed504e761ea6f4646a75a63ab"><tt>8abb44f</tt></a> (Lehel Gyuro)</li>
<li>feat(test): Adapt completion tests to Cobra 1.1 <a class="commit-link" href="https://github.com/helm/helm/commit/82f739072cb3c94f26e3103e4524a1f74526342d"><tt>82f7390</tt></a> (Marc Khouzam)</li>
<li>Bump github.com/spf13/cobra from 1.0.0 to 1.1.1 <a class="commit-link" href="https://github.com/helm/helm/commit/713ec751a3d69482c16513f2acaeefed3cdc6828"><tt>713ec75</tt></a> (dependabot[bot])</li>
<li>Update err message to use the regex pattern directly <a class="commit-link" href="https://github.com/helm/helm/commit/b83632e757bbf6c316a3e11ef984c23ea106bc77"><tt>b83632e</tt></a> (Martin Hickey)</li>
<li>Fix the lint error message for valid names <a class="commit-link" href="https://github.com/helm/helm/commit/5785dd6d497f3eb025a92416db19508cc9a372f0"><tt>5785dd6</tt></a> (Martin Hickey)</li>
<li>do not check YAML if nothing was parsed <a class="commit-link" href="https://github.com/helm/helm/commit/f736af95eb94950acc5871a8451fa4a4bdc37697"><tt>f736af9</tt></a> (Christophe VILA)</li>
<li>fix(test): display error message <a class="commit-link" href="https://github.com/helm/helm/commit/38c964ae8134a65c1ffda13e37ac8e5573bd3de3"><tt>38c964a</tt></a> (Matthew Fisher)</li>
<li>bump version to v3.4.0 <a class="commit-link" href="https://github.com/helm/helm/commit/ce4fa95868c0a27dec081eacf23cc66f1a635eb6"><tt>ce4fa95</tt></a> (Matt Farina)</li>
<li>Skip tests when running helm template <a class="commit-link" href="https://github.com/helm/helm/commit/9ea10ef04a19796507d09334228471b0b60d3842"><tt>9ea10ef</tt></a> (Torsten Walter)</li>
<li>Add --skip-refresh option in helm dep build <a class="commit-link" href="https://github.com/helm/helm/commit/09af5447d900805f19a25259fa1d6e61063fe9f7"><tt>09af544</tt></a> (yxxhero)</li>
<li>Adjusted import <a class="commit-link" href="https://github.com/helm/helm/commit/cf3870a57fc56de0d9569fcbbf6f7b9e978e4cb9"><tt>cf3870a</tt></a> (Janario Oliveira)</li>
<li>Reuse kube-client <a class="commit-link" href="https://github.com/helm/helm/commit/10a29d1662110fb1f1f922d8fed796e69823e5a7"><tt>10a29d1</tt></a> (Janario Oliveira)</li>
<li>fix(helm): allow skipping manifests in tests directories <a class="commit-link" href="https://github.com/helm/helm/commit/3d66daeb55d947c4d30d542dfb7459afc21a3c10"><tt>3d66dae</tt></a> (Torsten Walter)</li>
<li>prepare testdata <a class="commit-link" href="https://github.com/helm/helm/commit/fd157b5a35a65ffce6892d05dafae0f67e69fc97"><tt>fd157b5</tt></a> (Torsten Walter)</li>
<li>Bugfix: panic when chart contains requirements.lock <a class="commit-link" href="https://github.com/helm/helm/commit/ebf6d7e5b2b016cc74da67860f651de9544690a7"><tt>ebf6d7e</tt></a> (Zhengyi Lai)</li>
</ul>

## Helm v3.5.0-rc.2
<p style="font-size:12px;"> 06, Jan 2021 
<a href="https://github.com/helm/helm/releases/tag/v3.5.0-rc.2" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Helm v3.5.0-rc.2 is a pre-release. It is to help gather feedback from the community as well as give users a chance to test Helm in staging environments before v3.5.0 is officially released.</p>
<p>The official changelog will come out with the v3.5.0 release. For now, you can see the commit changes from v3.4.2 <a href="https://github.com/helm/helm/compare/v3.4.2...v3.5.0-rc.2">here</a>.</p>
<h2>Installation and Upgrading</h2>
<p>Download Helm v3.5.0-rc.2. The common platform binaries are here:</p>
<ul>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.2-darwin-amd64.tar.gz" rel="nofollow">MacOS amd64</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.2-darwin-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 12072c84ae7165e05347d282131445a70e465a758bc8b4594f45cb04715caf72)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.2-linux-amd64.tar.gz" rel="nofollow">Linux amd64</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.2-linux-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / e0912608b41ccdeb6a30f0a28114aae9255f571a1c1954278f3bd9aa80d132db)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.2-linux-arm.tar.gz" rel="nofollow">Linux arm</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.2-linux-arm.tar.gz.sha256sum" rel="nofollow">checksum</a> / 752f7a5e6268f44f017726ba1c05560a4814249a3e5d7be0a8961a848a6270d1)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.2-linux-arm64.tar.gz" rel="nofollow">Linux arm64</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.2-linux-arm64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 52b26168002c637cfc78f0e8c2e69e85cae5116a798608ed78d7810e00f36e29)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.2-linux-386.tar.gz" rel="nofollow">Linux i386</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.2-linux-386.tar.gz.sha256sum" rel="nofollow">checksum</a> / 7b21f942d2552571f60e0ee0bbeb86d89a9ee62e6d75097a65723352ca632428)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.2-linux-ppc64le.tar.gz" rel="nofollow">Linux ppc64le</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.2-linux-ppc64le.tar.gz.sha256sum" rel="nofollow">checksum</a> / d0c23de69616f125830d7e28cb981b3eff8ea5c49fd4dd23d7a1778a732ff532)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.2-linux-s390x.tar.gz" rel="nofollow">Linux s390x</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.2-linux-s390x.tar.gz.sha256sum" rel="nofollow">checksum</a> / 12072c84ae7165e05347d282131445a70e465a758bc8b4594f45cb04715caf72)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.2-windows-amd64.zip" rel="nofollow">Windows amd64</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.2-windows-amd64.zip.sha256sum" rel="nofollow">checksum</a> / 45741d9f42c31dab41d8b3305d8b32aff9891277a3d4e355dddaf544db3f97ed)</li>
</ul>
<p>This release was signed with <code>672C 657B E06B 4B30 969C 4A57 4614 49C2 5E36 B98E </code> and can be found at <a class="user-mention" href="https://github.com/mattfarina">@mattfarina</a> <a href="https://keybase.io/mattfarina" rel="nofollow">keybase account</a>. Please use the attached signatures for verifying this release using <code>gpg</code>.</p>

## v3.5.0-rc.1
<p style="font-size:12px;"> 06, Jan 2021 
<a href="https://github.com/helm/helm/releases/tag/v3.5.0-rc.1" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Helm v3.5.0-rc.1 is a pre-release. It is to help gather feedback from the community as well as give users a chance to test Helm in staging environments before v3.5.0 is officially released.</p>
<p>The official changelog will come out with the v3.5.0 release. For now, you can see the commit changes from v3.4.2 <a href="https://github.com/helm/helm/compare/v3.4.2...v3.5.0-rc.1">here</a>.</p>
<h2>Installation and Upgrading</h2>
<p>Download Helm v3.5.0-rc.1. The common platform binaries are here:</p>
<ul>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.1-darwin-amd64.tar.gz" rel="nofollow">MacOS amd64</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.1-darwin-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 2aa82b7b82e5bc354f087afdc30e9855ff19246be7b6c6fb0cbeabf45da9760f)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.1-linux-amd64.tar.gz" rel="nofollow">Linux amd64</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.1-linux-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 0df2fac8b423ed95f9da97e575a830a9d8d497fe6412e4922c0dec3eb6f03bdc)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.1-linux-arm.tar.gz" rel="nofollow">Linux arm</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.1-linux-arm.tar.gz.sha256sum" rel="nofollow">checksum</a> / 565a3aa43cf9bcff2c5cde43d028cb472a81a1c8d8f1d7180c7589c8e64c97f5)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.1-linux-arm64.tar.gz" rel="nofollow">Linux arm64</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.1-linux-arm64.tar.gz.sha256sum" rel="nofollow">checksum</a> / e9c995e582f0a732f7d4900081919b00e23520b5289526b297fd8e2997fa63e6)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.1-linux-386.tar.gz" rel="nofollow">Linux i386</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.1-linux-386.tar.gz.sha256sum" rel="nofollow">checksum</a> / dbceb74588e21bf60cb765dda9c69ff5e34def1bdfa0f1429400c46d7c25b922)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.1-linux-ppc64le.tar.gz" rel="nofollow">Linux ppc64le</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.1-linux-ppc64le.tar.gz.sha256sum" rel="nofollow">checksum</a> / 5acbe798cc8a46bdb32036d6350a99afdf8b7dd5f6ce8dc55468c66f882ffca6)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.1-linux-s390x.tar.gz" rel="nofollow">Linux s390x</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.1-linux-s390x.tar.gz.sha256sum" rel="nofollow">checksum</a> / 2aa82b7b82e5bc354f087afdc30e9855ff19246be7b6c6fb0cbeabf45da9760f)</li>
<li><a href="https://get.helm.sh/helm-v3.5.0-rc.1-windows-amd64.zip" rel="nofollow">Windows amd64</a> (<a href="https://get.helm.sh/helm-v3.5.0-rc.1-windows-amd64.zip.sha256sum" rel="nofollow">checksum</a> / 5fe5074eb7c54fc3f4671e15d004ba7a65087cf13c359b628bd04e1c25f82f5a)</li>
</ul>
<p>This release was signed with <code>672C 657B E06B 4B30 969C 4A57 4614 49C2 5E36 B98E </code> and can be found at <a class="user-mention" href="https://github.com/mattfarina">@mattfarina</a> <a href="https://keybase.io/mattfarina" rel="nofollow">keybase account</a>. Please use the attached signatures for verifying this release using <code>gpg</code>.</p>

## Helm 3.4.2
<p style="font-size:12px;"> 09, Dec 2020 
<a href="https://github.com/helm/helm/releases/tag/v3.4.2" target="_blank"> 
Source </a><OutboundLink /></p>
<p>Helm v3.4.2 is a patch release. Users are encouraged to upgrade for the best experience.</p>
<p>The community keeps growing, and we'd love to see you there!</p>
<ul>
<li>Join the discussion in <a href="https://kubernetes.slack.com" rel="nofollow">Kubernetes Slack</a>:
<ul>
<li>for questions and just to hang out</li>
<li>for discussing PRs, code, and bugs</li>
</ul>
</li>
<li>Hang out at the Public Developer Call: Thursday, 9:30 Pacific via <a href="https://zoom.us/j/696660622" rel="nofollow">Zoom</a></li>
<li>Test, debug, and contribute charts: <a href="https://github.com/helm/charts">GitHub/helm/charts</a></li>
</ul>
<h2>Installation and Upgrading</h2>
<p>Download Helm v3.4.2. The common platform binaries are here:</p>
<ul>
<li><a href="https://get.helm.sh/helm-v3.4.2-darwin-amd64.tar.gz" rel="nofollow">MacOS amd64</a> (<a href="https://get.helm.sh/helm-v3.4.2-darwin-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / c33b7ee72b0006f23b33f5032b531dd609fff7b08a4324f9ba07722a4f3fec9a)</li>
<li><a href="https://get.helm.sh/helm-v3.4.2-linux-amd64.tar.gz" rel="nofollow">Linux amd64</a> (<a href="https://get.helm.sh/helm-v3.4.2-linux-amd64.tar.gz.sha256sum" rel="nofollow">checksum</a> / cacde7768420dd41111a4630e047c231afa01f67e49cc0c6429563e024da4b98)</li>
<li><a href="https://get.helm.sh/helm-v3.4.2-linux-arm.tar.gz" rel="nofollow">Linux arm</a> (<a href="https://get.helm.sh/helm-v3.4.2-linux-arm.tar.gz.sha256sum" rel="nofollow">checksum</a> / feafaebe64f0fa4228d5b2014defb462d1898fcddbd33a1c34531cbad24e159f)</li>
<li><a href="https://get.helm.sh/helm-v3.4.2-linux-arm64.tar.gz" rel="nofollow">Linux arm64</a> (<a href="https://get.helm.sh/helm-v3.4.2-linux-arm64.tar.gz.sha256sum" rel="nofollow">checksum</a> / 486cad35b9ac1da88781847f2fcaaaed729e44705eb42593322e4b52d0f2c1a1)</li>
<li><a href="https://get.helm.sh/helm-v3.4.2-linux-386.tar.gz" rel="nofollow">Linux i386</a> (<a href="https://get.helm.sh/helm-v3.4.2-linux-386.tar.gz.sha256sum" rel="nofollow">checksum</a> / c7a4872d7409bc2840a2c82380b2abbd94b69b4264fad08ed8bb2a4cc617118e)</li>
<li><a href="https://get.helm.sh/helm-v3.4.2-linux-ppc64le.tar.gz" rel="nofollow">Linux ppc64le</a> (<a href="https://get.helm.sh/helm-v3.4.2-linux-ppc64le.tar.gz.sha256sum" rel="nofollow">checksum</a> / 52062596e5625a3238c6b967d31cf6ec1f0fd5926d2443a1179aeb91ed14d539)</li>
<li><a href="https://get.helm.sh/helm-v3.4.2-linux-s390x.tar.gz" rel="nofollow">Linux s390x</a> (<a href="https://get.helm.sh/helm-v3.4.2-linux-s390x.tar.gz.sha256sum" rel="nofollow">checksum</a> / c33b7ee72b0006f23b33f5032b531dd609fff7b08a4324f9ba07722a4f3fec9a)</li>
<li><a href="https://get.helm.sh/helm-v3.4.2-windows-amd64.zip" rel="nofollow">Windows amd64</a> (<a href="https://get.helm.sh/helm-v3.4.2-windows-amd64.zip.sha256sum" rel="nofollow">checksum</a> / 76ff3f8c21c9af5b80abdd87ec07629ad88dbfe6206decc4d3024f26398554b9)</li>
</ul>
<p>This release was signed with <code>672C 657B E06B 4B30 969C 4A57 4614 49C2 5E36 B98E </code> and can be found at <a class="user-mention" href="https://github.com/mattfarina">@mattfarina</a> <a href="https://keybase.io/mattfarina" rel="nofollow">keybase account</a>. Please use the attached signatures for verifying this release using <code>gpg</code>.</p>
<p>The <a href="https://helm.sh/docs/intro/quickstart/" rel="nofollow">Quickstart Guide</a> will get you going from there. For <strong>upgrade instructions</strong> or detailed installation notes, check the <a href="https://helm.sh/docs/intro/install/" rel="nofollow">install guide</a>. You can also use a <a href="https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3" rel="nofollow">script to install</a> on any system with <code>bash</code>.</p>
<h2>What's Next</h2>
<ul>
<li>3.5.0 is the next feature release. This will be released on January 13. 2021.</li>
</ul>
<h2>Changelog</h2>
<ul>
<li>Updating to Kubernetes 1.19.4 package versions <a class="commit-link" href="https://github.com/helm/helm/commit/23dd3af5e19a02d4f4baa5b2f242645a1a3af629"><tt>23dd3af</tt></a> (Matt Farina)</li>
<li>fix: ingress path issue <a class="commit-link" href="https://github.com/helm/helm/commit/3ba833f5ad97c157a3a27b9985d6f0c660db901e"><tt>3ba833f</tt></a> (Salim Salaues)</li>
</ul>
