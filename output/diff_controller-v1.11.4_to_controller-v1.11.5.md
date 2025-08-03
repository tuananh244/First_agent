# 🔍 Code Diff Analysis: `controller-v1.11.4` → `controller-v1.11.5`
📅 Generated at: 2025-08-01T03:10:11.744166

## 📌 Git Log Summary
```bash
795b6964d|Marco Ebert|2025-03-25|Release controller v1.11.5 & chart v4.11.5. (#13074)
97ffeeee0|Marco Ebert|2025-03-25|Images: Trigger controller build. (#13072)
e6716b13f|Marco Ebert|2025-03-25|Controller: Several security fixes. (#13070)
cd854d91e|Marco Ebert|2025-03-24|Chart: Bump Kube Webhook CertGen. (#13067)
138ade74b|k8s-infra-cherrypick-robot|2025-03-24|Tests & Docs: Bump images. (#13065)
4d3318ffd|k8s-infra-cherrypick-robot|2025-03-24|Images: Trigger other builds (2/2). (#13060)
8bd6f4bf3|k8s-infra-cherrypick-robot|2025-03-24|Images: Trigger other builds (1/2). (#13058)
6718acf2d|Marco Ebert|2025-03-24|Tests: Bump Test Runner to v1.3.1. (#13049)
19cfa1aee|Marco Ebert|2025-03-24|Images: Trigger Test Runner build. (#13046)
9c32f26cc|Marco Ebert|2025-03-24|Images: Bump `NGINX_BASE` to v0.3.1. (#13041)
aa97baa2d|Marco Ebert|2025-03-24|Images: Trigger NGINX build. (#13040)
ebf2c460c|Marco Ebert|2025-03-24|Go: Update dependencies. (#13037)
2da8520b9|k8s-infra-cherrypick-robot|2025-03-24|Bump github.com/opencontainers/runc from 1.2.5 to 1.2.6 in the go group across 1 directory (#13034)
781ab63e0|Marco Ebert|2025-03-23|CI: Update KIND to v1.32.3. (#13030)
44e20ccb2|k8s-infra-cherrypick-robot|2025-03-23|Bump github.com/onsi/ginkgo/v2 from 2.23.0 to 2.23.3 (#13028)
ee6686be0|k8s-infra-cherrypick-robot|2025-03-23|CI: Update Kubernetes to v1.32.3. (#13026)
2d16da718|k8s-infra-cherrypick-robot|2025-03-23|Bump the actions group with 5 updates (#13024)
a1945904d|k8s-infra-cherrypick-robot|2025-03-23|Images: Rework. (3/3) (#13017)
17fb5c9fd|k8s-infra-cherrypick-robot|2025-03-23|Images: Rework. (2/3) (#13012)
79c996ed6|k8s-infra-cherrypick-robot|2025-03-23|Images: Rework. (1/3) (#13015)
133bf2190|k8s-infra-cherrypick-robot|2025-03-22|Custom Error Pages: Accept first of many MIME types. (#13007)
034449403|k8s-infra-cherrypick-robot|2025-03-17|Bump dorny/test-reporter from 1.9.1 to 2.0.0 (#12990)
ffd547ce3|k8s-infra-cherrypick-robot|2025-03-17|Bump github.com/prometheus/common from 0.62.0 to 0.63.0 (#12988)
67f035d0f|k8s-infra-cherrypick-robot|2025-03-17|Bump the go group across 3 directories with 9 updates (#12986)
b0d3da82a|k8s-infra-cherrypick-robot|2025-03-17|Bump the actions group with 3 updates (#12983)
bf7d5b202|k8s-infra-cherrypick-robot|2025-03-15|Docs: Use `enable-global-auth` annotation instead of non-existing ConfigMap option. (#12977)
900e460cf|k8s-infra-cherrypick-robot|2025-03-11|Bump github/codeql-action from 3.28.10 to 3.28.11 in the actions group (#12969)
eba5025c4|Marco Ebert|2025-03-09|Go: Update dependencies. (#12964)
9ce48ce63|k8s-infra-cherrypick-robot|2025-03-09|Bump github.com/onsi/ginkgo/v2 from 2.22.2 to 2.23.0 (#12959)
14946c4ca|k8s-infra-cherrypick-robot|2025-03-09|Docs: Update link to `values.yaml`. (#12961)
6b6579c59|k8s-infra-cherrypick-robot|2025-03-06|Bump golang.org/x/crypto from 0.35.0 to 0.36.0 (#12956)
c6c5b48b6|k8s-infra-cherrypick-robot|2025-03-06|fix DNS issues with unresolvable backends with ExternalName (#12952)
1301ba724|k8s-infra-cherrypick-robot|2025-03-05|Go: Bump to v1.24.1. (#12943)
19c0e107e|k8s-infra-cherrypick-robot|2025-03-05|Bump the go group across 2 directories with 1 update (#12939)
1f53d60fa|k8s-infra-cherrypick-robot|2025-03-05|Bump google.golang.org/grpc from 1.70.0 to 1.71.0 (#12936)
41f41ccac|Marco Ebert|2025-03-04|CI: Update KIND images. (#12932)
7acafd6a9|k8s-infra-cherrypick-robot|2025-03-04|Test: Remove gRPC Fortune Teller. (#12930)
fd1fecc43|k8s-infra-cherrypick-robot|2025-03-03|Bump golang.org/x/crypto from 0.34.0 to 0.35.0 (#12924)
e7d5e2fb4|k8s-infra-cherrypick-robot|2025-03-03|Bump the actions group with 3 updates (#12922)
e84dac05f|k8s-infra-cherrypick-robot|2025-03-01|NGINX: Update ModSecurity. (#12916)
662a0776b|k8s-infra-cherrypick-robot|2025-02-28|Development: Update KIND images. (#12910)
8c2f46f2d|k8s-infra-cherrypick-robot|2025-02-24|Bump github.com/prometheus/client_golang from 1.20.5 to 1.21.0 (#12901)
4ed05e40f|k8s-infra-cherrypick-robot|2025-02-24|Config: Remove notes about future defaults. (#12899)
378a91eab|k8s-infra-cherrypick-robot|2025-02-24|Bump golang.org/x/crypto from 0.33.0 to 0.34.0 (#12894)
c53f60fc8|k8s-infra-cherrypick-robot|2025-02-24|Bump github.com/prometheus/client_golang from 1.20.5 to 1.21.0 in /images/custom-error-pages/rootfs (#12891)
9dcb389bf|k8s-infra-cherrypick-robot|2025-02-24|Bump the actions group with 4 updates (#12890)
12a09b31c|k8s-infra-cherrypick-robot|2025-02-17|Bump github.com/spf13/cobra from 1.8.1 to 1.9.1 (#12868)
65d6d463e|k8s-infra-cherrypick-robot|2025-02-17|Bump the go group across 3 directories with 11 updates (#12866)
b90e05944|k8s-infra-cherrypick-robot|2025-02-17|Bump the actions group with 2 updates (#12864)
be1d67582|k8s-infra-cherrypick-robot|2025-02-17|Bump github.com/spf13/cobra from 1.8.1 to 1.9.1 in /images/kube-webhook-certgen/rootfs (#12862)
a3a05746b|k8s-infra-cherrypick-robot|2025-02-15|Images: Update `kubectl` to v1.32.2. (#12855)
97b93720b|k8s-infra-cherrypick-robot|2025-02-14|Development: Update Kubernetes to v1.32.0. (#12854)
f8df661b4|k8s-infra-cherrypick-robot|2025-02-14|CI: Update `kubectl` to v1.32.2. (#12852)
458051a51|k8s-infra-cherrypick-robot|2025-02-14|Images: Migrate to AR. (2/2) (#12850)
8b8996a2f|k8s-infra-cherrypick-robot|2025-02-14|Images: Migrate to AR. (1/2) (#12847)
ad75df8a5|k8s-infra-cherrypick-robot|2025-02-10|Bump the actions group with 4 updates (#12815)
f7d4e2b3e|k8s-infra-cherrypick-robot|2025-02-10|Bump golang.org/x/crypto from 0.32.0 to 0.33.0 (#12813)
2c026151e|k8s-infra-cherrypick-robot|2025-02-08|Docs: Migrate to AR. (#12808)
b3c2c188f|k8s-infra-cherrypick-robot|2025-02-07|Docs: Enable code copy button. (#12806)
4d6d23774|k8s-infra-cherrypick-robot|2025-02-05|Go: Bump to v1.23.6. (#12800)
41cfe9a77|k8s-infra-cherrypick-robot|2025-02-04|CI: Update Artifact Hub to v1.20.0. (#12794)
5b0b60233|k8s-infra-cherrypick-robot|2025-02-04|Images: Update `kubectl` to v1.31.5. (#12792)
595bdcab6|k8s-infra-cherrypick-robot|2025-02-04|CI: Update `kubectl` to v1.31.5. (#12790)
a0f4a1735|k8s-infra-cherrypick-robot|2025-02-03|Development: Bump Kubernetes to v1.31.4. (#12783)
93aa96cde|k8s-infra-cherrypick-robot|2025-02-03|Go: Replace `golang.org/x/exp/slices` with `slices`. (#12780)
ca50eaa2e|k8s-infra-cherrypick-robot|2025-02-03|Bump the actions group with 2 updates (#12778)
a0bddb0bb|k8s-infra-cherrypick-robot|2025-02-03|Bump the go group across 2 directories with 1 update (#12776)
1fb829651|k8s-infra-cherrypick-robot|2025-02-03|Docs: Fix character format. (#12774)
6a3960b69|k8s-infra-cherrypick-robot|2025-01-27|Bump google.golang.org/grpc from 1.69.4 to 1.70.0 (#12761)
7172a5c46|k8s-infra-cherrypick-robot|2025-01-27|Bump sigs.k8s.io/controller-runtime from 0.20.0 to 0.20.1 in the go group across 1 directory (#12759)
debcfe385|k8s-infra-cherrypick-robot|2025-01-27|Bump the actions group with 5 updates (#12757)
2b849914b|k8s-infra-cherrypick-robot|2025-01-22|Docs: Improve bare-metal setup. (#12745)
63f63b0c0|k8s-infra-cherrypick-robot|2025-01-21|Build: Always use local `tmp` dir on macOS. (#12742)
423125eca|k8s-infra-cherrypick-robot|2025-01-21|Development: Bump Kubernetes to v1.31.4. (#12740)
55bf35416|k8s-infra-cherrypick-robot|2025-01-21|Images: Bump `gcb-docker-gcloud` to v20250116-2a05ea7e3d. (#12737)
736d4b36b|k8s-infra-cherrypick-robot|2025-01-21|Go: Bump to v1.23.5. (#12735)
ff9c9399c|k8s-infra-cherrypick-robot|2025-01-20|Bump sigs.k8s.io/controller-runtime from 0.19.4 to 0.20.0 (#12731)
f9d036488|k8s-infra-cherrypick-robot|2025-01-20|Bump github.com/prometheus/common from 0.61.0 to 0.62.0 (#12729)
c6d5b00a5|k8s-infra-cherrypick-robot|2025-01-20|Bump the go group across 3 directories with 9 updates (#12727)
90106cea1|k8s-infra-cherrypick-robot|2025-01-20|Bump golangci/golangci-lint-action from 6.1.1 to 6.2.0 in the actions group (#12724)
eea7014cf|k8s-infra-cherrypick-robot|2025-01-17|Docs: Clarify rate limits are per ingress controller replica. (#12716)
1e03161e8|k8s-infra-cherrypick-robot|2025-01-16|Go: Stop using workspace. (#12713)
18715e51e|k8s-infra-cherrypick-robot|2025-01-13|Bump google.golang.org/grpc from 1.69.2 to 1.69.4 in the go group across 1 directory (#12700)
57682a71e|Marco Ebert|2025-01-13|Chart: Bump Kube Webhook CertGen. (#12697)
c4eb35eb3|k8s-infra-cherrypick-robot|2025-01-13|Tests & Docs: Bump images. (#12695)
57cf9c359|k8s-infra-cherrypick-robot|2025-01-12|Images: Trigger other builds (2/2). (#12691)
cdaf3f4e5|k8s-infra-cherrypick-robot|2025-01-12|Images: Trigger other builds (1/2). (#12687)
ecd7d7257|Marco Ebert|2025-01-12|Tests: Bump Test Runner to v20250112-01b7af21. (#12685)
5e162204e|Marco Ebert|2025-01-12|Images: Trigger Test Runner build. (#12682)
354cca61b|Marco Ebert|2025-01-12|Images: Bump `NGINX_BASE` to v0.3.0. (#12679)
c54573f05|Marco Ebert|2025-01-11|Images: Trigger NGINX build. (#12675)
1a5c07fcc|k8s-infra-cherrypick-robot|2025-01-11|NGINX: Align quotes. (#12670)
6d97ff409|k8s-infra-cherrypick-robot|2025-01-10|Annotations: Deny newlines. (#12666)
ea603be52|k8s-infra-cherrypick-robot|2025-01-10|Bump the actions group with 3 updates (#12665)
7acb412db|k8s-infra-cherrypick-robot|2025-01-10|Bump the go group across 1 directory with 3 updates (#12663)
fca895f66|k8s-infra-cherrypick-robot|2025-01-10|Bump golang.org/x/crypto from 0.31.0 to 0.32.0 (#12660)
5802ecc4b|k8s-infra-cherrypick-robot|2025-01-09|Annotations: Reload on custom header changes. (#12653)
96cda8d69|k8s-infra-cherrypick-robot|2025-01-09|NGINX: Bump ModSecurity. (#12650)
e10cf1b70|Marco Ebert|2025-01-06|NGINX: Bump OpenTelemetry. (#12632)
920f1ebe0|k8s-infra-cherrypick-robot|2025-01-06|Bump github.com/onsi/ginkgo/v2 from 2.22.1 to 2.22.2 (#12629)
```

## 🧩 Diff Summary (all files changed)
```diff
M	.github/workflows/chart.yaml
M	.github/workflows/ci.yaml
M	.github/workflows/golangci-lint.yml
M	.github/workflows/images.yaml
M	.github/workflows/junit-reports.yaml
M	.github/workflows/plugin.yaml
M	.github/workflows/scorecards.yml
M	.github/workflows/stale.yaml
M	.github/workflows/vulnerability-scans.yaml
M	.github/workflows/zz-tmpl-images.yaml
M	.github/workflows/zz-tmpl-k8s-e2e.yaml
M	.golangci.yml
M	GOLANG_VERSION
M	MANUAL_RELEASE.md
M	Makefile
M	NEW_CONTRIBUTOR.md
M	NGINX_BASE
M	README.md
M	TAG
M	build/dev-env.sh
M	build/run-in-docker.sh
A	changelog/controller-1.11.5.md
M	charts/ingress-nginx/Chart.yaml
M	charts/ingress-nginx/README.md
A	charts/ingress-nginx/changelog/helm-chart-4.11.5.md
M	charts/ingress-nginx/values.yaml
M	cloudbuild.yaml
M	deploy/static/provider/aws/deploy.yaml
M	deploy/static/provider/aws/nlb-with-tls-termination/deploy.yaml
M	deploy/static/provider/baremetal/deploy.yaml
M	deploy/static/provider/cloud/deploy.yaml
M	deploy/static/provider/do/deploy.yaml
M	deploy/static/provider/exoscale/deploy.yaml
M	deploy/static/provider/kind/deploy.yaml
M	deploy/static/provider/oracle/deploy.yaml
M	deploy/static/provider/scw/deploy.yaml
M	docs/deploy/baremetal.md
M	docs/deploy/index.md
M	docs/e2e-tests.md
M	docs/examples/canary/README.md
M	docs/examples/customization/custom-errors/custom-default-backend.helm.values.yaml
M	docs/examples/customization/custom-errors/custom-default-backend.yaml
M	docs/examples/customization/external-auth-headers/echo-service.yaml
M	docs/examples/customization/jwt/README.md
M	docs/faq.md
M	docs/user-guide/miscellaneous.md
M	docs/user-guide/nginx-configuration/annotations.md
M	ginkgo_upgrade.md
M	go.mod
M	go.sum
D	go.work
D	go.work.sum
D	hack/init-buildx.sh
M	images/Makefile
M	images/README.md
M	images/cfssl/TAG
M	images/cfssl/cloudbuild.yaml
M	images/custom-error-pages/TAG
M	images/custom-error-pages/cloudbuild.yaml
M	images/custom-error-pages/rootfs/go.mod
M	images/custom-error-pages/rootfs/go.sum
M	images/custom-error-pages/rootfs/main.go
M	images/e2e-test-echo/TAG
M	images/e2e-test-echo/cloudbuild.yaml
M	images/ext-auth-example-authsvc/TAG
M	images/ext-auth-example-authsvc/rootfs/go.mod
M	images/ext-auth-example-authsvc/rootfs/go.sum
M	images/fastcgi-helloserver/TAG
M	images/fastcgi-helloserver/cloudbuild.yaml
M	images/go-grpc-greeter-server/TAG
M	images/httpbun/TAG
M	images/httpbun/cloudbuild.yaml
M	images/kube-webhook-certgen/TAG
M	images/kube-webhook-certgen/cloudbuild.yaml
M	images/kube-webhook-certgen/rootfs/go.mod
M	images/kube-webhook-certgen/rootfs/go.sum
M	images/nginx/Makefile
M	images/nginx/TAG
M	images/nginx/cloudbuild.yaml
M	images/nginx/rootfs/Dockerfile
M	images/nginx/rootfs/build.sh
M	images/test-runner/Makefile
M	images/test-runner/TAG
M	images/test-runner/cloudbuild.yaml
M	images/test-runner/rootfs/Dockerfile
M	internal/ingress/annotations/auth/main.go
M	internal/ingress/annotations/customheaders/main.go
M	internal/ingress/annotations/mirror/main_test.go
M	internal/ingress/annotations/parser/validators.go
M	internal/ingress/annotations/parser/validators_test.go
M	internal/ingress/controller/config/config.go
M	internal/ingress/controller/controller.go
M	internal/ingress/controller/controller_test.go
M	internal/ingress/controller/template/template.go
M	internal/ingress/defaults/main.go
M	internal/ingress/metric/collectors/nginx_status_test.go
M	magefiles/go.mod
M	magefiles/go.sum
M	mkdocs.yml
M	pkg/apis/ingress/types_equals.go
M	rootfs/etc/nginx/lua/balancer.lua
M	rootfs/etc/nginx/template/nginx.tmpl
M	test/e2e-image/Makefile
M	test/e2e/HTTPBUN_IMAGE
M	test/e2e/admission/admission.go
M	test/e2e/annotations/grpc.go
M	test/e2e/annotations/mirror.go
M	test/e2e/framework/deployment.go
M	test/e2e/framework/fastcgi_helloserver.go
D	test/e2e/framework/grpc_fortune_teller.go
M	test/e2e/run-chart-test.sh
M	test/e2e/run-kind-e2e.sh
M	test/e2e/settings/ocsp/ocsp.go
M	test/manifests/configuration-a.json
M	test/manifests/configuration-b.json
```

## 🧠 Commit-wise Changes
### 🔸 Commit `920f1ebe051dc94fd8ba0ceaac7a0c710abdc007` - Bump github.com/onsi/ginkgo/v2 from 2.22.1 to 2.22.2 (#12629) (2025-01-06) by `k8s-infra-cherrypick-robot`
- `build/run-in-docker.sh` [M]
```diff
diff --git a/build/run-in-docker.sh b/build/run-in-docker.sh
index 03cc3de73..e191eda65 100755
--- a/build/run-in-docker.sh
+++ b/build/run-in-docker.sh
@@ -82,7 +82,7 @@ if [[ "$DOCKER_IN_DOCKER_ENABLED" == "true" ]]; then
   echo "..reached DIND check TRUE block, inside run-in-docker.sh"
   echo "FLAGS=$FLAGS"
   #go env
-  go install -mod=mod github.com/onsi/ginkgo/v2/ginkgo@v2.22.1
+  go install -mod=mod github.com/onsi/ginkgo/v2/ginkgo@v2.22.2
   find / -type f -name ginkgo 2>/dev/null
   which ginkgo
   /bin/bash -c "${FLAGS}"
```
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 7cced6117..71e1b6925 100644
--- a/go.mod
+++ b/go.mod
@@ -14,7 +14,7 @@ require (
 	github.com/mitchellh/mapstructure v1.5.0
 	github.com/moul/pb v0.0.0-20220425114252-bca18df4138c
 	github.com/ncabatoff/process-exporter v0.8.4
-	github.com/onsi/ginkgo/v2 v2.22.1
+	github.com/onsi/ginkgo/v2 v2.22.2
 	github.com/opencontainers/runc v1.2.3
 	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2
 	github.com/prometheus/client_golang v1.20.5
@@ -123,7 +123,7 @@ require (
 	golang.org/x/time v0.7.0 // indirect
 	golang.org/x/tools v0.28.0 // indirect
 	google.golang.org/genproto/googleapis/rpc v0.0.0-20241015192408-796eee8c2d53 // indirect
-	google.golang.org/protobuf v1.35.2 // indirect
+	google.golang.org/protobuf v1.36.1 // indirect
 	gopkg.in/go-playground/assert.v1 v1.2.1 // indirect
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 53b639700..5fb9377f0 100644
--- a/go.sum
+++ b/go.sum
@@ -163,12 +163,12 @@ github.com/onsi/ginkgo v1.6.0/go.mod h1:lLunBs/Ym6LB5Z9jYTR76FiuTmxDTDusOGeTQH+W
 github.com/onsi/ginkgo v1.12.1/go.mod h1:zj2OWP4+oCPe1qIXoGWkgMRwljMUYCdkwsT2108oapk=
 github.com/onsi/ginkgo v1.16.5 h1:8xi0RTUf59SOSfEtZMvwTvXYMzG4gV23XVHOZiXNtnE=
 github.com/onsi/ginkgo v1.16.5/go.mod h1:+E8gABHa3K6zRBolWtd+ROzc/U5bkGt0FwiG042wbpU=
-github.com/onsi/ginkgo/v2 v2.22.1 h1:QW7tbJAUDyVDVOM5dFa7qaybo+CRfR7bemlQUN6Z8aM=
-github.com/onsi/ginkgo/v2 v2.22.1/go.mod h1:S6aTpoRsSq2cZOd+pssHAlKW/Q/jZt6cPrPlnj4a1xM=
+github.com/onsi/ginkgo/v2 v2.22.2 h1:/3X8Panh8/WwhU/3Ssa6rCKqPLuAkVY2I0RoyDLySlU=
+github.com/onsi/ginkgo/v2 v2.22.2/go.mod h1:oeMosUL+8LtarXBHu/c0bx2D/K9zyQ6uX3cTyztHwsk=
 github.com/onsi/gomega v1.7.1/go.mod h1:XdKZgCCFLUoM/7CFJVPcG8C1xQ1AJ0vpAezJrB7JYyY=
 github.com/onsi/gomega v1.10.1/go.mod h1:iN09h71vgCQne3DLsj+A5owkum+a2tYe+TOCB1ybHNo=
-github.com/onsi/gomega v1.36.1 h1:bJDPBO7ibjxcbHMgSCoo4Yj18UWbKDlLwX1x9sybDcw=
-github.com/onsi/gomega v1.36.1/go.mod h1:PvZbdDc8J6XJEpDK4HCuRBm8a6Fzp9/DmhC9C7yFlog=
+github.com/onsi/gomega v1.36.2 h1:koNYke6TVk6ZmnyHrCXba/T/MoLBXFjeC1PtvYgw0A8=
+github.com/onsi/gomega v1.36.2/go.mod h1:DdwyADRjrc825LhMEkD76cHR5+pUnjhUN8GlHlRPHzY=
 github.com/opencontainers/runc v1.2.3 h1:fxE7amCzfZflJO2lHXf4y/y8M1BoAqp+FVmG19oYB80=
 github.com/opencontainers/runc v1.2.3/go.mod h1:nSxcWUydXrsBZVYNSkTjoQ/N6rcyTtn+1SD5D4+kRIM=
... (truncated)
```
- `go.work.sum` [M]
```diff
diff --git a/go.work.sum b/go.work.sum
index 825d0335a..0bc5d32bc 100644
--- a/go.work.sum
+++ b/go.work.sum
@@ -51,7 +51,6 @@ github.com/golang/glog v1.2.2/go.mod h1:6AhwSGph0fcJtXVM/PEHPqZlFeoLxhs7/t5UDAwm
 github.com/golang/groupcache v0.0.0-20210331224755-41bb18bfe9da/go.mod h1:cIg4eruTrX1D+g88fzRXU5OdNfaM+9IcxsU14FzY7Hc=
 github.com/golang/snappy v0.0.4/go.mod h1:/XxbfmMg8lxefKM7IXC3fBNl/7bRcc72aCRzEWrmP2Q=
 github.com/google/cel-go v0.22.0/go.mod h1:BuznPXXfQDpXKWQ9sPW3TzlAJN5zzFe+i9tIs0yC4s8=
-github.com/google/pprof v0.0.0-20240827171923-fa2c70bbbfe5/go.mod h1:vavhavw2zAxS5dIdcRluK6cSGGPlZynqzFM8NdvU144=
 github.com/google/pprof v0.0.0-20241029153458-d1b30febd7db/go.mod h1:vavhavw2zAxS5dIdcRluK6cSGGPlZynqzFM8NdvU144=
 github.com/gorilla/websocket v1.5.0/go.mod h1:YR8l580nyteQvAITg2hZ9XVh4b55+EU/adAjf1fMHhE=
 github.com/grpc-ecosystem/go-grpc-middleware v1.3.0/go.mod h1:z0ButlSOZa5vEBq9m2m2hlwIgKw+rp3sdCBRoJY+30Y=
@@ -78,8 +77,8 @@ github.com/mwitkow/go-conntrack v0.0.0-20190716064945-2f068394615f/go.mod h1:qRW
 github.com/mxk/go-flowrate v0.0.0-20140419014527-cca7078d478f/go.mod h1:ZdcZmHo+o7JKHSa8/e818NopupXU1YMK5fe1lsApnBw=
 github.com/ncabatoff/fakescraper v0.0.0-20201102132415-4b37ba603d65/go.mod h1:Tx6UMSMyIsjLG/VU/F6xA1+0XI+/f9o1dGJnf1l+bPg=
 github.com/nwaples/rardecode v1.1.3/go.mod h1:5DzqNKiOdpKKBH87u8VlvAnPZMXcGRhxWkRpHbbfGS0=
-github.com/onsi/ginkgo/v2 v2.20.1/go.mod h1:lG9ey2Z29hR41WMVthyJBGUBcBhGOtoPF2VFMvBXFCI=
 github.com/onsi/ginkgo/v2 v2.21.0/go.mod h1:7Du3c42kxCUegi0IImZ1wUQzMBVecgIHjR1C+NkhLQo=
+github.com/onsi/ginkgo/v2 v2.22.1/go.mod h1:S6aTpoRsSq2cZOd+pssHAlKW/Q/jZt6cPrPlnj4a1xM=
 github.com/onsi/gomega v1.35.1/go.mod h1:PvZbdDc8J6XJEpDK4HCuRBm8a6Fzp9/DmhC9C7yFlog=
... (truncated)
```
- `images/kube-webhook-certgen/rootfs/go.mod` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.mod b/images/kube-webhook-certgen/rootfs/go.mod
index 46d7747c5..d1fcf4909 100644
--- a/images/kube-webhook-certgen/rootfs/go.mod
+++ b/images/kube-webhook-certgen/rootfs/go.mod
@@ -33,8 +33,8 @@ require (
 	github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd // indirect
 	github.com/modern-go/reflect2 v1.0.2 // indirect
 	github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 // indirect
-	github.com/onsi/ginkgo/v2 v2.22.1 // indirect
-	github.com/onsi/gomega v1.36.1 // indirect
+	github.com/onsi/ginkgo/v2 v2.22.2 // indirect
+	github.com/onsi/gomega v1.36.2 // indirect
 	github.com/pkg/errors v0.9.1 // indirect
 	github.com/spf13/pflag v1.0.5 // indirect
 	github.com/x448/float16 v0.8.4 // indirect
@@ -44,7 +44,7 @@ require (
 	golang.org/x/term v0.27.0 // indirect
 	golang.org/x/text v0.21.0 // indirect
 	golang.org/x/time v0.7.0 // indirect
-	google.golang.org/protobuf v1.35.1 // indirect
... (truncated)
```
- `images/kube-webhook-certgen/rootfs/go.sum` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.sum b/images/kube-webhook-certgen/rootfs/go.sum
index fee4d4e02..429552b0e 100644
--- a/images/kube-webhook-certgen/rootfs/go.sum
+++ b/images/kube-webhook-certgen/rootfs/go.sum
@@ -56,10 +56,10 @@ github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 h1:C3w9PqII01/Oq
 github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822/go.mod h1:+n7T8mK8HuQTcFwEeznm/DIxMOiR9yIdICNftLE1DvQ=
 github.com/onrik/logrus v0.11.0 h1:pu+BCaWL36t0yQaj/2UHK2erf88dwssAKOT51mxPUVs=
 github.com/onrik/logrus v0.11.0/go.mod h1:fO2vlZwIdti6PidD3gV5YKt9Lq5ptpnP293RAe1ITwk=
-github.com/onsi/ginkgo/v2 v2.22.1 h1:QW7tbJAUDyVDVOM5dFa7qaybo+CRfR7bemlQUN6Z8aM=
-github.com/onsi/ginkgo/v2 v2.22.1/go.mod h1:S6aTpoRsSq2cZOd+pssHAlKW/Q/jZt6cPrPlnj4a1xM=
-github.com/onsi/gomega v1.36.1 h1:bJDPBO7ibjxcbHMgSCoo4Yj18UWbKDlLwX1x9sybDcw=
-github.com/onsi/gomega v1.36.1/go.mod h1:PvZbdDc8J6XJEpDK4HCuRBm8a6Fzp9/DmhC9C7yFlog=
+github.com/onsi/ginkgo/v2 v2.22.2 h1:/3X8Panh8/WwhU/3Ssa6rCKqPLuAkVY2I0RoyDLySlU=
+github.com/onsi/ginkgo/v2 v2.22.2/go.mod h1:oeMosUL+8LtarXBHu/c0bx2D/K9zyQ6uX3cTyztHwsk=
+github.com/onsi/gomega v1.36.2 h1:koNYke6TVk6ZmnyHrCXba/T/MoLBXFjeC1PtvYgw0A8=
+github.com/onsi/gomega v1.36.2/go.mod h1:DdwyADRjrc825LhMEkD76cHR5+pUnjhUN8GlHlRPHzY=
 github.com/pkg/errors v0.9.1 h1:FEBLx1zS214owpjy7qsBeixbURkuhQAwrK5UwLGTwt4=
 github.com/pkg/errors v0.9.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
 github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
@@ -129,8 +129,8 @@ golang.org/x/xerrors v0.0.0-20190717185122-a985d3407aa7/go.mod h1:I/5z698sn9Ka8T
... (truncated)
```
- `images/test-runner/Makefile` [M]
```diff
diff --git a/images/test-runner/Makefile b/images/test-runner/Makefile
index b51293643..3db9a7977 100644
--- a/images/test-runner/Makefile
+++ b/images/test-runner/Makefile
@@ -59,7 +59,7 @@ image:
 		--build-arg YAML_LINT_VERSION=1.33.0 \
 		--build-arg YAMALE_VERSION=4.0.4 \
 		--build-arg HELM_VERSION=3.14.4 \
-		--build-arg GINKGO_VERSION=2.22.1 \
+		--build-arg GINKGO_VERSION=2.22.2 \
 		--build-arg GOLINT_VERSION=latest \
 		-t ${IMAGE}:${TAG} rootfs
 
@@ -80,7 +80,7 @@ build: ensure-buildx
 		--build-arg YAML_LINT_VERSION=1.33.0 \
 		--build-arg YAMALE_VERSION=4.0.4 \
 		--build-arg HELM_VERSION=3.14.4 \
-		--build-arg GINKGO_VERSION=2.22.1 \
+		--build-arg GINKGO_VERSION=2.22.2 \
 		--build-arg GOLINT_VERSION=latest \
... (truncated)
```
- `test/e2e/run-chart-test.sh` [M]
```diff
diff --git a/test/e2e/run-chart-test.sh b/test/e2e/run-chart-test.sh
index 144db41df..c8b079f84 100755
--- a/test/e2e/run-chart-test.sh
+++ b/test/e2e/run-chart-test.sh
@@ -78,7 +78,7 @@ fi
 
 if [ "${SKIP_IMAGE_CREATION:-false}" = "false" ]; then
   if ! command -v ginkgo &> /dev/null; then
-    go install github.com/onsi/ginkgo/v2/ginkgo@v2.22.1
+    go install github.com/onsi/ginkgo/v2/ginkgo@v2.22.2
   fi
   echo "[dev-env] building image"
   make -C ${DIR}/../../ clean-image build image
```
- `test/e2e/run-kind-e2e.sh` [M]
```diff
diff --git a/test/e2e/run-kind-e2e.sh b/test/e2e/run-kind-e2e.sh
index 34096fea2..8202b6b83 100755
--- a/test/e2e/run-kind-e2e.sh
+++ b/test/e2e/run-kind-e2e.sh
@@ -96,7 +96,7 @@ fi
 
 if [ "${SKIP_E2E_IMAGE_CREATION}" = "false" ]; then
   if ! command -v ginkgo &> /dev/null; then
-    go install github.com/onsi/ginkgo/v2/ginkgo@v2.22.1
+    go install github.com/onsi/ginkgo/v2/ginkgo@v2.22.2
   fi
 
   echo "[dev-env] .. done building controller images"
```

### 🔸 Commit `e10cf1b709c9b3630124595b8654023395c61f98` - NGINX: Bump OpenTelemetry. (#12632) (2025-01-06) by `Marco Ebert`
- `images/nginx/rootfs/Dockerfile` [M]
```diff
diff --git a/images/nginx/rootfs/Dockerfile b/images/nginx/rootfs/Dockerfile
index 078630170..834a9bcf3 100644
--- a/images/nginx/rootfs/Dockerfile
+++ b/images/nginx/rootfs/Dockerfile
@@ -51,6 +51,8 @@ RUN apk update \
   tzdata \
   grpc-cpp \
   libprotobuf \
+  abseil-cpp-crc-cpu-detect \
+  abseil-cpp-vlog-config-internal \
   && ln -s /usr/local/nginx/sbin/nginx /sbin/nginx \
   && adduser -S -D -H -u 101 -h /usr/local/nginx \
   -s /sbin/nologin -G www-data -g www-data www-data \
```
- `images/nginx/rootfs/build.sh` [M]
```diff
diff --git a/images/nginx/rootfs/build.sh b/images/nginx/rootfs/build.sh
index 61469b32e..32f87b106 100755
--- a/images/nginx/rootfs/build.sh
+++ b/images/nginx/rootfs/build.sh
@@ -101,13 +101,14 @@ export LUA_RESTY_IPMATCHER_VERSION=3e93c53eb8c9884efe939ef070486a0e507cc5be
 # Check for recent changes: https://github.com/ElvinEfendi/lua-resty-global-throttle/compare/v0.2.0...main
 export LUA_RESTY_GLOBAL_THROTTLE_VERSION=v0.2.0
 
-# Check for recent changes:  https://github.com/microsoft/mimalloc/compare/v2.1.7...master
+# Check for recent changes: https://github.com/microsoft/mimalloc/compare/v2.1.7...master
 export MIMALOC_VERSION=v2.1.7
 
-# Check on https://github.com/open-telemetry/opentelemetry-cpp
-export OPENTELEMETRY_CPP_VERSION="v1.11.0"
-# Check on https://github.com/open-telemetry/opentelemetry-proto
-export OPENTELEMETRY_PROTO_VERSION="v1.1.0"
+# Check for recent changes: https://github.com/open-telemetry/opentelemetry-cpp/compare/v1.18.0...main
+export OPENTELEMETRY_CPP_VERSION="v1.18.0"
+
+# Check for recent changes: https://github.com/open-telemetry/opentelemetry-proto/compare/v1.5.0...main
... (truncated)
```

### 🔸 Commit `96cda8d697c20ec5c18f43a578ff3768b8d2afba` - NGINX: Bump ModSecurity. (#12650) (2025-01-09) by `k8s-infra-cherrypick-robot`
- `images/nginx/rootfs/build.sh` [M]
```diff
diff --git a/images/nginx/rootfs/build.sh b/images/nginx/rootfs/build.sh
index 32f87b106..5667afc17 100755
--- a/images/nginx/rootfs/build.sh
+++ b/images/nginx/rootfs/build.sh
@@ -38,11 +38,11 @@ export NGINX_SUBSTITUTIONS=e12e965ac1837ca709709f9a26f572a54d83430e
 # Check for recent changes: https://github.com/SpiderLabs/ModSecurity-nginx/compare/v1.0.3...master
 export MODSECURITY_VERSION=v1.0.3
 
-# Check for recent changes: https://github.com/SpiderLabs/ModSecurity/compare/v3.0.8...v3/master
-export MODSECURITY_LIB_VERSION=v3.0.12
+# Check for recent changes: https://github.com/SpiderLabs/ModSecurity/compare/v3.0.13...v3/master
+export MODSECURITY_LIB_VERSION=v3.0.13
 
-# Check for recent changes: https://github.com/coreruleset/coreruleset/compare/v3.3.5...v4.0/main
-export OWASP_MODSECURITY_CRS_VERSION=v4.4.0
+# Check for recent changes: https://github.com/coreruleset/coreruleset/compare/v4.10.0...main
+export OWASP_MODSECURITY_CRS_VERSION=v4.10.0
 
 # Check for recent changes: https://github.com/openresty/lua-nginx-module/compare/v0.10.26``...master
 export LUA_NGX_VERSION=v0.10.26
```

### 🔸 Commit `5802ecc4b5708e73f4a36ad2e6eb45bcca3aebc1` - Annotations: Reload on custom header changes. (#12653) (2025-01-09) by `k8s-infra-cherrypick-robot`
- `internal/ingress/annotations/customheaders/main.go` [M]
```diff
diff --git a/internal/ingress/annotations/customheaders/main.go b/internal/ingress/annotations/customheaders/main.go
index 774e9c3d3..bc0ef2eb5 100644
--- a/internal/ingress/annotations/customheaders/main.go
+++ b/internal/ingress/annotations/customheaders/main.go
@@ -18,6 +18,7 @@ package customheaders
 
 import (
 	"fmt"
+	"reflect"
 	"regexp"
 
 	"k8s.io/klog/v2"
@@ -35,6 +36,18 @@ type Config struct {
 	Headers map[string]string `json:"headers,omitempty"`
 }
 
+// Equal tests for equality between two Config types
+func (c1 *Config) Equal(c2 *Config) bool {
+	if c1 == c2 {
+		return true
... (truncated)
```
- `pkg/apis/ingress/types_equals.go` [M]
```diff
diff --git a/pkg/apis/ingress/types_equals.go b/pkg/apis/ingress/types_equals.go
index eeed9a06e..e8ef2af4d 100644
--- a/pkg/apis/ingress/types_equals.go
+++ b/pkg/apis/ingress/types_equals.go
@@ -470,6 +470,10 @@ func (l1 *Location) Equal(l2 *Location) bool {
 		return false
 	}
 
+	if !l1.CustomHeaders.Equal(&l2.CustomHeaders) {
+		return false
+	}
+
 	return true
 }
```
- `test/manifests/configuration-a.json` [M]
```diff
diff --git a/test/manifests/configuration-a.json b/test/manifests/configuration-a.json
index ba513c616..f9599d77c 100644
--- a/test/manifests/configuration-a.json
+++ b/test/manifests/configuration-a.json
@@ -302,7 +302,12 @@
 				"validationDepth": 0
 			},
 			"use-port-in-redirects": false,
-			"configuration-snippet": ""
+			"configuration-snippet": "",
+			"customHeaders": {
+				"headers": {
+					"Server": "HAL9000"
+				}
+			}
 		}]
 	}, {
 		"hostname": "dev.mycompany.com",
```
- `test/manifests/configuration-b.json` [M]
```diff
diff --git a/test/manifests/configuration-b.json b/test/manifests/configuration-b.json
index 9e40785b4..d2e71bb29 100644
--- a/test/manifests/configuration-b.json
+++ b/test/manifests/configuration-b.json
@@ -302,7 +302,12 @@
 				"validationDepth": 0
 			},
 			"use-port-in-redirects": false,
-			"configuration-snippet": ""
+			"configuration-snippet": "",
+			"customHeaders": {
+				"headers": {
+					"Server": "HAL9000"
+				}
+			}
 		}]
 	}, {
 		"hostname": "dev.mycompany.com",
```

### 🔸 Commit `fca895f66c257716d9699d909fdffe78dbe3ae16` - Bump golang.org/x/crypto from 0.31.0 to 0.32.0 (#12660) (2025-01-10) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 71e1b6925..fd8675851 100644
--- a/go.mod
+++ b/go.mod
@@ -25,7 +25,7 @@ require (
 	github.com/stretchr/testify v1.10.0
 	github.com/yudai/gojsondiff v1.0.0
 	github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30
-	golang.org/x/crypto v0.31.0
+	golang.org/x/crypto v0.32.0
 	golang.org/x/exp v0.0.0-20240719175910-8a7402abbf56
 	google.golang.org/grpc v1.69.2
 	google.golang.org/grpc/examples v0.0.0-20240223204917-5ccf176a08ab
@@ -117,8 +117,8 @@ require (
 	golang.org/x/net v0.33.0 // indirect
 	golang.org/x/oauth2 v0.24.0 // indirect
 	golang.org/x/sync v0.10.0 // indirect
-	golang.org/x/sys v0.28.0 // indirect
-	golang.org/x/term v0.27.0 // indirect
+	golang.org/x/sys v0.29.0 // indirect
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 5fb9377f0..03ff1b917 100644
--- a/go.sum
+++ b/go.sum
@@ -243,8 +243,8 @@ go.uber.org/zap v1.27.0/go.mod h1:GB2qFLM7cTU87MWRP2mPIjqfIDnGu+VIO4V/SdhGo2E=
 golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
 golang.org/x/crypto v0.0.0-20191011191535-87dc89f01550/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
 golang.org/x/crypto v0.0.0-20200622213623-75b288015ac9/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
-golang.org/x/crypto v0.31.0 h1:ihbySMvVjLAeSH1IbfcRTkD/iNscyz8rGzjF/E5hV6U=
-golang.org/x/crypto v0.31.0/go.mod h1:kDsLvtWBEx7MV9tJOj9bnXsPbxwJQ6csT/x4KIN4Ssk=
+golang.org/x/crypto v0.32.0 h1:euUpcYgM8WcP71gNpTqQCn6rC2t6ULUPiOzfWaXVVfc=
+golang.org/x/crypto v0.32.0/go.mod h1:ZnnJkOaASj8g0AjIduWNlq2NRxL0PlBrbKVyZ6V/Ugc=
 golang.org/x/exp v0.0.0-20240719175910-8a7402abbf56 h1:2dVuKD2vS7b0QIHQbpyTISPd0LeHDbnYEryqj5Q1ug8=
 golang.org/x/exp v0.0.0-20240719175910-8a7402abbf56/go.mod h1:M4RDyNAINzryxdtnbRXRL/OHtkFuWGRjvuhBJpk2IlY=
 golang.org/x/mod v0.2.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
@@ -281,10 +281,10 @@ golang.org/x/sys v0.0.0-20220520151302-bc2c85ada10a/go.mod h1:oPkhp1MJrh7nUepCBc
 golang.org/x/sys v0.0.0-20220715151400-c0bba94af5f8/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
 golang.org/x/sys v0.0.0-20220811171246-fbc7d0a398ab/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
 golang.org/x/sys v0.6.0/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
-golang.org/x/sys v0.28.0 h1:Fksou7UEQUWlKvIdsqzJmUmCX3cZuD2+P3XyyzwMhlA=
... (truncated)
```

### 🔸 Commit `7acb412db60e1e071b667c4732d6699a0bc48c4c` - Bump the go group across 1 directory with 3 updates (#12663) (2025-01-10) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index fd8675851..6335b6f89 100644
--- a/go.mod
+++ b/go.mod
@@ -13,9 +13,9 @@ require (
 	github.com/mitchellh/hashstructure/v2 v2.0.2
 	github.com/mitchellh/mapstructure v1.5.0
 	github.com/moul/pb v0.0.0-20220425114252-bca18df4138c
-	github.com/ncabatoff/process-exporter v0.8.4
+	github.com/ncabatoff/process-exporter v0.8.5
 	github.com/onsi/ginkgo/v2 v2.22.2
-	github.com/opencontainers/runc v1.2.3
+	github.com/opencontainers/runc v1.2.4
 	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2
 	github.com/prometheus/client_golang v1.20.5
 	github.com/prometheus/client_model v0.6.1
@@ -41,7 +41,7 @@ require (
 	k8s.io/component-base v0.32.0
 	k8s.io/klog/v2 v2.130.1
 	pault.ag/go/sniff v0.0.0-20200207005214-cf7e4d167732
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 03ff1b917..8de6c6bda 100644
--- a/go.sum
+++ b/go.sum
@@ -154,8 +154,8 @@ github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 h1:C3w9PqII01/Oq
 github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822/go.mod h1:+n7T8mK8HuQTcFwEeznm/DIxMOiR9yIdICNftLE1DvQ=
 github.com/ncabatoff/go-seq v0.0.0-20180805175032-b08ef85ed833 h1:t4WWQ9I797y7QUgeEjeXnVb+oYuEDQc6gLvrZJTYo94=
 github.com/ncabatoff/go-seq v0.0.0-20180805175032-b08ef85ed833/go.mod h1:0CznHmXSjMEqs5Tezj/w2emQoM41wzYM9KpDKUHPYag=
-github.com/ncabatoff/process-exporter v0.8.4 h1:qj0pWbP6AytVQ1fMYabRd5LnuV6NPh0O6WCfenPJT54=
-github.com/ncabatoff/process-exporter v0.8.4/go.mod h1:MxEOWl740VK/hlWycJkq91VrA2mI+U9Bvc1wuyAaxA4=
+github.com/ncabatoff/process-exporter v0.8.5 h1:Hk1sflgRWn0Xrh/OsupQLVVCTW01kv0YYrGxu7NvkmM=
+github.com/ncabatoff/process-exporter v0.8.5/go.mod h1:IZndG/m2Y++D90y99NhDJfg0SOkpbx/Fl6MlnBr4SC0=
 github.com/nxadm/tail v1.4.4/go.mod h1:kenIhsEOeOJmVchQTgglprH7qJGnHDVpk1VPCcaMI8A=
 github.com/nxadm/tail v1.4.8 h1:nPr65rt6Y5JFSKQO7qToXr7pePgD6Gwiw05lkbyAQTE=
 github.com/nxadm/tail v1.4.8/go.mod h1:+ncqLTQzXmGhMZNUePPaPqPvBxHAIsmXswZKocGu+AU=
@@ -169,8 +169,8 @@ github.com/onsi/gomega v1.7.1/go.mod h1:XdKZgCCFLUoM/7CFJVPcG8C1xQ1AJ0vpAezJrB7J
 github.com/onsi/gomega v1.10.1/go.mod h1:iN09h71vgCQne3DLsj+A5owkum+a2tYe+TOCB1ybHNo=
 github.com/onsi/gomega v1.36.2 h1:koNYke6TVk6ZmnyHrCXba/T/MoLBXFjeC1PtvYgw0A8=
 github.com/onsi/gomega v1.36.2/go.mod h1:DdwyADRjrc825LhMEkD76cHR5+pUnjhUN8GlHlRPHzY=
-github.com/opencontainers/runc v1.2.3 h1:fxE7amCzfZflJO2lHXf4y/y8M1BoAqp+FVmG19oYB80=
... (truncated)
```

### 🔸 Commit `ea603be5269616d33d0015b22f2815d247b2960c` - Bump the actions group with 3 updates (#12665) (2025-01-10) by `k8s-infra-cherrypick-robot`
- `.github/workflows/ci.yaml` [M]
```diff
diff --git a/.github/workflows/ci.yaml b/.github/workflows/ci.yaml
index 039651bbb..62be8beba 100644
--- a/.github/workflows/ci.yaml
+++ b/.github/workflows/ci.yaml
@@ -143,7 +143,7 @@ jobs:
           check-latest: true
 
       - name: Set up QEMU
-        uses: docker/setup-qemu-action@49b3bc8e6bdd4a60e6116a5414239cba5943d3cf # v3.2.0
+        uses: docker/setup-qemu-action@53851d14592bedcffcf25ea515637cff71ef929a # v3.3.0
 
       - name: Set up Docker Buildx
         id: buildx
@@ -186,7 +186,7 @@ jobs:
             | gzip > docker.tar.gz
 
       - name: cache
-        uses: actions/upload-artifact@6f51ac03b9356f520e9adb1b1b7802705f340c2b # v4.5.0
+        uses: actions/upload-artifact@65c4c4a1ddee5b72f698fdd19549f0f0fb45cf08 # v4.6.0
         with:
... (truncated)
```
- `.github/workflows/images.yaml` [M]
```diff
diff --git a/.github/workflows/images.yaml b/.github/workflows/images.yaml
index a3238604d..4a220ddf2 100644
--- a/.github/workflows/images.yaml
+++ b/.github/workflows/images.yaml
@@ -194,7 +194,7 @@ jobs:
       - name: Checkout
         uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
       - name: Set up QEMU
-        uses: docker/setup-qemu-action@49b3bc8e6bdd4a60e6116a5414239cba5943d3cf # v3.2.0
+        uses: docker/setup-qemu-action@53851d14592bedcffcf25ea515637cff71ef929a # v3.3.0
       - name: Set up Docker Buildx
         id: buildx
         uses: docker/setup-buildx-action@6524bf65af31da8d45b59e8c27de4bd072b392f5 # v3.8.0
```
- `.github/workflows/scorecards.yml` [M]
```diff
diff --git a/.github/workflows/scorecards.yml b/.github/workflows/scorecards.yml
index 916235c42..7d6424e5b 100644
--- a/.github/workflows/scorecards.yml
+++ b/.github/workflows/scorecards.yml
@@ -51,7 +51,7 @@ jobs:
       # Upload the results as artifacts (optional). Commenting out will disable uploads of run results in SARIF
       # format to the repository Actions tab.
       - name: "Upload artifact"
-        uses: actions/upload-artifact@6f51ac03b9356f520e9adb1b1b7802705f340c2b # v4.5.0
+        uses: actions/upload-artifact@65c4c4a1ddee5b72f698fdd19549f0f0fb45cf08 # v4.6.0
         with:
           name: SARIF file
           path: results.sarif
@@ -59,6 +59,6 @@ jobs:
 
       # Upload the results to GitHub's code scanning dashboard.
       - name: "Upload to code-scanning"
-        uses: github/codeql-action/upload-sarif@48ab28a6f5dbc2a99bf1e0131198dd8f1df78169 # v3.28.0
+        uses: github/codeql-action/upload-sarif@b6a472f63d85b9c78a3ac5e89422239fc15e9b3c # v3.28.1
         with:
... (truncated)
```
- `.github/workflows/vulnerability-scans.yaml` [M]
```diff
diff --git a/.github/workflows/vulnerability-scans.yaml b/.github/workflows/vulnerability-scans.yaml
index 3838dde75..6e4243f04 100644
--- a/.github/workflows/vulnerability-scans.yaml
+++ b/.github/workflows/vulnerability-scans.yaml
@@ -75,7 +75,7 @@ jobs:
 
       # This step checks out a copy of your repository.
       - name: Upload SARIF file
-        uses: github/codeql-action/upload-sarif@48ab28a6f5dbc2a99bf1e0131198dd8f1df78169 # v3.28.0
+        uses: github/codeql-action/upload-sarif@b6a472f63d85b9c78a3ac5e89422239fc15e9b3c # v3.28.1
         with:
           token: ${{ github.token }}
           # Path to SARIF file relative to the root of the repository
```
- `.github/workflows/zz-tmpl-k8s-e2e.yaml` [M]
```diff
diff --git a/.github/workflows/zz-tmpl-k8s-e2e.yaml b/.github/workflows/zz-tmpl-k8s-e2e.yaml
index bed0af207..b245886ae 100644
--- a/.github/workflows/zz-tmpl-k8s-e2e.yaml
+++ b/.github/workflows/zz-tmpl-k8s-e2e.yaml
@@ -50,7 +50,7 @@ jobs:
           make kind-e2e-test
 
       - name: Upload e2e junit-reports ${{ inputs.variation }}
-        uses: actions/upload-artifact@6f51ac03b9356f520e9adb1b1b7802705f340c2b # v4.5.0
+        uses: actions/upload-artifact@65c4c4a1ddee5b72f698fdd19549f0f0fb45cf08 # v4.6.0
         if: success() || failure()
         with:
           name: e2e-test-reports-${{ inputs.k8s-version }}${{ inputs.variation }}
```

### 🔸 Commit `6d97ff409e8e3fe783d282cd2d9617f29d7950b8` - Annotations: Deny newlines. (#12666) (2025-01-10) by `k8s-infra-cherrypick-robot`
- `internal/ingress/annotations/parser/validators.go` [M]
```diff
diff --git a/internal/ingress/annotations/parser/validators.go b/internal/ingress/annotations/parser/validators.go
index 31524508f..3c724a311 100644
--- a/internal/ingress/annotations/parser/validators.go
+++ b/internal/ingress/annotations/parser/validators.go
@@ -79,6 +79,8 @@ var (
 	// URLWithNginxVariableRegex defines a url that can contain nginx variables.
 	// It is a risky operation
 	URLWithNginxVariableRegex = regexp.MustCompile("^[" + extendedAlphaNumeric + urlEnabledChars + "$]*$")
+	// MaliciousRegex defines chars that are known to inject RCE
+	MaliciousRegex = regexp.MustCompile(`\r|\n`)
 )
 
 // ValidateArrayOfServerName validates if all fields on a Server name annotation are
@@ -113,6 +115,10 @@ func ValidateRegex(regex *regexp.Regexp, removeSpace bool) AnnotationValidator {
 		if !regex.MatchString(s) {
 			return fmt.Errorf("value %s is invalid", s)
 		}
+		if MaliciousRegex.MatchString(s) {
+			return fmt.Errorf("value %s contains malicious string", s)
+		}
... (truncated)
```
- `internal/ingress/annotations/parser/validators_test.go` [M]
```diff
diff --git a/internal/ingress/annotations/parser/validators_test.go b/internal/ingress/annotations/parser/validators_test.go
index 6c88342e4..49923ba76 100644
--- a/internal/ingress/annotations/parser/validators_test.go
+++ b/internal/ingress/annotations/parser/validators_test.go
@@ -65,6 +65,11 @@ func TestValidateArrayOfServerName(t *testing.T) {
 			value:   "something.com,lolo;xpto.com,nothing.com",
 			wantErr: true,
 		},
+		{
+			name:    "should deny names with malicous chars",
+			value:   "http://something.com/#;\nournewinjection",
+			wantErr: true,
+		},
 	}
 	for _, tt := range tests {
 		t.Run(tt.name, func(t *testing.T) {
```

### 🔸 Commit `1a5c07fccecfd7712d0c7132b2697cd3db80b3ee` - NGINX: Align quotes. (#12670) (2025-01-11) by `k8s-infra-cherrypick-robot`
- `images/nginx/rootfs/build.sh` [M]
```diff
diff --git a/images/nginx/rootfs/build.sh b/images/nginx/rootfs/build.sh
index 5667afc17..1d530e640 100755
--- a/images/nginx/rootfs/build.sh
+++ b/images/nginx/rootfs/build.sh
@@ -105,10 +105,10 @@ export LUA_RESTY_GLOBAL_THROTTLE_VERSION=v0.2.0
 export MIMALOC_VERSION=v2.1.7
 
 # Check for recent changes: https://github.com/open-telemetry/opentelemetry-cpp/compare/v1.18.0...main
-export OPENTELEMETRY_CPP_VERSION="v1.18.0"
+export OPENTELEMETRY_CPP_VERSION=v1.18.0
 
 # Check for recent changes: https://github.com/open-telemetry/opentelemetry-proto/compare/v1.5.0...main
-export OPENTELEMETRY_PROTO_VERSION="v1.5.0"
+export OPENTELEMETRY_PROTO_VERSION=v1.5.0
 
 export BUILD_PATH=/tmp/build
```

### 🔸 Commit `c54573f0587d8146fc879700955dcdbbe553f520` - Images: Trigger NGINX build. (#12675) (2025-01-11) by `Marco Ebert`
- `images/nginx/TAG` [M]
```diff
diff --git a/images/nginx/TAG b/images/nginx/TAG
index 1474d00f0..268b0334e 100644
--- a/images/nginx/TAG
+++ b/images/nginx/TAG
@@ -1 +1 @@
-v0.2.0
+v0.3.0
```

### 🔸 Commit `354cca61bb33e4130cd4891e6b508ad619a74f96` - Images: Bump `NGINX_BASE` to v0.3.0. (#12679) (2025-01-12) by `Marco Ebert`
- `NGINX_BASE` [M]
```diff
diff --git a/NGINX_BASE b/NGINX_BASE
index 5d0baff5f..d082857a7 100644
--- a/NGINX_BASE
+++ b/NGINX_BASE
@@ -1 +1 @@
-registry.k8s.io/ingress-nginx/nginx:v0.2.0@sha256:df33459aa3ef83c62d7fb1f1eafc872cf322fa342c0ec97a2533e844267d45b4
+registry.k8s.io/ingress-nginx/nginx:v0.3.0@sha256:73b4df804b128dc7aed9a769e17e9eaa70304895f26115c3d57e44e08ecc3685
```

### 🔸 Commit `5e162204e18831a9acc47716fbb19898760aa6d4` - Images: Trigger Test Runner build. (#12682) (2025-01-12) by `Marco Ebert`
- `images/test-runner/TAG` [M]
```diff
diff --git a/images/test-runner/TAG b/images/test-runner/TAG
index 79127d85a..18fa8e74f 100644
--- a/images/test-runner/TAG
+++ b/images/test-runner/TAG
@@ -1 +1 @@
-v1.2.0
+v1.3.0
```

### 🔸 Commit `ecd7d72577bf8e93bf5a4c249987a20a219e0310` - Tests: Bump Test Runner to v20250112-01b7af21. (#12685) (2025-01-12) by `Marco Ebert`
- `build/run-in-docker.sh` [M]
```diff
diff --git a/build/run-in-docker.sh b/build/run-in-docker.sh
index e191eda65..3f85159eb 100755
--- a/build/run-in-docker.sh
+++ b/build/run-in-docker.sh
@@ -44,7 +44,7 @@ function cleanup {
 }
 trap cleanup EXIT
 
-E2E_IMAGE=${E2E_IMAGE:-registry.k8s.io/ingress-nginx/e2e-test-runner:v20241224-68ed4e7b@sha256:871642296ebc0dd386f9a43b0cf2606028d757d6c4a2737d41180f02f8172823}
+E2E_IMAGE=${E2E_IMAGE:-registry.k8s.io/ingress-nginx/e2e-test-runner:v20250112-01b7af21@sha256:f77bb4625985462fe1a2bc846c430d668113abc90e5e5de6b4533403f56a048c}
 
 if [[ "$RUNTIME" == podman ]]; then
   # Podman does not support both tag and digest
```
- `test/e2e-image/Makefile` [M]
```diff
diff --git a/test/e2e-image/Makefile b/test/e2e-image/Makefile
index 7d553c04e..023fe68d3 100644
--- a/test/e2e-image/Makefile
+++ b/test/e2e-image/Makefile
@@ -1,6 +1,6 @@
 
 DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
-E2E_BASE_IMAGE ?= "registry.k8s.io/ingress-nginx/e2e-test-runner:v20241224-68ed4e7b@sha256:871642296ebc0dd386f9a43b0cf2606028d757d6c4a2737d41180f02f8172823"
+E2E_BASE_IMAGE ?= "registry.k8s.io/ingress-nginx/e2e-test-runner:v20250112-01b7af21@sha256:f77bb4625985462fe1a2bc846c430d668113abc90e5e5de6b4533403f56a048c"
 
 image:
 	echo "..entered Makefile in /test/e2e-image"
```
- `test/e2e/run-chart-test.sh` [M]
```diff
diff --git a/test/e2e/run-chart-test.sh b/test/e2e/run-chart-test.sh
index c8b079f84..10679a4c8 100755
--- a/test/e2e/run-chart-test.sh
+++ b/test/e2e/run-chart-test.sh
@@ -114,5 +114,5 @@ docker run \
   --workdir /workdir \
   --entrypoint ct \
   --rm \
-  registry.k8s.io/ingress-nginx/e2e-test-runner:v20241224-68ed4e7b@sha256:871642296ebc0dd386f9a43b0cf2606028d757d6c4a2737d41180f02f8172823 \
+  registry.k8s.io/ingress-nginx/e2e-test-runner:v20250112-01b7af21@sha256:f77bb4625985462fe1a2bc846c430d668113abc90e5e5de6b4533403f56a048c \
     install --charts charts/ingress-nginx
```

### 🔸 Commit `cdaf3f4e547575ac2bcf0c248c1d9c6424976a22` - Images: Trigger other builds (1/2). (#12687) (2025-01-12) by `k8s-infra-cherrypick-robot`
- `images/cfssl/TAG` [M]
```diff
diff --git a/images/cfssl/TAG b/images/cfssl/TAG
index 795460fce..56130fb3a 100644
--- a/images/cfssl/TAG
+++ b/images/cfssl/TAG
@@ -1 +1 @@
-v1.1.0
+v1.1.1
```
- `images/custom-error-pages/TAG` [M]
```diff
diff --git a/images/custom-error-pages/TAG b/images/custom-error-pages/TAG
index 795460fce..56130fb3a 100644
--- a/images/custom-error-pages/TAG
+++ b/images/custom-error-pages/TAG
@@ -1 +1 @@
-v1.1.0
+v1.1.1
```
- `images/e2e-test-echo/TAG` [M]
```diff
diff --git a/images/e2e-test-echo/TAG b/images/e2e-test-echo/TAG
index 795460fce..56130fb3a 100644
--- a/images/e2e-test-echo/TAG
+++ b/images/e2e-test-echo/TAG
@@ -1 +1 @@
-v1.1.0
+v1.1.1
```
- `images/ext-auth-example-authsvc/TAG` [M]
```diff
diff --git a/images/ext-auth-example-authsvc/TAG b/images/ext-auth-example-authsvc/TAG
index 795460fce..56130fb3a 100644
--- a/images/ext-auth-example-authsvc/TAG
+++ b/images/ext-auth-example-authsvc/TAG
@@ -1 +1 @@
-v1.1.0
+v1.1.1
```

### 🔸 Commit `57cf9c359192d22b5eb9e3433b761293a3fc491c` - Images: Trigger other builds (2/2). (#12691) (2025-01-12) by `k8s-infra-cherrypick-robot`
- `images/fastcgi-helloserver/TAG` [M]
```diff
diff --git a/images/fastcgi-helloserver/TAG b/images/fastcgi-helloserver/TAG
index 795460fce..56130fb3a 100644
--- a/images/fastcgi-helloserver/TAG
+++ b/images/fastcgi-helloserver/TAG
@@ -1 +1 @@
-v1.1.0
+v1.1.1
```
- `images/go-grpc-greeter-server/TAG` [M]
```diff
diff --git a/images/go-grpc-greeter-server/TAG b/images/go-grpc-greeter-server/TAG
index 795460fce..56130fb3a 100644
--- a/images/go-grpc-greeter-server/TAG
+++ b/images/go-grpc-greeter-server/TAG
@@ -1 +1 @@
-v1.1.0
+v1.1.1
```
- `images/httpbun/TAG` [M]
```diff
diff --git a/images/httpbun/TAG b/images/httpbun/TAG
index 795460fce..56130fb3a 100644
--- a/images/httpbun/TAG
+++ b/images/httpbun/TAG
@@ -1 +1 @@
-v1.1.0
+v1.1.1
```
- `images/kube-webhook-certgen/TAG` [M]
```diff
diff --git a/images/kube-webhook-certgen/TAG b/images/kube-webhook-certgen/TAG
index 2e7bd9108..53b5bbb12 100644
--- a/images/kube-webhook-certgen/TAG
+++ b/images/kube-webhook-certgen/TAG
@@ -1 +1 @@
-v1.5.0
+v1.5.1
```

### 🔸 Commit `c4eb35eb331031d94d860fcfd79ee87e1b61a59b` - Tests & Docs: Bump images. (#12695) (2025-01-13) by `k8s-infra-cherrypick-robot`
- `docs/examples/canary/README.md` [M]
```diff
diff --git a/docs/examples/canary/README.md b/docs/examples/canary/README.md
index 77b711b3a..885991a3b 100644
--- a/docs/examples/canary/README.md
+++ b/docs/examples/canary/README.md
@@ -31,7 +31,7 @@ spec:
     spec:
       containers:
       - name: production
-        image: registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.0@sha256:0713ba47b3e4359b38ad53cd785c34b158e168a91636520a4a5e54cd500d8356
+        image: registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.1@sha256:a1e0152e2eeab26e3f6fd3986f3d82b17bc7711717cae5392dcd18dd447ba6ef
         ports:
         - containerPort: 80
         env:
@@ -97,7 +97,7 @@ spec:
     spec:
       containers:
       - name: canary
-        image: registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.0@sha256:0713ba47b3e4359b38ad53cd785c34b158e168a91636520a4a5e54cd500d8356
+        image: registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.1@sha256:a1e0152e2eeab26e3f6fd3986f3d82b17bc7711717cae5392dcd18dd447ba6ef
         ports:
... (truncated)
```
- `docs/examples/customization/custom-errors/custom-default-backend.helm.values.yaml` [M]
```diff
diff --git a/docs/examples/customization/custom-errors/custom-default-backend.helm.values.yaml b/docs/examples/customization/custom-errors/custom-default-backend.helm.values.yaml
index b538f75ab..d72001d58 100644
--- a/docs/examples/customization/custom-errors/custom-default-backend.helm.values.yaml
+++ b/docs/examples/customization/custom-errors/custom-default-backend.helm.values.yaml
@@ -6,7 +6,7 @@ defaultBackend:
   image:
     registry: registry.k8s.io
     image: ingress-nginx/custom-error-pages
-    tag: v1.1.0@sha256:a2342e403fc3c19f81f5625e1b93daa0f8fb3dfaa1df4905f85e32d2d98a5e96
+    tag: v1.1.1@sha256:8c10776191ae44b5c387b8c7696d8bc17ceec90d7184a3a38b89ac8434b6c56b
   extraVolumes:
   - name: custom-error-pages
     configMap:
```
- `docs/examples/customization/custom-errors/custom-default-backend.yaml` [M]
```diff
diff --git a/docs/examples/customization/custom-errors/custom-default-backend.yaml b/docs/examples/customization/custom-errors/custom-default-backend.yaml
index b392eefef..088ca1374 100644
--- a/docs/examples/customization/custom-errors/custom-default-backend.yaml
+++ b/docs/examples/customization/custom-errors/custom-default-backend.yaml
@@ -36,7 +36,7 @@ spec:
     spec:
       containers:
       - name: nginx-error-server
-        image: registry.k8s.io/ingress-nginx/custom-error-pages:v1.1.0@sha256:a2342e403fc3c19f81f5625e1b93daa0f8fb3dfaa1df4905f85e32d2d98a5e96
+        image: registry.k8s.io/ingress-nginx/custom-error-pages:v1.1.1@sha256:8c10776191ae44b5c387b8c7696d8bc17ceec90d7184a3a38b89ac8434b6c56b
         ports:
         - containerPort: 8080
         # Setting the environment variable DEBUG we can see the headers sent
```
- `docs/examples/customization/external-auth-headers/echo-service.yaml` [M]
```diff
diff --git a/docs/examples/customization/external-auth-headers/echo-service.yaml b/docs/examples/customization/external-auth-headers/echo-service.yaml
index 6a970dd9f..10244458d 100644
--- a/docs/examples/customization/external-auth-headers/echo-service.yaml
+++ b/docs/examples/customization/external-auth-headers/echo-service.yaml
@@ -18,7 +18,7 @@ spec:
       terminationGracePeriodSeconds: 60
       containers:
       - name: echo-service
-        image: registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.0@sha256:0713ba47b3e4359b38ad53cd785c34b158e168a91636520a4a5e54cd500d8356
+        image: registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.1@sha256:a1e0152e2eeab26e3f6fd3986f3d82b17bc7711717cae5392dcd18dd447ba6ef
         ports:
         - containerPort: 8080
         resources:
```
- `test/e2e/HTTPBUN_IMAGE` [M]
```diff
diff --git a/test/e2e/HTTPBUN_IMAGE b/test/e2e/HTTPBUN_IMAGE
index 11f540282..491b333c7 100644
--- a/test/e2e/HTTPBUN_IMAGE
+++ b/test/e2e/HTTPBUN_IMAGE
@@ -1 +1 @@
-registry.k8s.io/ingress-nginx/httpbun:v1.1.0@sha256:bd870e71e30d478fafd00c515fba454f326960fe343a84ace577723a07a2cd6c
+registry.k8s.io/ingress-nginx/httpbun:v1.1.1@sha256:4569515d9b74470c915566a010792e7202b6769443fb1f3bb1b1e87376028634
```
- `test/e2e/framework/deployment.go` [M]
```diff
diff --git a/test/e2e/framework/deployment.go b/test/e2e/framework/deployment.go
index 21458a156..f213e2e98 100644
--- a/test/e2e/framework/deployment.go
+++ b/test/e2e/framework/deployment.go
@@ -47,7 +47,7 @@ const NIPService = "external-nip"
 var HTTPBunImage = os.Getenv("HTTPBUN_IMAGE")
 
 // EchoImage is the default image to be used by the echo service
-const EchoImage = "registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.0@sha256:0713ba47b3e4359b38ad53cd785c34b158e168a91636520a4a5e54cd500d8356" //#nosec G101
+const EchoImage = "registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.1@sha256:a1e0152e2eeab26e3f6fd3986f3d82b17bc7711717cae5392dcd18dd447ba6ef" //#nosec G101
 
 // TODO: change all Deployment functions to use these options
 // in order to reduce complexity and have a unified API across the
```
- `test/e2e/framework/fastcgi_helloserver.go` [M]
```diff
diff --git a/test/e2e/framework/fastcgi_helloserver.go b/test/e2e/framework/fastcgi_helloserver.go
index 65e257cfd..c414c4da3 100644
--- a/test/e2e/framework/fastcgi_helloserver.go
+++ b/test/e2e/framework/fastcgi_helloserver.go
@@ -59,7 +59,7 @@ func (f *Framework) NewNewFastCGIHelloServerDeploymentWithReplicas(replicas int3
 					Containers: []corev1.Container{
 						{
 							Name:  "fastcgi-helloserver",
-							Image: "registry.k8s.io/ingress-nginx/fastcgi-helloserver:v1.1.0@sha256:939cb351010a618383921b49056ccb6227b5a486ec52773464edbec03bc04812",
+							Image: "registry.k8s.io/ingress-nginx/fastcgi-helloserver:v1.1.1@sha256:6af4d8c7745c6727aab759db616a58fd68d784d07ce7a32d1ad149c331fd9a6f",
 							Env:   []corev1.EnvVar{},
 							Ports: []corev1.ContainerPort{
 								{
```
- `test/e2e/settings/ocsp/ocsp.go` [M]
```diff
diff --git a/test/e2e/settings/ocsp/ocsp.go b/test/e2e/settings/ocsp/ocsp.go
index 72e6d7ad2..282194bfe 100644
--- a/test/e2e/settings/ocsp/ocsp.go
+++ b/test/e2e/settings/ocsp/ocsp.go
@@ -295,7 +295,7 @@ func ocspserveDeployment(namespace string) (*appsv1.Deployment, *corev1.Service)
 						Containers: []corev1.Container{
 							{
 								Name:  name,
-								Image: "registry.k8s.io/ingress-nginx/cfssl:v1.1.0@sha256:31a195d7c3dc801575ca46919ff2b3f01afce54a744ab22ee83469f92a6e0965",
+								Image: "registry.k8s.io/ingress-nginx/cfssl:v1.1.1@sha256:bcd576c6d0a01d4710969195e804c02da62b71b5c35c6816df9b7584d5445437",
 								Command: []string{
 									"/bin/bash",
 									"-c",
```

### 🔸 Commit `57682a71eea248fcae54fea56b786dce6d525654` - Chart: Bump Kube Webhook CertGen. (#12697) (2025-01-13) by `Marco Ebert`
- `charts/ingress-nginx/README.md` [M]
```diff
diff --git a/charts/ingress-nginx/README.md b/charts/ingress-nginx/README.md
index 95b1ea0c3..de032d5ee 100644
--- a/charts/ingress-nginx/README.md
+++ b/charts/ingress-nginx/README.md
@@ -271,11 +271,11 @@ metadata:
 | controller.admissionWebhooks.namespaceSelector | object | `{}` |  |
 | controller.admissionWebhooks.objectSelector | object | `{}` |  |
 | controller.admissionWebhooks.patch.enabled | bool | `true` |  |
-| controller.admissionWebhooks.patch.image.digest | string | `"sha256:aaafd456bda110628b2d4ca6296f38731a3aaf0bf7581efae824a41c770a8fc4"` |  |
+| controller.admissionWebhooks.patch.image.digest | string | `"sha256:0de05718b59dc33b57ddfb4d8ad5f637cefd13eafdec0e1579d782b3483c27c3"` |  |
 | controller.admissionWebhooks.patch.image.image | string | `"ingress-nginx/kube-webhook-certgen"` |  |
 | controller.admissionWebhooks.patch.image.pullPolicy | string | `"IfNotPresent"` |  |
 | controller.admissionWebhooks.patch.image.registry | string | `"registry.k8s.io"` |  |
-| controller.admissionWebhooks.patch.image.tag | string | `"v1.5.0"` |  |
+| controller.admissionWebhooks.patch.image.tag | string | `"v1.5.1"` |  |
 | controller.admissionWebhooks.patch.labels | object | `{}` | Labels to be added to patch job resources |
 | controller.admissionWebhooks.patch.networkPolicy.enabled | bool | `false` | Enable 'networkPolicy' or not |
 | controller.admissionWebhooks.patch.nodeSelector."kubernetes.io/os" | string | `"linux"` |  |
```
- `charts/ingress-nginx/values.yaml` [M]
```diff
diff --git a/charts/ingress-nginx/values.yaml b/charts/ingress-nginx/values.yaml
index 02a024cb5..7d911d90e 100644
--- a/charts/ingress-nginx/values.yaml
+++ b/charts/ingress-nginx/values.yaml
@@ -808,8 +808,8 @@ controller:
         ## for backwards compatibility consider setting the full image url via the repository value below
         ## use *either* current default registry/image or repository format or installing chart by providing the values.yaml will fail
         ## repository:
-        tag: v1.5.0
-        digest: sha256:aaafd456bda110628b2d4ca6296f38731a3aaf0bf7581efae824a41c770a8fc4
+        tag: v1.5.1
+        digest: sha256:0de05718b59dc33b57ddfb4d8ad5f637cefd13eafdec0e1579d782b3483c27c3
         pullPolicy: IfNotPresent
       # -- Provide a priority class name to the webhook patching job
       ##
```

### 🔸 Commit `18715e51e9c14497441647db67305351a4d9bc74` - Bump google.golang.org/grpc from 1.69.2 to 1.69.4 in the go group across 1 directory (#12700) (2025-01-13) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 6335b6f89..91ab5be2e 100644
--- a/go.mod
+++ b/go.mod
@@ -27,7 +27,7 @@ require (
 	github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30
 	golang.org/x/crypto v0.32.0
 	golang.org/x/exp v0.0.0-20240719175910-8a7402abbf56
-	google.golang.org/grpc v1.69.2
+	google.golang.org/grpc v1.69.4
 	google.golang.org/grpc/examples v0.0.0-20240223204917-5ccf176a08ab
 	gopkg.in/go-playground/pool.v3 v3.1.1
 	gopkg.in/mcuadros/go-syslog.v2 v2.3.0
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 8de6c6bda..0ca74e190 100644
--- a/go.sum
+++ b/go.sum
@@ -306,8 +306,8 @@ gomodules.xyz/jsonpatch/v2 v2.4.0 h1:Ci3iUJyx9UeRx7CeFN8ARgGbkESwJK+KB9lLcWxY/Zw
 gomodules.xyz/jsonpatch/v2 v2.4.0/go.mod h1:AH3dM2RI6uoBZxn3LVrfvJ3E0/9dG4cSrbuBJT4moAY=
 google.golang.org/genproto/googleapis/rpc v0.0.0-20241015192408-796eee8c2d53 h1:X58yt85/IXCx0Y3ZwN6sEIKZzQtDEYaBWrDvErdXrRE=
 google.golang.org/genproto/googleapis/rpc v0.0.0-20241015192408-796eee8c2d53/go.mod h1:GX3210XPVPUjJbTUbvwI8f2IpZDMZuPJWDzDuebbviI=
-google.golang.org/grpc v1.69.2 h1:U3S9QEtbXC0bYNvRtcoklF3xGtLViumSYxWykJS+7AU=
-google.golang.org/grpc v1.69.2/go.mod h1:vyjdE6jLBI76dgpDojsFGNaHlxdjXN9ghpnd2o7JGZ4=
+google.golang.org/grpc v1.69.4 h1:MF5TftSMkd8GLw/m0KM6V8CMOCY6NZ1NQDPGFgbTt4A=
+google.golang.org/grpc v1.69.4/go.mod h1:vyjdE6jLBI76dgpDojsFGNaHlxdjXN9ghpnd2o7JGZ4=
 google.golang.org/grpc/examples v0.0.0-20240223204917-5ccf176a08ab h1:tg8hvIl5RmFBuXlcJMuL0h4Psh1gx5Q5xEMwzBZIzWA=
 google.golang.org/grpc/examples v0.0.0-20240223204917-5ccf176a08ab/go.mod h1:liVNnGuZDITxuksuZ+BBvdy7FcJfeNk+efF9qgqNUmc=
 google.golang.org/protobuf v0.0.0-20200109180630-ec00e32a8dfd/go.mod h1:DFci5gLYBciE7Vtevhsrf46CRTquxDuWsQurQQe4oz8=
```

### 🔸 Commit `1e03161e8708f9488fc437d2d7cfe62439eb57d1` - Go: Stop using workspace. (#12713) (2025-01-16) by `k8s-infra-cherrypick-robot`
- `go.work` [D]
```diff
diff --git a/go.work b/go.work
deleted file mode 100644
index 76d1a6369..000000000
--- a/go.work
+++ /dev/null
@@ -1,7 +0,0 @@
-go 1.23.4
-
-use (
-	.
-	./images/kube-webhook-certgen/rootfs
-	./magefiles
-)
```
- `go.work.sum` [D]
```diff
diff --git a/go.work.sum b/go.work.sum
deleted file mode 100644
index 0bc5d32bc..000000000
--- a/go.work.sum
+++ /dev/null
@@ -1,145 +0,0 @@
-cel.dev/expr v0.18.0/go.mod h1:MrpN08Q+lEBs+bGYdLxxHkZoUSsCp0nSKTs0nTymJgw=
-cloud.google.com/go/compute v1.23.3/go.mod h1:VCgBUoMnIVIR0CscqQiPJLAG25E3ZRZMzcFZeQ+h8CI=
-cloud.google.com/go/compute/metadata v0.3.0/go.mod h1:zFmK7XCadkQkj6TtorcaGlCW1hT1fIilQDwofLpJ20k=
-cloud.google.com/go/compute/metadata v0.5.2/go.mod h1:C66sj2AluDcIqakBq/M8lw8/ybHgOZqin2obFxa/E5k=
-github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.24.2/go.mod h1:itPGVDKf9cC/ov4MdvJ2QZ0khw4bfoo9jzwTJlaxy2k=
-github.com/Masterminds/semver/v3 v3.2.1/go.mod h1:qvl/7zhW3nngYb5+80sSMF+FG2BjYrf8m9wsX0PNOMQ=
-github.com/NYTimes/gziphandler v1.1.1/go.mod h1:n/CVRwUEOgIxrgPvAQhUUr9oeUtvrhMomdKFjzJNB0c=
-github.com/alecthomas/kingpin/v2 v2.4.0/go.mod h1:0gyi0zQnjuFk8xrkNKamJoyUo382HRL7ATRpFZCw6tE=
-github.com/alecthomas/units v0.0.0-20211218093645-b94a6e3cc137/go.mod h1:OMCwj8VM1Kc9e19TLln2VL61YJF0x1XFtfdL4JdbSyE=
-github.com/andybalholm/brotli v1.1.0/go.mod h1:sms7XGricyQI9K10gOSf56VKKWS4oLer58Q+mhRPtnY=
-github.com/antlr4-go/antlr/v4 v4.13.0/go.mod h1:pfChB/xh/Unjila75QW7+VU4TSnWnnk9UTnmpPaOR2g=
-github.com/armon/go-socks5 v0.0.0-20160902184237-e75332964ef5/go.mod h1:wHh0iHkYZB8zMSxRWpUBQtwG5a7fFgvEO+odwuTv2gs=
-github.com/asaskevich/govalidator v0.0.0-20190424111038-f61b66f89f4a/go.mod h1:lB+ZfQJz7igIIfQNfa7Ml4HSf2uFQQRzpGGRXenZAgY=
-github.com/bytedance/sonic v1.9.1/go.mod h1:i736AoUSYt75HyZLoJW9ERYxcy6eaN6h4BZXU064P/U=
... (truncated)
```

### 🔸 Commit `eea7014cf041d0e7cd84d65da0734e9b8afb62fd` - Docs: Clarify rate limits are per ingress controller replica. (#12716) (2025-01-17) by `k8s-infra-cherrypick-robot`
- `docs/user-guide/nginx-configuration/annotations.md` [M]
```diff
diff --git a/docs/user-guide/nginx-configuration/annotations.md b/docs/user-guide/nginx-configuration/annotations.md
index 9fd392eae..d04ad0ab2 100755
--- a/docs/user-guide/nginx-configuration/annotations.md
+++ b/docs/user-guide/nginx-configuration/annotations.md
@@ -552,10 +552,15 @@ By default the controller redirects all requests to an existing service that pro
 
 These annotations define limits on connections and transmission rates.  These can be used to mitigate [DDoS Attacks](https://www.nginx.com/blog/mitigating-ddos-attacks-with-nginx-and-nginx-plus).
 
-* `nginx.ingress.kubernetes.io/limit-connections`: number of concurrent connections allowed from a single IP address. A 503 error is returned when exceeding this limit.
-* `nginx.ingress.kubernetes.io/limit-rps`: number of requests accepted from a given IP each second. The burst limit is set to this limit multiplied by the burst multiplier, the default multiplier is 5. When clients exceed this limit,  [limit-req-status-code](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#limit-req-status-code) ***default:*** 503 is returned.
-* `nginx.ingress.kubernetes.io/limit-rpm`: number of requests accepted from a given IP each minute. The burst limit is set to this limit multiplied by the burst multiplier, the default multiplier is 5. When clients exceed this limit,  [limit-req-status-code](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#limit-req-status-code) ***default:*** 503 is returned.
-* `nginx.ingress.kubernetes.io/limit-burst-multiplier`: multiplier of the limit rate for burst size. The default burst multiplier is 5, this annotation override the default multiplier. When clients exceed this limit,  [limit-req-status-code](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#limit-req-status-code) ***default:*** 503 is returned.
+!!! attention
+    Rate limits are applied per Ingress NGINX controller replica. 
+    If you're running multiple replicas or using a horizontal pod autoscaler (HPA), the effective rate limit will be multiplied by the number of replicas.
+    When using HPA, the exact rate limit becomes dynamic as the number of replicas may change based on load.
+
+* `nginx.ingress.kubernetes.io/limit-connections`: number of concurrent connections allowed from a single IP address per controller replica. A 503 error is returned when exceeding this limit.
+* `nginx.ingress.kubernetes.io/limit-rps`: number of requests accepted from a given IP each second per controller replica. The burst limit is set to this limit multiplied by the burst multiplier, the default multiplier is 5. When clients exceed this limit, [limit-req-status-code](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#limit-req-status-code) ***default:*** 503 is returned.
+* `nginx.ingress.kubernetes.io/limit-rpm`: number of requests accepted from a given IP each minute per controller replica. The burst limit is set to this limit multiplied by the burst multiplier, the default multiplier is 5. When clients exceed this limit, [limit-req-status-code](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#limit-req-status-code) ***default:*** 503 is returned.
... (truncated)
```

### 🔸 Commit `90106cea19d56b5b9f0996e2325f096642e3e092` - Bump golangci/golangci-lint-action from 6.1.1 to 6.2.0 in the actions group (#12724) (2025-01-20) by `k8s-infra-cherrypick-robot`
- `.github/workflows/golangci-lint.yml` [M]
```diff
diff --git a/.github/workflows/golangci-lint.yml b/.github/workflows/golangci-lint.yml
index 942ef9a6d..199a9db50 100644
--- a/.github/workflows/golangci-lint.yml
+++ b/.github/workflows/golangci-lint.yml
@@ -28,7 +28,7 @@ jobs:
           check-latest: true
 
       - name: golangci-lint
-        uses: golangci/golangci-lint-action@971e284b6050e8a5849b72094c50ab08da042db8 # v6.1.1
+        uses: golangci/golangci-lint-action@ec5d18412c0aeab7936cb16880d708ba2a64e1ae # v6.2.0
         with:
           version: v1.62
           only-new-issues: true
```

### 🔸 Commit `c6d5b00a5a6e2f9b557cc4a4277319f76c488e2c` - Bump the go group across 3 directories with 9 updates (#12727) (2025-01-20) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 91ab5be2e..1b3300d67 100644
--- a/go.mod
+++ b/go.mod
@@ -31,14 +31,14 @@ require (
 	google.golang.org/grpc/examples v0.0.0-20240223204917-5ccf176a08ab
 	gopkg.in/go-playground/pool.v3 v3.1.1
 	gopkg.in/mcuadros/go-syslog.v2 v2.3.0
-	k8s.io/api v0.32.0
-	k8s.io/apiextensions-apiserver v0.32.0
-	k8s.io/apimachinery v0.32.0
-	k8s.io/apiserver v0.32.0
-	k8s.io/cli-runtime v0.32.0
-	k8s.io/client-go v0.32.0
-	k8s.io/code-generator v0.32.0
-	k8s.io/component-base v0.32.0
+	k8s.io/api v0.32.1
+	k8s.io/apiextensions-apiserver v0.32.1
+	k8s.io/apimachinery v0.32.1
+	k8s.io/apiserver v0.32.1
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 0ca74e190..f6e6ecdb1 100644
--- a/go.sum
+++ b/go.sum
@@ -342,22 +342,22 @@ gopkg.in/yaml.v2 v2.4.0/go.mod h1:RDklbk79AGWmwhnvt/jBztapEOGDOx6ZbXqjP6csGnQ=
 gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
 gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
 gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
-k8s.io/api v0.32.0 h1:OL9JpbvAU5ny9ga2fb24X8H6xQlVp+aJMFlgtQjR9CE=
-k8s.io/api v0.32.0/go.mod h1:4LEwHZEf6Q/cG96F3dqR965sYOfmPM7rq81BLgsE0p0=
-k8s.io/apiextensions-apiserver v0.32.0 h1:S0Xlqt51qzzqjKPxfgX1xh4HBZE+p8KKBq+k2SWNOE0=
-k8s.io/apiextensions-apiserver v0.32.0/go.mod h1:86hblMvN5yxMvZrZFX2OhIHAuFIMJIZ19bTvzkP+Fmw=
-k8s.io/apimachinery v0.32.0 h1:cFSE7N3rmEEtv4ei5X6DaJPHHX0C+upp+v5lVPiEwpg=
-k8s.io/apimachinery v0.32.0/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
-k8s.io/apiserver v0.32.0 h1:VJ89ZvQZ8p1sLeiWdRJpRD6oLozNZD2+qVSLi+ft5Qs=
-k8s.io/apiserver v0.32.0/go.mod h1:HFh+dM1/BE/Hm4bS4nTXHVfN6Z6tFIZPi649n83b4Ag=
-k8s.io/cli-runtime v0.32.0 h1:dP+OZqs7zHPpGQMCGAhectbHU2SNCuZtIimRKTv2T1c=
-k8s.io/cli-runtime v0.32.0/go.mod h1:Mai8ht2+esoDRK5hr861KRy6z0zHsSTYttNVJXgP3YQ=
-k8s.io/client-go v0.32.0 h1:DimtMcnN/JIKZcrSrstiwvvZvLjG0aSxy8PxN8IChp8=
-k8s.io/client-go v0.32.0/go.mod h1:boDWvdM1Drk4NJj/VddSLnx59X3OPgwrOo0vGbtq9+8=
... (truncated)
```
- `images/ext-auth-example-authsvc/rootfs/go.mod` [M]
```diff
diff --git a/images/ext-auth-example-authsvc/rootfs/go.mod b/images/ext-auth-example-authsvc/rootfs/go.mod
index f3e7ba804..c90ef9aaf 100644
--- a/images/ext-auth-example-authsvc/rootfs/go.mod
+++ b/images/ext-auth-example-authsvc/rootfs/go.mod
@@ -2,6 +2,6 @@ module example.com/authsvc
 
 go 1.23.4
 
-require k8s.io/apimachinery v0.32.0
+require k8s.io/apimachinery v0.32.1
 
 require github.com/google/uuid v1.6.0 // indirect
```
- `images/ext-auth-example-authsvc/rootfs/go.sum` [M]
```diff
diff --git a/images/ext-auth-example-authsvc/rootfs/go.sum b/images/ext-auth-example-authsvc/rootfs/go.sum
index 8984e1828..17a075fd0 100644
--- a/images/ext-auth-example-authsvc/rootfs/go.sum
+++ b/images/ext-auth-example-authsvc/rootfs/go.sum
@@ -1,4 +1,4 @@
 github.com/google/uuid v1.6.0 h1:NIvaJDMOsjHA8n1jAhLSgzrAzy1Hgr+hNrb57e+94F0=
 github.com/google/uuid v1.6.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
-k8s.io/apimachinery v0.32.0 h1:cFSE7N3rmEEtv4ei5X6DaJPHHX0C+upp+v5lVPiEwpg=
-k8s.io/apimachinery v0.32.0/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
+k8s.io/apimachinery v0.32.1 h1:683ENpaCBjma4CYqsmZyhEzrGz6cjn1MY/X2jB2hkZs=
+k8s.io/apimachinery v0.32.1/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
```
- `images/kube-webhook-certgen/rootfs/go.mod` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.mod b/images/kube-webhook-certgen/rootfs/go.mod
index d1fcf4909..e0e50678c 100644
--- a/images/kube-webhook-certgen/rootfs/go.mod
+++ b/images/kube-webhook-certgen/rootfs/go.mod
@@ -6,10 +6,10 @@ require (
 	github.com/onrik/logrus v0.11.0
 	github.com/sirupsen/logrus v1.9.3
 	github.com/spf13/cobra v1.8.1
-	k8s.io/api v0.32.0
-	k8s.io/apimachinery v0.32.0
-	k8s.io/client-go v0.32.0
-	k8s.io/kube-aggregator v0.32.0
+	k8s.io/api v0.32.1
+	k8s.io/apimachinery v0.32.1
+	k8s.io/client-go v0.32.1
+	k8s.io/kube-aggregator v0.32.1
 )
 
 require (
```
- `images/kube-webhook-certgen/rootfs/go.sum` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.sum b/images/kube-webhook-certgen/rootfs/go.sum
index 429552b0e..10fb1e113 100644
--- a/images/kube-webhook-certgen/rootfs/go.sum
+++ b/images/kube-webhook-certgen/rootfs/go.sum
@@ -141,16 +141,16 @@ gopkg.in/inf.v0 v0.9.1/go.mod h1:cWUDdTG/fYaXco+Dcufb5Vnc6Gp2YChqWtbxRZE0mXw=
 gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
 gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
 gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
-k8s.io/api v0.32.0 h1:OL9JpbvAU5ny9ga2fb24X8H6xQlVp+aJMFlgtQjR9CE=
-k8s.io/api v0.32.0/go.mod h1:4LEwHZEf6Q/cG96F3dqR965sYOfmPM7rq81BLgsE0p0=
-k8s.io/apimachinery v0.32.0 h1:cFSE7N3rmEEtv4ei5X6DaJPHHX0C+upp+v5lVPiEwpg=
-k8s.io/apimachinery v0.32.0/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
-k8s.io/client-go v0.32.0 h1:DimtMcnN/JIKZcrSrstiwvvZvLjG0aSxy8PxN8IChp8=
-k8s.io/client-go v0.32.0/go.mod h1:boDWvdM1Drk4NJj/VddSLnx59X3OPgwrOo0vGbtq9+8=
+k8s.io/api v0.32.1 h1:f562zw9cy+GvXzXf0CKlVQ7yHJVYzLfL6JAS4kOAaOc=
+k8s.io/api v0.32.1/go.mod h1:/Yi/BqkuueW1BgpoePYBRdDYfjPF5sgTr5+YqDZra5k=
+k8s.io/apimachinery v0.32.1 h1:683ENpaCBjma4CYqsmZyhEzrGz6cjn1MY/X2jB2hkZs=
+k8s.io/apimachinery v0.32.1/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
+k8s.io/client-go v0.32.1 h1:otM0AxdhdBIaQh7l1Q0jQpmo7WOFIk5FFa4bg6YMdUU=
+k8s.io/client-go v0.32.1/go.mod h1:aTTKZY7MdxUaJ/KiUs8D+GssR9zJZi77ZqtzcGXIiDg=
... (truncated)
```

### 🔸 Commit `f9d036488eb7b49df22adfb863c351e9c0d3517f` - Bump github.com/prometheus/common from 0.61.0 to 0.62.0 (#12729) (2025-01-20) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 1b3300d67..568b5cb96 100644
--- a/go.mod
+++ b/go.mod
@@ -19,7 +19,7 @@ require (
 	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2
 	github.com/prometheus/client_golang v1.20.5
 	github.com/prometheus/client_model v0.6.1
-	github.com/prometheus/common v0.61.0
+	github.com/prometheus/common v0.62.0
 	github.com/spf13/cobra v1.8.1
 	github.com/spf13/pflag v1.0.5
 	github.com/stretchr/testify v1.10.0
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index f6e6ecdb1..0a98313bb 100644
--- a/go.sum
+++ b/go.sum
@@ -184,8 +184,8 @@ github.com/prometheus/client_golang v1.20.5 h1:cxppBPuYhUnsO6yo/aoRol4L7q7UFfdm+
 github.com/prometheus/client_golang v1.20.5/go.mod h1:PIEt8X02hGcP8JWbeHyeZ53Y/jReSnHgO035n//V5WE=
 github.com/prometheus/client_model v0.6.1 h1:ZKSh/rekM+n3CeS952MLRAdFwIKqeY8b62p8ais2e9E=
 github.com/prometheus/client_model v0.6.1/go.mod h1:OrxVMOVHjw3lKMa8+x6HeMGkHMQyHDk9E3jmP2AmGiY=
-github.com/prometheus/common v0.61.0 h1:3gv/GThfX0cV2lpO7gkTUwZru38mxevy90Bj8YFSRQQ=
-github.com/prometheus/common v0.61.0/go.mod h1:zr29OCN/2BsJRaFwG8QOBr41D6kkchKbpeNH7pAjb/s=
+github.com/prometheus/common v0.62.0 h1:xasJaQlnWAeyHdUBeGjXmutelfJHWMRr+Fg4QszZ2Io=
+github.com/prometheus/common v0.62.0/go.mod h1:vyBcEuLSvWos9B1+CyL7JZ2up+uFzXhkqml0W5zIY1I=
 github.com/prometheus/procfs v0.15.1 h1:YagwOFzUgYfKKHX6Dr+sHT7km/hxC76UB0learggepc=
 github.com/prometheus/procfs v0.15.1/go.mod h1:fB45yRUv8NstnjriLhBQLuOUt+WW4BsoGhij/e3PBqk=
 github.com/rogpeppe/go-internal v1.12.0 h1:exVL4IDcn6na9z1rAb56Vxr+CgyK3nn3O+epU5NdKM8=
```

### 🔸 Commit `ff9c9399c0d00bee3bb0795739a38b92ae8721b9` - Bump sigs.k8s.io/controller-runtime from 0.19.4 to 0.20.0 (#12731) (2025-01-20) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 568b5cb96..b33e499ce 100644
--- a/go.mod
+++ b/go.mod
@@ -41,7 +41,7 @@ require (
 	k8s.io/component-base v0.32.1
 	k8s.io/klog/v2 v2.130.1
 	pault.ag/go/sniff v0.0.0-20200207005214-cf7e4d167732
-	sigs.k8s.io/controller-runtime v0.19.4
+	sigs.k8s.io/controller-runtime v0.20.0
 	sigs.k8s.io/mdtoc v1.4.0
 )
 
@@ -81,7 +81,7 @@ require (
 	github.com/gogo/protobuf v1.3.2 // indirect
 	github.com/golang/protobuf v1.5.4 // indirect
 	github.com/gomarkdown/markdown v0.0.0-20240328165702-4d01890c35c0 // indirect
-	github.com/google/btree v1.1.2 // indirect
+	github.com/google/btree v1.1.3 // indirect
 	github.com/google/gnostic-models v0.6.8 // indirect
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 0a98313bb..d3b078355 100644
--- a/go.sum
+++ b/go.sum
@@ -77,8 +77,8 @@ github.com/golang/protobuf v1.5.4 h1:i7eJL8qZTpSEXOPTxNKhASYpMn+8e5Q6AdndVa1dWek
 github.com/golang/protobuf v1.5.4/go.mod h1:lnTiLA8Wa4RWRcIUkrtSVa5nRhsEGBg48fD6rSs7xps=
 github.com/gomarkdown/markdown v0.0.0-20240328165702-4d01890c35c0 h1:4gjrh/PN2MuWCCElk8/I4OCKRKWCCo2zEct3VKCbibU=
 github.com/gomarkdown/markdown v0.0.0-20240328165702-4d01890c35c0/go.mod h1:JDGcbDT52eL4fju3sZ4TeHGsQwhG9nbDV21aMyhwPoA=
-github.com/google/btree v1.1.2 h1:xf4v41cLI2Z6FxbKm+8Bu+m8ifhj15JuZ9sa0jZCMUU=
-github.com/google/btree v1.1.2/go.mod h1:qOPhT0dTNdNzV6Z/lhRX0YXUafgPLFUh+gZMl761Gm4=
+github.com/google/btree v1.1.3 h1:CVpQJjYgC4VbzxeGVHfvZrv1ctoYCAI8vbl07Fcxlyg=
+github.com/google/btree v1.1.3/go.mod h1:qOPhT0dTNdNzV6Z/lhRX0YXUafgPLFUh+gZMl761Gm4=
 github.com/google/gnostic-models v0.6.8 h1:yo/ABAfM5IMRsS1VnXjTBvUb61tFIHozhlYvRgGre9I=
 github.com/google/gnostic-models v0.6.8/go.mod h1:5n7qKqH0f5wFt+aWF8CW6pZLLNOfYuF5OpfBSENuI8U=
 github.com/google/go-cmp v0.3.0/go.mod h1:8QqcDgzrUqlUb/G2PQTWiueGozuR1884gddMywk6iLU=
@@ -368,8 +368,8 @@ k8s.io/utils v0.0.0-20241104100929-3ea5e8cea738 h1:M3sRQVHv7vB20Xc2ybTt7ODCeFj6J
 k8s.io/utils v0.0.0-20241104100929-3ea5e8cea738/go.mod h1:OLgZIPagt7ERELqWJFomSt595RzquPNLL48iOWgYOg0=
 pault.ag/go/sniff v0.0.0-20200207005214-cf7e4d167732 h1:SAElp8THCfmBdM+4lmWX5gebiSSkEr7PAYDVF91qpfg=
 pault.ag/go/sniff v0.0.0-20200207005214-cf7e4d167732/go.mod h1:lpvCfhqEHNJSSpG5R5A2EgsVzG8RTt4RfPoQuRAcDmg=
-sigs.k8s.io/controller-runtime v0.19.4 h1:SUmheabttt0nx8uJtoII4oIP27BVVvAKFvdvGFwV/Qo=
... (truncated)
```

### 🔸 Commit `736d4b36b00b97fde22d521bfdefd3a53a3180ea` - Go: Bump to v1.23.5. (#12735) (2025-01-21) by `k8s-infra-cherrypick-robot`
- `GOLANG_VERSION` [M]
```diff
diff --git a/GOLANG_VERSION b/GOLANG_VERSION
index 27ddcc14d..ca8ec414e 100644
--- a/GOLANG_VERSION
+++ b/GOLANG_VERSION
@@ -1 +1 @@
-1.23.4
+1.23.5
```
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index b33e499ce..91748527f 100644
--- a/go.mod
+++ b/go.mod
@@ -1,6 +1,6 @@
 module k8s.io/ingress-nginx
 
-go 1.23.4
+go 1.23.5
 
 require (
 	dario.cat/mergo v1.0.1
```
- `images/custom-error-pages/rootfs/go.mod` [M]
```diff
diff --git a/images/custom-error-pages/rootfs/go.mod b/images/custom-error-pages/rootfs/go.mod
index 274b81ab1..e221e8e41 100644
--- a/images/custom-error-pages/rootfs/go.mod
+++ b/images/custom-error-pages/rootfs/go.mod
@@ -1,6 +1,6 @@
 module k8s.io/ingress-nginx/custom-error-pages
 
-go 1.23.4
+go 1.23.5
 
 require github.com/prometheus/client_golang v1.20.5
```
- `images/ext-auth-example-authsvc/rootfs/go.mod` [M]
```diff
diff --git a/images/ext-auth-example-authsvc/rootfs/go.mod b/images/ext-auth-example-authsvc/rootfs/go.mod
index c90ef9aaf..8db2af11b 100644
--- a/images/ext-auth-example-authsvc/rootfs/go.mod
+++ b/images/ext-auth-example-authsvc/rootfs/go.mod
@@ -1,6 +1,6 @@
 module example.com/authsvc
 
-go 1.23.4
+go 1.23.5
 
 require k8s.io/apimachinery v0.32.1
```
- `images/kube-webhook-certgen/rootfs/go.mod` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.mod b/images/kube-webhook-certgen/rootfs/go.mod
index e0e50678c..60d82d7a1 100644
--- a/images/kube-webhook-certgen/rootfs/go.mod
+++ b/images/kube-webhook-certgen/rootfs/go.mod
@@ -1,6 +1,6 @@
 module github.com/jet/kube-webhook-certgen
 
-go 1.23.4
+go 1.23.5
 
 require (
 	github.com/onrik/logrus v0.11.0
```
- `magefiles/go.mod` [M]
```diff
diff --git a/magefiles/go.mod b/magefiles/go.mod
index 9ee2bf363..5bb8b79ee 100644
--- a/magefiles/go.mod
+++ b/magefiles/go.mod
@@ -1,6 +1,6 @@
 module k8s.io/ingress-nginx/magefiles
 
-go 1.23.4
+go 1.23.5
 
 require (
 	github.com/blang/semver/v4 v4.0.0
```

### 🔸 Commit `55bf3541611aba97118c0e6808c7085c39164610` - Images: Bump `gcb-docker-gcloud` to v20250116-2a05ea7e3d. (#12737) (2025-01-21) by `k8s-infra-cherrypick-robot`
- `cloudbuild.yaml` [M]
```diff
diff --git a/cloudbuild.yaml b/cloudbuild.yaml
index 88ba9b935..cb74da0a5 100644
--- a/cloudbuild.yaml
+++ b/cloudbuild.yaml
@@ -2,7 +2,7 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20241217-ff46a068cd
+  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
       - REGISTRY=gcr.io/k8s-staging-ingress-nginx
       - REPO_INFO=https://github.com/kubernetes/ingress-nginx
```
- `images/cfssl/cloudbuild.yaml` [M]
```diff
diff --git a/images/cfssl/cloudbuild.yaml b/images/cfssl/cloudbuild.yaml
index 658921d1a..612bae942 100644
--- a/images/cfssl/cloudbuild.yaml
+++ b/images/cfssl/cloudbuild.yaml
@@ -2,7 +2,7 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20241217-ff46a068cd
+  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
       - REGISTRY=gcr.io/k8s-staging-ingress-nginx
     entrypoint: bash
```
- `images/custom-error-pages/cloudbuild.yaml` [M]
```diff
diff --git a/images/custom-error-pages/cloudbuild.yaml b/images/custom-error-pages/cloudbuild.yaml
index 7a583e69d..7a37591f8 100644
--- a/images/custom-error-pages/cloudbuild.yaml
+++ b/images/custom-error-pages/cloudbuild.yaml
@@ -2,7 +2,7 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20241217-ff46a068cd
+  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
       - REGISTRY=gcr.io/k8s-staging-ingress-nginx
     entrypoint: bash
```
- `images/e2e-test-echo/cloudbuild.yaml` [M]
```diff
diff --git a/images/e2e-test-echo/cloudbuild.yaml b/images/e2e-test-echo/cloudbuild.yaml
index a368f3489..ada4486a4 100644
--- a/images/e2e-test-echo/cloudbuild.yaml
+++ b/images/e2e-test-echo/cloudbuild.yaml
@@ -2,7 +2,7 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20241217-ff46a068cd
+  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
       - REGISTRY=gcr.io/k8s-staging-ingress-nginx
     entrypoint: bash
```
- `images/fastcgi-helloserver/cloudbuild.yaml` [M]
```diff
diff --git a/images/fastcgi-helloserver/cloudbuild.yaml b/images/fastcgi-helloserver/cloudbuild.yaml
index 289a59c2d..9dc5588a1 100644
--- a/images/fastcgi-helloserver/cloudbuild.yaml
+++ b/images/fastcgi-helloserver/cloudbuild.yaml
@@ -2,7 +2,7 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20241217-ff46a068cd
+  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
       - REGISTRY=gcr.io/k8s-staging-ingress-nginx
     entrypoint: bash
```
- `images/httpbun/cloudbuild.yaml` [M]
```diff
diff --git a/images/httpbun/cloudbuild.yaml b/images/httpbun/cloudbuild.yaml
index cd3df273d..741a5ebee 100644
--- a/images/httpbun/cloudbuild.yaml
+++ b/images/httpbun/cloudbuild.yaml
@@ -2,7 +2,7 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20241217-ff46a068cd
+  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
       - REGISTRY=gcr.io/k8s-staging-ingress-nginx
     entrypoint: bash
```
- `images/kube-webhook-certgen/cloudbuild.yaml` [M]
```diff
diff --git a/images/kube-webhook-certgen/cloudbuild.yaml b/images/kube-webhook-certgen/cloudbuild.yaml
index 443f24d0c..3f05ff099 100644
--- a/images/kube-webhook-certgen/cloudbuild.yaml
+++ b/images/kube-webhook-certgen/cloudbuild.yaml
@@ -2,7 +2,7 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20241217-ff46a068cd
+  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
       - REGISTRY=gcr.io/k8s-staging-ingress-nginx
     entrypoint: bash
```
- `images/nginx/cloudbuild.yaml` [M]
```diff
diff --git a/images/nginx/cloudbuild.yaml b/images/nginx/cloudbuild.yaml
index 4bf39adc8..c07c36a92 100644
--- a/images/nginx/cloudbuild.yaml
+++ b/images/nginx/cloudbuild.yaml
@@ -4,7 +4,7 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20241217-ff46a068cd
+  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
       - REGISTRY=gcr.io/k8s-staging-ingress-nginx
     entrypoint: bash
```
- `images/test-runner/cloudbuild.yaml` [M]
```diff
diff --git a/images/test-runner/cloudbuild.yaml b/images/test-runner/cloudbuild.yaml
index 5b38d5b32..bec8f3694 100644
--- a/images/test-runner/cloudbuild.yaml
+++ b/images/test-runner/cloudbuild.yaml
@@ -2,7 +2,7 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20241217-ff46a068cd
+  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
       - REGISTRY=gcr.io/k8s-staging-ingress-nginx
     entrypoint: bash
```

### 🔸 Commit `423125eca2bd9b2c5a9c38ee39d78a357d6a8808` - Development: Bump Kubernetes to v1.31.4. (#12740) (2025-01-21) by `k8s-infra-cherrypick-robot`
- `build/dev-env.sh` [M]
```diff
diff --git a/build/dev-env.sh b/build/dev-env.sh
index 699c98030..6bbd8c22c 100755
--- a/build/dev-env.sh
+++ b/build/dev-env.sh
@@ -64,7 +64,7 @@ echo "[dev-env] building image"
 make build image
 docker tag "${REGISTRY}/controller:${TAG}" "${DEV_IMAGE}"
 
-export K8S_VERSION=${K8S_VERSION:-v1.29.2@sha256:51a1434a5397193442f0be2a297b488b6c919ce8a3931be0ce822606ea5ca245}
+export K8S_VERSION=${K8S_VERSION:-v1.31.4@sha256:2cb39f7295fe7eafee0842b1052a599a4fb0f8bcf3f83d96c7f4864c357c6c30}
 
 KIND_CLUSTER_NAME="ingress-nginx-dev"
```

### 🔸 Commit `63f63b0c02a6ee85237ee857d88b99a64450d268` - Build: Always use local `tmp` dir on macOS. (#12742) (2025-01-21) by `k8s-infra-cherrypick-robot`
- `build/run-in-docker.sh` [M]
```diff
diff --git a/build/run-in-docker.sh b/build/run-in-docker.sh
index 3f85159eb..b5e683f3d 100755
--- a/build/run-in-docker.sh
+++ b/build/run-in-docker.sh
@@ -26,14 +26,11 @@ set -o nounset
 set -o pipefail
 
 # temporal directory for the /etc/ingress-controller directory
-if [[ "$OSTYPE" == darwin* ]] && [[ "$RUNTIME" == podman ]]; then
+if [[ "$OSTYPE" == darwin* ]]; then
   mkdir -p "tmp"
   INGRESS_VOLUME=$(pwd)/$(mktemp -d tmp/XXXXXX)
 else
   INGRESS_VOLUME=$(mktemp -d)
-  if [[ "$OSTYPE" == darwin* ]]; then
-    INGRESS_VOLUME=/private$INGRESS_VOLUME
-  fi
 fi
 
 # make sure directory for SSL cert storage exists under ingress volume
```

### 🔸 Commit `2b849914bfa7becdafba10d4602122ed0f6d059f` - Docs: Improve bare-metal setup. (#12745) (2025-01-22) by `k8s-infra-cherrypick-robot`
- `docs/deploy/baremetal.md` [M]
```diff
diff --git a/docs/deploy/baremetal.md b/docs/deploy/baremetal.md
index f5ff54174..077d1e758 100644
--- a/docs/deploy/baremetal.md
+++ b/docs/deploy/baremetal.md
@@ -118,6 +118,8 @@ requests.
 
 ![NodePort request flow](../images/baremetal/nodeport.jpg)
 
+You can **customize the exposed node port numbers** by setting the `controller.service.nodePorts.*` Helm values, but they still have to be in the 30000-32767 range.
+
 !!! example
     Given the NodePort `30100` allocated to the `ingress-nginx` Service
 
@@ -152,7 +154,7 @@ requests.
 
 This approach has a few other limitations one ought to be aware of:
 
-* **Source IP address**
+### Source IP address
 
... (truncated)
```
- `docs/user-guide/miscellaneous.md` [M]
```diff
diff --git a/docs/user-guide/miscellaneous.md b/docs/user-guide/miscellaneous.md
index 80a38db51..ee3d63056 100644
--- a/docs/user-guide/miscellaneous.md
+++ b/docs/user-guide/miscellaneous.md
@@ -4,9 +4,11 @@
 
 By default NGINX uses the content of the header `X-Forwarded-For` as the source of truth to get information about the client IP address. This works without issues in L7 **if we configure the setting `proxy-real-ip-cidr`** with the correct information of the IP/network address of trusted external load balancer.
 
+This setting can be enabled/disabled by setting [`use-forwarded-headers`](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#use-forwarded-headers).
+
 If the ingress controller is running in AWS we need to use the VPC IPv4 CIDR.
 
-Another option is to enable proxy protocol using `use-proxy-protocol: "true"`.
+Another option is to enable the **PROXY protocol** using [`use-proxy-protocol: "true"`](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#use-proxy-protocol).
 
 In this mode NGINX does not use the content of the header to get the source IP address of the connection.
```

### 🔸 Commit `debcfe38574bb713278c5b254eed41f917b483e3` - Bump the actions group with 5 updates (#12757) (2025-01-27) by `k8s-infra-cherrypick-robot`
- `.github/workflows/chart.yaml` [M]
```diff
diff --git a/.github/workflows/chart.yaml b/.github/workflows/chart.yaml
index f2c017fd5..dc7359814 100644
--- a/.github/workflows/chart.yaml
+++ b/.github/workflows/chart.yaml
@@ -31,7 +31,7 @@ jobs:
         uses: azure/setup-helm@fe7b79cd5ee1e45176fcad797de68ecaf3ca4814 # v4.2.0
 
       - name: Set up Helm Chart Testing
-        uses: helm/chart-testing-action@e6669bcd63d7cb57cb4380c33043eebe5d111992 # v2.6.1
+        uses: helm/chart-testing-action@0d28d3144d3a25ea2cc349d6e59901c4ff469b3b # v2.7.0
 
       - name: Set up Artifact Hub
         run: |
@@ -55,7 +55,7 @@ jobs:
           ah lint --path charts/ingress-nginx
 
       - name: Release chart
-        uses: helm/chart-releaser-action@a917fd15b20e8b64b94d9158ad54cd6345335584 # v1.6.0
+        uses: helm/chart-releaser-action@cae68fefc6b5f367a0275617c9f83181ba54714f # v1.7.0
         env:
... (truncated)
```
- `.github/workflows/ci.yaml` [M]
```diff
diff --git a/.github/workflows/ci.yaml b/.github/workflows/ci.yaml
index 62be8beba..515613529 100644
--- a/.github/workflows/ci.yaml
+++ b/.github/workflows/ci.yaml
@@ -86,7 +86,7 @@ jobs:
 
       - name: Set up Go
         id: go
-        uses: actions/setup-go@3041bf56c941b39c61721a86cd11f3bb1338122a # v5.2.0
+        uses: actions/setup-go@f111f3307d8850f501ac008e886eec1fd1932a34 # v5.3.0
         with:
           go-version: ${{ env.GOLANG_VERSION }}
           check-latest: true
@@ -108,7 +108,7 @@ jobs:
         run: echo "GOLANG_VERSION=$(cat GOLANG_VERSION)" >> $GITHUB_ENV
       - name: Set up Go
         id: go
-        uses: actions/setup-go@3041bf56c941b39c61721a86cd11f3bb1338122a # v5.2.0
+        uses: actions/setup-go@f111f3307d8850f501ac008e886eec1fd1932a34 # v5.3.0
         with:
... (truncated)
```
- `.github/workflows/golangci-lint.yml` [M]
```diff
diff --git a/.github/workflows/golangci-lint.yml b/.github/workflows/golangci-lint.yml
index 199a9db50..b69725dde 100644
--- a/.github/workflows/golangci-lint.yml
+++ b/.github/workflows/golangci-lint.yml
@@ -22,7 +22,7 @@ jobs:
 
       - name: Set up Go
         id: go
-        uses: actions/setup-go@3041bf56c941b39c61721a86cd11f3bb1338122a # v5.2.0
+        uses: actions/setup-go@f111f3307d8850f501ac008e886eec1fd1932a34 # v5.3.0
         with:
           go-version: ${{ env.GOLANG_VERSION }}
           check-latest: true
```
- `.github/workflows/images.yaml` [M]
```diff
diff --git a/.github/workflows/images.yaml b/.github/workflows/images.yaml
index 4a220ddf2..69f9a9d9d 100644
--- a/.github/workflows/images.yaml
+++ b/.github/workflows/images.yaml
@@ -148,7 +148,7 @@ jobs:
 
     - name: Set up Go
       id: go
-      uses: actions/setup-go@3041bf56c941b39c61721a86cd11f3bb1338122a # v5.2.0
+      uses: actions/setup-go@f111f3307d8850f501ac008e886eec1fd1932a34 # v5.3.0
       with:
         go-version: ${{ env.GOLANG_VERSION }}
         check-latest: true
```
- `.github/workflows/plugin.yaml` [M]
```diff
diff --git a/.github/workflows/plugin.yaml b/.github/workflows/plugin.yaml
index a9c5c9248..8e203c373 100644
--- a/.github/workflows/plugin.yaml
+++ b/.github/workflows/plugin.yaml
@@ -20,7 +20,7 @@ jobs:
         run: echo "GOLANG_VERSION=$(cat GOLANG_VERSION)" >> $GITHUB_ENV
 
       - name: Set up Go
-        uses: actions/setup-go@3041bf56c941b39c61721a86cd11f3bb1338122a # v5.2.0
+        uses: actions/setup-go@f111f3307d8850f501ac008e886eec1fd1932a34 # v5.3.0
         with:
           go-version: ${{ env.GOLANG_VERSION }}
           check-latest: true
```
- `.github/workflows/scorecards.yml` [M]
```diff
diff --git a/.github/workflows/scorecards.yml b/.github/workflows/scorecards.yml
index 7d6424e5b..d94c7b336 100644
--- a/.github/workflows/scorecards.yml
+++ b/.github/workflows/scorecards.yml
@@ -59,6 +59,6 @@ jobs:
 
       # Upload the results to GitHub's code scanning dashboard.
       - name: "Upload to code-scanning"
-        uses: github/codeql-action/upload-sarif@b6a472f63d85b9c78a3ac5e89422239fc15e9b3c # v3.28.1
+        uses: github/codeql-action/upload-sarif@f6091c0113d1dcf9b98e269ee48e8a7e51b7bdd4 # v3.28.5
         with:
           sarif_file: results.sarif
```
- `.github/workflows/stale.yaml` [M]
```diff
diff --git a/.github/workflows/stale.yaml b/.github/workflows/stale.yaml
index a7c245295..45a7cd320 100644
--- a/.github/workflows/stale.yaml
+++ b/.github/workflows/stale.yaml
@@ -13,7 +13,7 @@ jobs:
       pull-requests: write
 
     steps:
-      - uses: actions/stale@28ca1036281a5e5922ead5184a1bbf96e5fc984e # v9.0.0
+      - uses: actions/stale@5bef64f19d7facfb25b37b414482c7164d639639 # v9.1.0
         with:
           stale-issue-message: "This is stale, but we won't close it automatically, just bare in mind the maintainers may be busy with other tasks and will reach your issue ASAP. If you have any question or request to prioritize this, please reach `#ingress-nginx-dev` on Kubernetes Slack."
           stale-pr-message: "This is stale, but we won't close it automatically, just bare in mind the maintainers may be busy with other tasks and will reach your issue ASAP. If you have any question or request to prioritize this, please reach `#ingress-nginx-dev` on Kubernetes Slack."
```
- `.github/workflows/vulnerability-scans.yaml` [M]
```diff
diff --git a/.github/workflows/vulnerability-scans.yaml b/.github/workflows/vulnerability-scans.yaml
index 6e4243f04..56e7c98cb 100644
--- a/.github/workflows/vulnerability-scans.yaml
+++ b/.github/workflows/vulnerability-scans.yaml
@@ -75,7 +75,7 @@ jobs:
 
       # This step checks out a copy of your repository.
       - name: Upload SARIF file
-        uses: github/codeql-action/upload-sarif@b6a472f63d85b9c78a3ac5e89422239fc15e9b3c # v3.28.1
+        uses: github/codeql-action/upload-sarif@f6091c0113d1dcf9b98e269ee48e8a7e51b7bdd4 # v3.28.5
         with:
           token: ${{ github.token }}
           # Path to SARIF file relative to the root of the repository
```

### 🔸 Commit `7172a5c46a241dc2aa45366d348f05d1398ff31f` - Bump sigs.k8s.io/controller-runtime from 0.20.0 to 0.20.1 in the go group across 1 directory (#12759) (2025-01-27) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 91748527f..fb134d8ff 100644
--- a/go.mod
+++ b/go.mod
@@ -41,7 +41,7 @@ require (
 	k8s.io/component-base v0.32.1
 	k8s.io/klog/v2 v2.130.1
 	pault.ag/go/sniff v0.0.0-20200207005214-cf7e4d167732
-	sigs.k8s.io/controller-runtime v0.20.0
+	sigs.k8s.io/controller-runtime v0.20.1
 	sigs.k8s.io/mdtoc v1.4.0
 )
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index d3b078355..84debcade 100644
--- a/go.sum
+++ b/go.sum
@@ -368,8 +368,8 @@ k8s.io/utils v0.0.0-20241104100929-3ea5e8cea738 h1:M3sRQVHv7vB20Xc2ybTt7ODCeFj6J
 k8s.io/utils v0.0.0-20241104100929-3ea5e8cea738/go.mod h1:OLgZIPagt7ERELqWJFomSt595RzquPNLL48iOWgYOg0=
 pault.ag/go/sniff v0.0.0-20200207005214-cf7e4d167732 h1:SAElp8THCfmBdM+4lmWX5gebiSSkEr7PAYDVF91qpfg=
 pault.ag/go/sniff v0.0.0-20200207005214-cf7e4d167732/go.mod h1:lpvCfhqEHNJSSpG5R5A2EgsVzG8RTt4RfPoQuRAcDmg=
-sigs.k8s.io/controller-runtime v0.20.0 h1:jjkMo29xEXH+02Md9qaVXfEIaMESSpy3TBWPrsfQkQs=
-sigs.k8s.io/controller-runtime v0.20.0/go.mod h1:BrP3w158MwvB3ZbNpaAcIKkHQ7YGpYnzpoSTZ8E14WU=
+sigs.k8s.io/controller-runtime v0.20.1 h1:JbGMAG/X94NeM3xvjenVUaBjy6Ui4Ogd/J5ZtjZnHaE=
+sigs.k8s.io/controller-runtime v0.20.1/go.mod h1:BrP3w158MwvB3ZbNpaAcIKkHQ7YGpYnzpoSTZ8E14WU=
 sigs.k8s.io/json v0.0.0-20241010143419-9aa6b5e7a4b3 h1:/Rv+M11QRah1itp8VhT6HoVx1Ray9eB4DBr+K+/sCJ8=
 sigs.k8s.io/json v0.0.0-20241010143419-9aa6b5e7a4b3/go.mod h1:18nIHnGi6636UCz6m8i4DhaJ65T6EruyzmoQqI2BVDo=
 sigs.k8s.io/kustomize/api v0.18.0 h1:hTzp67k+3NEVInwz5BHyzc9rGxIauoXferXyjv5lWPo=
```

### 🔸 Commit `6a3960b69c043c9bfd4717cbac04475f21f54acb` - Bump google.golang.org/grpc from 1.69.4 to 1.70.0 (#12761) (2025-01-27) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index fb134d8ff..d80985a43 100644
--- a/go.mod
+++ b/go.mod
@@ -27,7 +27,7 @@ require (
 	github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30
 	golang.org/x/crypto v0.32.0
 	golang.org/x/exp v0.0.0-20240719175910-8a7402abbf56
-	google.golang.org/grpc v1.69.4
+	google.golang.org/grpc v1.70.0
 	google.golang.org/grpc/examples v0.0.0-20240223204917-5ccf176a08ab
 	gopkg.in/go-playground/pool.v3 v3.1.1
 	gopkg.in/mcuadros/go-syslog.v2 v2.3.0
@@ -51,8 +51,8 @@ require (
 	github.com/klauspost/compress v1.17.9 // indirect
 	github.com/moby/sys/userns v0.1.0 // indirect
 	github.com/x448/float16 v0.8.4 // indirect
-	go.opentelemetry.io/otel v1.31.0 // indirect
-	go.opentelemetry.io/otel/trace v1.31.0 // indirect
+	go.opentelemetry.io/otel v1.32.0 // indirect
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 84debcade..c797b8308 100644
--- a/go.sum
+++ b/go.sum
@@ -224,16 +224,16 @@ github.com/yuin/goldmark v1.1.27/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9de
 github.com/yuin/goldmark v1.2.1/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9decYSb74=
 github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30 h1:rzHvkiukOVYcf840FqAsHqBMhfLofvQIxWtczkGRklU=
 github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30/go.mod h1:/Hzu8ych2oXCs1iNI+MeASyFzWTncQ6nlu/wgqbqC2A=
-go.opentelemetry.io/otel v1.31.0 h1:NsJcKPIW0D0H3NgzPDHmo0WW6SptzPdqg/L1zsIm2hY=
-go.opentelemetry.io/otel v1.31.0/go.mod h1:O0C14Yl9FgkjqcCZAsE053C13OaddMYr/hz6clDkEJE=
-go.opentelemetry.io/otel/metric v1.31.0 h1:FSErL0ATQAmYHUIzSezZibnyVlft1ybhy4ozRPcF2fE=
-go.opentelemetry.io/otel/metric v1.31.0/go.mod h1:C3dEloVbLuYoX41KpmAhOqNriGbA+qqH6PQ5E5mUfnY=
-go.opentelemetry.io/otel/sdk v1.31.0 h1:xLY3abVHYZ5HSfOg3l2E5LUj2Cwva5Y7yGxnSW9H5Gk=
-go.opentelemetry.io/otel/sdk v1.31.0/go.mod h1:TfRbMdhvxIIr/B2N2LQW2S5v9m3gOQ/08KsbbO5BPT0=
-go.opentelemetry.io/otel/sdk/metric v1.31.0 h1:i9hxxLJF/9kkvfHppyLL55aW7iIJz4JjxTeYusH7zMc=
-go.opentelemetry.io/otel/sdk/metric v1.31.0/go.mod h1:CRInTMVvNhUKgSAMbKyTMxqOBC0zgyxzW55lZzX43Y8=
-go.opentelemetry.io/otel/trace v1.31.0 h1:ffjsj1aRouKewfr85U2aGagJ46+MvodynlQ1HYdmJys=
-go.opentelemetry.io/otel/trace v1.31.0/go.mod h1:TXZkRk7SM2ZQLtR6eoAWQFIHPvzQ06FJAsO1tJg480A=
+go.opentelemetry.io/otel v1.32.0 h1:WnBN+Xjcteh0zdk01SVqV55d/m62NJLJdIyb4y/WO5U=
+go.opentelemetry.io/otel v1.32.0/go.mod h1:00DCVSB0RQcnzlwyTfqtxSm+DRr9hpYrHjNGiBHVQIg=
... (truncated)
```

### 🔸 Commit `1fb8296511f30990884c9106d4304bf8c523563e` - Docs: Fix character format. (#12774) (2025-02-03) by `k8s-infra-cherrypick-robot`
- `docs/faq.md` [M]
```diff
diff --git a/docs/faq.md b/docs/faq.md
index 97d3325ca..ea1e4d308 100644
--- a/docs/faq.md
+++ b/docs/faq.md
@@ -165,8 +165,8 @@ default on the next breaking change release, set for 2.0.0.
 
 - When "`ingress.spec.rules.http.pathType=Exact`" or "`pathType=Prefix`", this
 validation will limit the characters accepted on the field "`ingress.spec.rules.http.paths.path`",
-to "`alphanumeric characters`", and  `"/," "_," "-."` Also, in this case,
-the path should start with `"/."`
+to "`alphanumeric characters`", and  "`/`", "`_`", "`-`". Also, in this case,
+the path should start with "`/`".
 
 - When the ingress resource path contains other characters (like on rewrite
 configurations), the pathType value should be "`ImplementationSpecific`".
@@ -175,7 +175,7 @@ configurations), the pathType value should be "`ImplementationSpecific`".
 
 - When this option is enabled, the validation will happen on the Admission
 Webhook. So if any new ingress object contains characters other than
-alphanumeric characters, and, `"/,","_","-"`, in the `path` field, but
... (truncated)
```

### 🔸 Commit `a0bddb0bb01512377fb44400458fd9c2281214f2` - Bump the go group across 2 directories with 1 update (#12776) (2025-02-03) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index d80985a43..d3bcf8246 100644
--- a/go.mod
+++ b/go.mod
@@ -21,7 +21,7 @@ require (
 	github.com/prometheus/client_model v0.6.1
 	github.com/prometheus/common v0.62.0
 	github.com/spf13/cobra v1.8.1
-	github.com/spf13/pflag v1.0.5
+	github.com/spf13/pflag v1.0.6
 	github.com/stretchr/testify v1.10.0
 	github.com/yudai/gojsondiff v1.0.0
 	github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index c797b8308..bf60b99be 100644
--- a/go.sum
+++ b/go.sum
@@ -197,8 +197,9 @@ github.com/sirupsen/logrus v1.9.3 h1:dueUQJ1C2q9oE3F7wvmSGAaVtTmUizReu6fjN8uqzbQ
 github.com/sirupsen/logrus v1.9.3/go.mod h1:naHLuLoDiP4jHNo9R0sCBMtWGeIprob74mVsIT4qYEQ=
 github.com/spf13/cobra v1.8.1 h1:e5/vxKd/rZsfSJMUX1agtjeTDf+qv1/JdBF8gg5k9ZM=
 github.com/spf13/cobra v1.8.1/go.mod h1:wHxEcudfqmLYa8iTfL+OuZPbBZkmvliBWKIezN3kD9Y=
-github.com/spf13/pflag v1.0.5 h1:iy+VFUOCP1a+8yFto/drg2CJ5u0yRoB7fZw3DKv/JXA=
 github.com/spf13/pflag v1.0.5/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
+github.com/spf13/pflag v1.0.6 h1:jFzHGLGAlb3ruxLB8MhbI6A8+AQX/2eW4qeyNZXNp2o=
+github.com/spf13/pflag v1.0.6/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
 github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
 github.com/stretchr/objx v0.5.2 h1:xuMeJ0Sdp5ZMRXx/aWO6RZxdr3beISkG5/G/aIRr3pY=
 github.com/stretchr/objx v0.5.2/go.mod h1:FRsXN1f5AsAjCGJKqEizvkpNtU+EGNCLh3NxZ/8L+MA=
```
- `images/kube-webhook-certgen/rootfs/go.mod` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.mod b/images/kube-webhook-certgen/rootfs/go.mod
index 60d82d7a1..bab5f8775 100644
--- a/images/kube-webhook-certgen/rootfs/go.mod
+++ b/images/kube-webhook-certgen/rootfs/go.mod
@@ -36,7 +36,7 @@ require (
 	github.com/onsi/ginkgo/v2 v2.22.2 // indirect
 	github.com/onsi/gomega v1.36.2 // indirect
 	github.com/pkg/errors v0.9.1 // indirect
-	github.com/spf13/pflag v1.0.5 // indirect
+	github.com/spf13/pflag v1.0.6 // indirect
 	github.com/x448/float16 v0.8.4 // indirect
 	golang.org/x/net v0.33.0 // indirect
 	golang.org/x/oauth2 v0.23.0 // indirect
```
- `images/kube-webhook-certgen/rootfs/go.sum` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.sum b/images/kube-webhook-certgen/rootfs/go.sum
index 10fb1e113..ba5876b08 100644
--- a/images/kube-webhook-certgen/rootfs/go.sum
+++ b/images/kube-webhook-certgen/rootfs/go.sum
@@ -72,8 +72,9 @@ github.com/sirupsen/logrus v1.9.3 h1:dueUQJ1C2q9oE3F7wvmSGAaVtTmUizReu6fjN8uqzbQ
 github.com/sirupsen/logrus v1.9.3/go.mod h1:naHLuLoDiP4jHNo9R0sCBMtWGeIprob74mVsIT4qYEQ=
 github.com/spf13/cobra v1.8.1 h1:e5/vxKd/rZsfSJMUX1agtjeTDf+qv1/JdBF8gg5k9ZM=
 github.com/spf13/cobra v1.8.1/go.mod h1:wHxEcudfqmLYa8iTfL+OuZPbBZkmvliBWKIezN3kD9Y=
-github.com/spf13/pflag v1.0.5 h1:iy+VFUOCP1a+8yFto/drg2CJ5u0yRoB7fZw3DKv/JXA=
 github.com/spf13/pflag v1.0.5/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
+github.com/spf13/pflag v1.0.6 h1:jFzHGLGAlb3ruxLB8MhbI6A8+AQX/2eW4qeyNZXNp2o=
+github.com/spf13/pflag v1.0.6/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
 github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
 github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
 github.com/stretchr/testify v1.7.0/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
```

### 🔸 Commit `ca50eaa2eb8e284a2f09eb4fc6b5162ef7f8a9fb` - Bump the actions group with 2 updates (#12778) (2025-02-03) by `k8s-infra-cherrypick-robot`
- `.github/workflows/chart.yaml` [M]
```diff
diff --git a/.github/workflows/chart.yaml b/.github/workflows/chart.yaml
index dc7359814..23109a001 100644
--- a/.github/workflows/chart.yaml
+++ b/.github/workflows/chart.yaml
@@ -23,7 +23,7 @@ jobs:
 
     steps:
       - name: Set up Python
-        uses: actions/setup-python@0b93645e9fea7318ecaed2b359559ac225c90a2b # v5.3.0
+        uses: actions/setup-python@42375524e23c412d93fb67b49958b491fce71c38 # v5.4.0
         with:
           python-version: 3.x
```
- `.github/workflows/ci.yaml` [M]
```diff
diff --git a/.github/workflows/ci.yaml b/.github/workflows/ci.yaml
index 515613529..c41becc38 100644
--- a/.github/workflows/ci.yaml
+++ b/.github/workflows/ci.yaml
@@ -202,7 +202,7 @@ jobs:
 
     steps:
       - name: Set up Python
-        uses: actions/setup-python@0b93645e9fea7318ecaed2b359559ac225c90a2b # v5.3.0
+        uses: actions/setup-python@42375524e23c412d93fb67b49958b491fce71c38 # v5.4.0
         with:
           python-version: 3.x
```
- `.github/workflows/scorecards.yml` [M]
```diff
diff --git a/.github/workflows/scorecards.yml b/.github/workflows/scorecards.yml
index d94c7b336..b9b88a9d9 100644
--- a/.github/workflows/scorecards.yml
+++ b/.github/workflows/scorecards.yml
@@ -59,6 +59,6 @@ jobs:
 
       # Upload the results to GitHub's code scanning dashboard.
       - name: "Upload to code-scanning"
-        uses: github/codeql-action/upload-sarif@f6091c0113d1dcf9b98e269ee48e8a7e51b7bdd4 # v3.28.5
+        uses: github/codeql-action/upload-sarif@dd746615b3b9d728a6a37ca2045b68ca76d4841a # v3.28.8
         with:
           sarif_file: results.sarif
```
- `.github/workflows/vulnerability-scans.yaml` [M]
```diff
diff --git a/.github/workflows/vulnerability-scans.yaml b/.github/workflows/vulnerability-scans.yaml
index 56e7c98cb..0215c5de2 100644
--- a/.github/workflows/vulnerability-scans.yaml
+++ b/.github/workflows/vulnerability-scans.yaml
@@ -75,7 +75,7 @@ jobs:
 
       # This step checks out a copy of your repository.
       - name: Upload SARIF file
-        uses: github/codeql-action/upload-sarif@f6091c0113d1dcf9b98e269ee48e8a7e51b7bdd4 # v3.28.5
+        uses: github/codeql-action/upload-sarif@dd746615b3b9d728a6a37ca2045b68ca76d4841a # v3.28.8
         with:
           token: ${{ github.token }}
           # Path to SARIF file relative to the root of the repository
```

### 🔸 Commit `93aa96cde07469f82ad19bf372d5acbdda654b0b` - Go: Replace `golang.org/x/exp/slices` with `slices`. (#12780) (2025-02-03) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index d3bcf8246..c96d19c4f 100644
--- a/go.mod
+++ b/go.mod
@@ -26,7 +26,6 @@ require (
 	github.com/yudai/gojsondiff v1.0.0
 	github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30
 	golang.org/x/crypto v0.32.0
-	golang.org/x/exp v0.0.0-20240719175910-8a7402abbf56
 	google.golang.org/grpc v1.70.0
 	google.golang.org/grpc/examples v0.0.0-20240223204917-5ccf176a08ab
 	gopkg.in/go-playground/pool.v3 v3.1.1
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index bf60b99be..7b46a41e1 100644
--- a/go.sum
+++ b/go.sum
@@ -246,8 +246,6 @@ golang.org/x/crypto v0.0.0-20191011191535-87dc89f01550/go.mod h1:yigFU9vqHzYiE8U
 golang.org/x/crypto v0.0.0-20200622213623-75b288015ac9/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
 golang.org/x/crypto v0.32.0 h1:euUpcYgM8WcP71gNpTqQCn6rC2t6ULUPiOzfWaXVVfc=
 golang.org/x/crypto v0.32.0/go.mod h1:ZnnJkOaASj8g0AjIduWNlq2NRxL0PlBrbKVyZ6V/Ugc=
-golang.org/x/exp v0.0.0-20240719175910-8a7402abbf56 h1:2dVuKD2vS7b0QIHQbpyTISPd0LeHDbnYEryqj5Q1ug8=
-golang.org/x/exp v0.0.0-20240719175910-8a7402abbf56/go.mod h1:M4RDyNAINzryxdtnbRXRL/OHtkFuWGRjvuhBJpk2IlY=
 golang.org/x/mod v0.2.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
 golang.org/x/mod v0.3.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
 golang.org/x/mod v0.22.0 h1:D4nJWe9zXqHOmWqj4VMOJhvzj7bEZg4wEYa759z1pH4=
```
- `internal/ingress/annotations/customheaders/main.go` [M]
```diff
diff --git a/internal/ingress/annotations/customheaders/main.go b/internal/ingress/annotations/customheaders/main.go
index bc0ef2eb5..d48018d8c 100644
--- a/internal/ingress/annotations/customheaders/main.go
+++ b/internal/ingress/annotations/customheaders/main.go
@@ -20,12 +20,12 @@ import (
 	"fmt"
 	"reflect"
 	"regexp"
+	"slices"
 
 	"k8s.io/klog/v2"
 
 	networking "k8s.io/api/networking/v1"
 
-	"golang.org/x/exp/slices"
 	"k8s.io/ingress-nginx/internal/ingress/annotations/parser"
 	ing_errors "k8s.io/ingress-nginx/internal/ingress/errors"
 	"k8s.io/ingress-nginx/internal/ingress/resolver"
```

### 🔸 Commit `a0f4a17353e099d39909d29e514ad951ecf4ab7f` - Development: Bump Kubernetes to v1.31.4. (#12783) (2025-02-03) by `k8s-infra-cherrypick-robot`
- `test/e2e/run-chart-test.sh` [M]
```diff
diff --git a/test/e2e/run-chart-test.sh b/test/e2e/run-chart-test.sh
index 10679a4c8..18b0ee72f 100755
--- a/test/e2e/run-chart-test.sh
+++ b/test/e2e/run-chart-test.sh
@@ -62,7 +62,7 @@ export KUBECONFIG="${KUBECONFIG:-$HOME/.kube/kind-config-$KIND_CLUSTER_NAME}"
 if [ "${SKIP_CLUSTER_CREATION:-false}" = "false" ]; then
   echo "[dev-env] creating Kubernetes cluster with kind"
 
-  export K8S_VERSION=${K8S_VERSION:-v1.29.2@sha256:51a1434a5397193442f0be2a297b488b6c919ce8a3931be0ce822606ea5ca245}
+  export K8S_VERSION=${K8S_VERSION:-v1.31.4@sha256:2cb39f7295fe7eafee0842b1052a599a4fb0f8bcf3f83d96c7f4864c357c6c30}
 
   kind create cluster \
     --verbosity=${KIND_LOG_LEVEL} \
```
- `test/e2e/run-kind-e2e.sh` [M]
```diff
diff --git a/test/e2e/run-kind-e2e.sh b/test/e2e/run-kind-e2e.sh
index 8202b6b83..34b773242 100755
--- a/test/e2e/run-kind-e2e.sh
+++ b/test/e2e/run-kind-e2e.sh
@@ -64,7 +64,7 @@ echo "Running e2e with nginx base image ${NGINX_BASE_IMAGE}"
 if [ "${SKIP_CLUSTER_CREATION}" = "false" ]; then
   echo "[dev-env] creating Kubernetes cluster with kind"
 
-  export K8S_VERSION=${K8S_VERSION:-v1.29.2@sha256:51a1434a5397193442f0be2a297b488b6c919ce8a3931be0ce822606ea5ca245}
+  export K8S_VERSION=${K8S_VERSION:-v1.31.4@sha256:2cb39f7295fe7eafee0842b1052a599a4fb0f8bcf3f83d96c7f4864c357c6c30}
 
   # delete the cluster if it exists
   if kind get clusters | grep "${KIND_CLUSTER_NAME}"; then
```

### 🔸 Commit `595bdcab6a2c44bf0abb9ce0623ff7d0dae12c99` - CI: Update `kubectl` to v1.31.5. (#12790) (2025-02-04) by `k8s-infra-cherrypick-robot`
- `.github/workflows/ci.yaml` [M]
```diff
diff --git a/.github/workflows/ci.yaml b/.github/workflows/ci.yaml
index c41becc38..33117264c 100644
--- a/.github/workflows/ci.yaml
+++ b/.github/workflows/ci.yaml
@@ -156,7 +156,7 @@ jobs:
 
       - name: Prepare Host
         run: |
-          curl -LO https://dl.k8s.io/release/v1.27.3/bin/linux/amd64/kubectl
+          curl -LO https://dl.k8s.io/release/v1.31.5/bin/linux/amd64/kubectl
           chmod +x ./kubectl
           sudo mv ./kubectl /usr/local/bin/kubectl
```

### 🔸 Commit `5b0b6023355835246aadbcd111c1e348ebd07d66` - Images: Update `kubectl` to v1.31.5. (#12792) (2025-02-04) by `k8s-infra-cherrypick-robot`
- `images/test-runner/Makefile` [M]
```diff
diff --git a/images/test-runner/Makefile b/images/test-runner/Makefile
index 3db9a7977..a449a7cdf 100644
--- a/images/test-runner/Makefile
+++ b/images/test-runner/Makefile
@@ -50,7 +50,7 @@ image:
 		--build-arg BASE_IMAGE=${NGINX_BASE_IMAGE} \
 		--build-arg GOLANG_VERSION=${GO_VERSION} \
 		--build-arg ETCD_VERSION=3.5.13-0 \
-		--build-arg K8S_RELEASE=v1.29.2 \
+		--build-arg K8S_RELEASE=v1.31.5 \
 		--build-arg RESTY_CLI_VERSION=0.27 \
 		--build-arg RESTY_CLI_SHA=e5f4f3128af49ba5c4d039d0554e5ae91bbe05866f60eccfa96d3653274bff90 \
 		--build-arg LUAROCKS_VERSION=3.8.0 \
@@ -71,7 +71,7 @@ build: ensure-buildx
 		--build-arg BASE_IMAGE=${NGINX_BASE_IMAGE} \
 		--build-arg GOLANG_VERSION=${GO_VERSION} \
 		--build-arg ETCD_VERSION=3.5.13-0 \
-		--build-arg K8S_RELEASE=v1.29.2 \
+		--build-arg K8S_RELEASE=v1.31.5 \
 		--build-arg RESTY_CLI_VERSION=0.27 \
... (truncated)
```

### 🔸 Commit `41cfe9a7763b5acdd1b3214f74f460dba93c40a1` - CI: Update Artifact Hub to v1.20.0. (#12794) (2025-02-04) by `k8s-infra-cherrypick-robot`
- `.github/workflows/chart.yaml` [M]
```diff
diff --git a/.github/workflows/chart.yaml b/.github/workflows/chart.yaml
index 23109a001..7c37447af 100644
--- a/.github/workflows/chart.yaml
+++ b/.github/workflows/chart.yaml
@@ -35,8 +35,8 @@ jobs:
 
       - name: Set up Artifact Hub
         run: |
-          curl --fail --location https://github.com/artifacthub/hub/releases/download/v1.19.0/ah_1.19.0_linux_amd64.tar.gz --output /tmp/ah.tar.gz
-          echo "0e430493521ce387ca04d79b26646a86f92886dbcceb44985bb71082a9530ca5  /tmp/ah.tar.gz" | shasum --check
+          curl --fail --location https://github.com/artifacthub/hub/releases/download/v1.20.0/ah_1.20.0_linux_amd64.tar.gz --output /tmp/ah.tar.gz
+          echo "9027626f19ff9f3ac668f222917130ac885e289e922e1428bfd2e7f066324e31  /tmp/ah.tar.gz" | shasum --check
           sudo tar --extract --file /tmp/ah.tar.gz --directory /usr/local/bin ah
 
       - name: Set up Git
```
- `.github/workflows/ci.yaml` [M]
```diff
diff --git a/.github/workflows/ci.yaml b/.github/workflows/ci.yaml
index 33117264c..b2ed04b6f 100644
--- a/.github/workflows/ci.yaml
+++ b/.github/workflows/ci.yaml
@@ -214,8 +214,8 @@ jobs:
 
       - name: Set up Artifact Hub
         run: |
-          curl --fail --location https://github.com/artifacthub/hub/releases/download/v1.19.0/ah_1.19.0_linux_amd64.tar.gz --output /tmp/ah.tar.gz
-          echo "0e430493521ce387ca04d79b26646a86f92886dbcceb44985bb71082a9530ca5  /tmp/ah.tar.gz" | shasum --check
+          curl --fail --location https://github.com/artifacthub/hub/releases/download/v1.20.0/ah_1.20.0_linux_amd64.tar.gz --output /tmp/ah.tar.gz
+          echo "9027626f19ff9f3ac668f222917130ac885e289e922e1428bfd2e7f066324e31  /tmp/ah.tar.gz" | shasum --check
           sudo tar --extract --file /tmp/ah.tar.gz --directory /usr/local/bin ah
 
       - name: Set up Helm Docs
```

### 🔸 Commit `4d6d237745683e580aee60232f529ad67b0b4e00` - Go: Bump to v1.23.6. (#12800) (2025-02-05) by `k8s-infra-cherrypick-robot`
- `GOLANG_VERSION` [M]
```diff
diff --git a/GOLANG_VERSION b/GOLANG_VERSION
index ca8ec414e..d8c40e539 100644
--- a/GOLANG_VERSION
+++ b/GOLANG_VERSION
@@ -1 +1 @@
-1.23.5
+1.23.6
```
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index c96d19c4f..0dfbc5670 100644
--- a/go.mod
+++ b/go.mod
@@ -1,6 +1,6 @@
 module k8s.io/ingress-nginx
 
-go 1.23.5
+go 1.23.6
 
 require (
 	dario.cat/mergo v1.0.1
```
- `images/custom-error-pages/rootfs/go.mod` [M]
```diff
diff --git a/images/custom-error-pages/rootfs/go.mod b/images/custom-error-pages/rootfs/go.mod
index e221e8e41..5c0377284 100644
--- a/images/custom-error-pages/rootfs/go.mod
+++ b/images/custom-error-pages/rootfs/go.mod
@@ -1,6 +1,6 @@
 module k8s.io/ingress-nginx/custom-error-pages
 
-go 1.23.5
+go 1.23.6
 
 require github.com/prometheus/client_golang v1.20.5
```
- `images/ext-auth-example-authsvc/rootfs/go.mod` [M]
```diff
diff --git a/images/ext-auth-example-authsvc/rootfs/go.mod b/images/ext-auth-example-authsvc/rootfs/go.mod
index 8db2af11b..186467b24 100644
--- a/images/ext-auth-example-authsvc/rootfs/go.mod
+++ b/images/ext-auth-example-authsvc/rootfs/go.mod
@@ -1,6 +1,6 @@
 module example.com/authsvc
 
-go 1.23.5
+go 1.23.6
 
 require k8s.io/apimachinery v0.32.1
```
- `images/kube-webhook-certgen/rootfs/go.mod` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.mod b/images/kube-webhook-certgen/rootfs/go.mod
index bab5f8775..343e325a7 100644
--- a/images/kube-webhook-certgen/rootfs/go.mod
+++ b/images/kube-webhook-certgen/rootfs/go.mod
@@ -1,6 +1,6 @@
 module github.com/jet/kube-webhook-certgen
 
-go 1.23.5
+go 1.23.6
 
 require (
 	github.com/onrik/logrus v0.11.0
```
- `magefiles/go.mod` [M]
```diff
diff --git a/magefiles/go.mod b/magefiles/go.mod
index 5bb8b79ee..f11ab740e 100644
--- a/magefiles/go.mod
+++ b/magefiles/go.mod
@@ -1,6 +1,6 @@
 module k8s.io/ingress-nginx/magefiles
 
-go 1.23.5
+go 1.23.6
 
 require (
 	github.com/blang/semver/v4 v4.0.0
```

### 🔸 Commit `b3c2c188ff8be9fa999aae84e0054ae9b1c3e318` - Docs: Enable code copy button. (#12806) (2025-02-07) by `k8s-infra-cherrypick-robot`
- `mkdocs.yml` [M]
```diff
diff --git a/mkdocs.yml b/mkdocs.yml
index 4b010c5ff..bb7745921 100644
--- a/mkdocs.yml
+++ b/mkdocs.yml
@@ -50,6 +50,7 @@ theme:
     - navigation.tabs.sticky
     - navigation.instant
     - navigation.sections
+    - content.code.copy
 
   palette:
     primary: "teal"
```

### 🔸 Commit `2c026151e45b224c49839e7b53c1317e154e3323` - Docs: Migrate to AR. (#12808) (2025-02-08) by `k8s-infra-cherrypick-robot`
- `MANUAL_RELEASE.md` [M]
```diff
diff --git a/MANUAL_RELEASE.md b/MANUAL_RELEASE.md
index 8a6b10bc1..0ae7a4e37 100644
--- a/MANUAL_RELEASE.md
+++ b/MANUAL_RELEASE.md
@@ -93,7 +93,7 @@ Promoting the images basically means that images, that were pushed to staging co
 
   ```
   ...
-  pushing manifest for gcr.io/k8s-staging-ingress-nginx/controller:v1.0.2@sha256:e15fac6e8474d77e1f017edc33d804ce72a184e3c0a30963b2a0d7f0b89f6b16
+  pushing manifest for us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx/controller:v1.0.2@sha256:e15fac6e8474d77e1f017edc33d804ce72a184e3c0a30963b2a0d7f0b89f6b16
   ...
   ```
 
@@ -113,7 +113,7 @@ Promoting the images basically means that images, that were pushed to staging co
 
 - For making, it easier, you can edit your branch directly in the browser. But be careful about making any mistake.
 
-- Insert the sha(s) & the tag(s), in a new line, in this file [Project kubernetes/k8s.io Ingress-Nginx-Controller Images](https://github.com/kubernetes/k8s.io/blob/main/k8s.gcr.io/images/k8s-staging-ingress-nginx/images.yaml)  Look at this [example PR and the diff](https://github.com/kubernetes/k8s.io/pull/2536) to see how it was done before
+- Insert the sha(s) & the tag(s), in a new line, in this file [Project kubernetes/k8s.io Ingress-Nginx-Controller Images](https://github.com/kubernetes/k8s.io/blob/main/registry.k8s.io/images/k8s-staging-ingress-nginx/images.yaml)  Look at this [example PR and the diff](https://github.com/kubernetes/k8s.io/pull/2536) to see how it was done before
 
... (truncated)
```
- `NEW_CONTRIBUTOR.md` [M]
```diff
diff --git a/NEW_CONTRIBUTOR.md b/NEW_CONTRIBUTOR.md
index 20c4e3daa..c9668430c 100644
--- a/NEW_CONTRIBUTOR.md
+++ b/NEW_CONTRIBUTOR.md
@@ -325,9 +325,9 @@ minikube start
 🐳  Preparing Kubernetes v1.23.3 on Docker 20.10.12 ...
     ▪ kubelet.housekeeping-interval=5m
 🔎  Verifying Kubernetes components...
-    ▪ Using image k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1
-    ▪ Using image k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1
-    ▪ Using image k8s.gcr.io/ingress-nginx/controller:v1.2.1
+    ▪ Using image registry.k8s.io/ingress-nginx/kube-webhook-certgen:v1.1.1
+    ▪ Using image registry.k8s.io/ingress-nginx/kube-webhook-certgen:v1.1.1
+    ▪ Using image registry.k8s.io/ingress-nginx/controller:v1.2.1
     ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
 🔎  Verifying ingress addon...
 🌟  Enabled addons: ingress, storage-provisioner, default-storageclass
```
- `ginkgo_upgrade.md` [M]
```diff
diff --git a/ginkgo_upgrade.md b/ginkgo_upgrade.md
index 57db0f28f..87e6bd9fd 100644
--- a/ginkgo_upgrade.md
+++ b/ginkgo_upgrade.md
@@ -49,7 +49,7 @@ Promoting the images basically means that images, that were pushed to staging co
 
   ```
   ...
-  pushing manifest for gcr.io/k8s-staging-ingress-nginx/controller:v1.0.2@sha256:e15fac6e8474d77e1f017edc33d804ce72a184e3c0a30963b2a0d7f0b89f6b16
+  pushing manifest for us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx/controller:v1.0.2@sha256:e15fac6e8474d77e1f017edc33d804ce72a184e3c0a30963b2a0d7f0b89f6b16
   ...
   ```
 
@@ -65,11 +65,11 @@ Promoting the images basically means that images, that were pushed to staging co
 
 - Create a branch in your fork, named as the issue number for this release
 
-- In the related branch, of your fork, edit the file k8s.gcr.io/images/k8s-staging-ingress-nginx/images.yaml.
+- In the related branch, of your fork, edit the file registry.k8s.io/images/k8s-staging-ingress-nginx/images.yaml.
 
... (truncated)
```

### 🔸 Commit `f7d4e2b3ee39f54bca2c19279fda4ba64cebe51e` - Bump golang.org/x/crypto from 0.32.0 to 0.33.0 (#12813) (2025-02-10) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 0dfbc5670..06c564a17 100644
--- a/go.mod
+++ b/go.mod
@@ -25,7 +25,7 @@ require (
 	github.com/stretchr/testify v1.10.0
 	github.com/yudai/gojsondiff v1.0.0
 	github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30
-	golang.org/x/crypto v0.32.0
+	golang.org/x/crypto v0.33.0
 	google.golang.org/grpc v1.70.0
 	google.golang.org/grpc/examples v0.0.0-20240223204917-5ccf176a08ab
 	gopkg.in/go-playground/pool.v3 v3.1.1
@@ -115,10 +115,10 @@ require (
 	golang.org/x/mod v0.22.0 // indirect
 	golang.org/x/net v0.33.0 // indirect
 	golang.org/x/oauth2 v0.24.0 // indirect
-	golang.org/x/sync v0.10.0 // indirect
-	golang.org/x/sys v0.29.0 // indirect
-	golang.org/x/term v0.28.0 // indirect
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 7b46a41e1..4123f644c 100644
--- a/go.sum
+++ b/go.sum
@@ -244,8 +244,8 @@ go.uber.org/zap v1.27.0/go.mod h1:GB2qFLM7cTU87MWRP2mPIjqfIDnGu+VIO4V/SdhGo2E=
 golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
 golang.org/x/crypto v0.0.0-20191011191535-87dc89f01550/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
 golang.org/x/crypto v0.0.0-20200622213623-75b288015ac9/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
-golang.org/x/crypto v0.32.0 h1:euUpcYgM8WcP71gNpTqQCn6rC2t6ULUPiOzfWaXVVfc=
-golang.org/x/crypto v0.32.0/go.mod h1:ZnnJkOaASj8g0AjIduWNlq2NRxL0PlBrbKVyZ6V/Ugc=
+golang.org/x/crypto v0.33.0 h1:IOBPskki6Lysi0lo9qQvbxiQ+FvsCC/YWOecCHAixus=
+golang.org/x/crypto v0.33.0/go.mod h1:bVdXmD7IV/4GdElGPozy6U7lWdRXA4qyRVGJV57uQ5M=
 golang.org/x/mod v0.2.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
 golang.org/x/mod v0.3.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
 golang.org/x/mod v0.22.0 h1:D4nJWe9zXqHOmWqj4VMOJhvzj7bEZg4wEYa759z1pH4=
@@ -264,8 +264,8 @@ golang.org/x/sync v0.0.0-20180314180146-1d60e4601c6f/go.mod h1:RxMgew5VJxzue5/jJ
 golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
 golang.org/x/sync v0.0.0-20190911185100-cd5d95a43a6e/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
 golang.org/x/sync v0.0.0-20201020160332-67f06af15bc9/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
-golang.org/x/sync v0.10.0 h1:3NQrjDixjgGwUOCaF8w2+VYHv0Ve/vGYSbdkTa98gmQ=
... (truncated)
```

### 🔸 Commit `ad75df8a5193f0d8c1a317ef6b526f4039c5b157` - Bump the actions group with 4 updates (#12815) (2025-02-10) by `k8s-infra-cherrypick-robot`
- `.github/workflows/ci.yaml` [M]
```diff
diff --git a/.github/workflows/ci.yaml b/.github/workflows/ci.yaml
index b2ed04b6f..5a4d572de 100644
--- a/.github/workflows/ci.yaml
+++ b/.github/workflows/ci.yaml
@@ -143,11 +143,11 @@ jobs:
           check-latest: true
 
       - name: Set up QEMU
-        uses: docker/setup-qemu-action@53851d14592bedcffcf25ea515637cff71ef929a # v3.3.0
+        uses: docker/setup-qemu-action@4574d27a4764455b42196d70a065bc6853246a25 # v3.4.0
 
       - name: Set up Docker Buildx
         id: buildx
-        uses: docker/setup-buildx-action@6524bf65af31da8d45b59e8c27de4bd072b392f5 # v3.8.0
+        uses: docker/setup-buildx-action@f7ce87c1d6bead3e36075b2ce75da1f6cc28aaca # v3.9.0
         with:
           version: latest
```
- `.github/workflows/golangci-lint.yml` [M]
```diff
diff --git a/.github/workflows/golangci-lint.yml b/.github/workflows/golangci-lint.yml
index b69725dde..1c3a94c9d 100644
--- a/.github/workflows/golangci-lint.yml
+++ b/.github/workflows/golangci-lint.yml
@@ -28,7 +28,7 @@ jobs:
           check-latest: true
 
       - name: golangci-lint
-        uses: golangci/golangci-lint-action@ec5d18412c0aeab7936cb16880d708ba2a64e1ae # v6.2.0
+        uses: golangci/golangci-lint-action@2e788936b09dd82dc280e845628a40d2ba6b204c # v6.3.1
         with:
           version: v1.62
           only-new-issues: true
```
- `.github/workflows/images.yaml` [M]
```diff
diff --git a/.github/workflows/images.yaml b/.github/workflows/images.yaml
index 69f9a9d9d..d9b8b34a1 100644
--- a/.github/workflows/images.yaml
+++ b/.github/workflows/images.yaml
@@ -194,10 +194,10 @@ jobs:
       - name: Checkout
         uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
       - name: Set up QEMU
-        uses: docker/setup-qemu-action@53851d14592bedcffcf25ea515637cff71ef929a # v3.3.0
+        uses: docker/setup-qemu-action@4574d27a4764455b42196d70a065bc6853246a25 # v3.4.0
       - name: Set up Docker Buildx
         id: buildx
-        uses: docker/setup-buildx-action@6524bf65af31da8d45b59e8c27de4bd072b392f5 # v3.8.0
+        uses: docker/setup-buildx-action@f7ce87c1d6bead3e36075b2ce75da1f6cc28aaca # v3.9.0
         with:
           version: latest
           platforms: ${{ env.PLATFORMS }}
```
- `.github/workflows/scorecards.yml` [M]
```diff
diff --git a/.github/workflows/scorecards.yml b/.github/workflows/scorecards.yml
index b9b88a9d9..a4473710d 100644
--- a/.github/workflows/scorecards.yml
+++ b/.github/workflows/scorecards.yml
@@ -59,6 +59,6 @@ jobs:
 
       # Upload the results to GitHub's code scanning dashboard.
       - name: "Upload to code-scanning"
-        uses: github/codeql-action/upload-sarif@dd746615b3b9d728a6a37ca2045b68ca76d4841a # v3.28.8
+        uses: github/codeql-action/upload-sarif@9e8d0789d4a0fa9ceb6b1738f7e269594bdd67f0 # v3.28.9
         with:
           sarif_file: results.sarif
```
- `.github/workflows/vulnerability-scans.yaml` [M]
```diff
diff --git a/.github/workflows/vulnerability-scans.yaml b/.github/workflows/vulnerability-scans.yaml
index 0215c5de2..4461d9757 100644
--- a/.github/workflows/vulnerability-scans.yaml
+++ b/.github/workflows/vulnerability-scans.yaml
@@ -75,7 +75,7 @@ jobs:
 
       # This step checks out a copy of your repository.
       - name: Upload SARIF file
-        uses: github/codeql-action/upload-sarif@dd746615b3b9d728a6a37ca2045b68ca76d4841a # v3.28.8
+        uses: github/codeql-action/upload-sarif@9e8d0789d4a0fa9ceb6b1738f7e269594bdd67f0 # v3.28.9
         with:
           token: ${{ github.token }}
           # Path to SARIF file relative to the root of the repository
```

### 🔸 Commit `8b8996a2fe3d00cb8f0df45307002381483ca4d4` - Images: Migrate to AR. (1/2) (#12847) (2025-02-14) by `k8s-infra-cherrypick-robot`
- `Makefile` [M]
```diff
diff --git a/Makefile b/Makefile
index 3ff56fc47..0b8f1f5c2 100644
--- a/Makefile
+++ b/Makefile
@@ -58,7 +58,7 @@ ifneq ($(PLATFORM),)
 	PLATFORM_FLAG="--platform"
 endif
 
-REGISTRY ?= gcr.io/k8s-staging-ingress-nginx
+REGISTRY ?= us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
 
 BASE_IMAGE ?= $(shell cat NGINX_BASE)
```
- `cloudbuild.yaml` [M]
```diff
diff --git a/cloudbuild.yaml b/cloudbuild.yaml
index cb74da0a5..0bb2b60a4 100644
--- a/cloudbuild.yaml
+++ b/cloudbuild.yaml
@@ -4,7 +4,7 @@ options:
 steps:
   - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
-      - REGISTRY=gcr.io/k8s-staging-ingress-nginx
+      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
       - REPO_INFO=https://github.com/kubernetes/ingress-nginx
       - COMMIT_SHA=${_PULL_BASE_SHA}
       - BUILD_ID=${BUILD_ID}
```
- `images/cfssl/cloudbuild.yaml` [M]
```diff
diff --git a/images/cfssl/cloudbuild.yaml b/images/cfssl/cloudbuild.yaml
index 612bae942..33fafdb08 100644
--- a/images/cfssl/cloudbuild.yaml
+++ b/images/cfssl/cloudbuild.yaml
@@ -4,7 +4,7 @@ options:
 steps:
   - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
-      - REGISTRY=gcr.io/k8s-staging-ingress-nginx
+      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
     entrypoint: bash
     args:
       - -c
```
- `images/custom-error-pages/cloudbuild.yaml` [M]
```diff
diff --git a/images/custom-error-pages/cloudbuild.yaml b/images/custom-error-pages/cloudbuild.yaml
index 7a37591f8..324a8f19a 100644
--- a/images/custom-error-pages/cloudbuild.yaml
+++ b/images/custom-error-pages/cloudbuild.yaml
@@ -4,7 +4,7 @@ options:
 steps:
   - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
-      - REGISTRY=gcr.io/k8s-staging-ingress-nginx
+      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
     entrypoint: bash
     args:
       - -c
```
- `images/e2e-test-echo/cloudbuild.yaml` [M]
```diff
diff --git a/images/e2e-test-echo/cloudbuild.yaml b/images/e2e-test-echo/cloudbuild.yaml
index ada4486a4..02bfc034a 100644
--- a/images/e2e-test-echo/cloudbuild.yaml
+++ b/images/e2e-test-echo/cloudbuild.yaml
@@ -4,7 +4,7 @@ options:
 steps:
   - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
-      - REGISTRY=gcr.io/k8s-staging-ingress-nginx
+      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
     entrypoint: bash
     args:
       - -c
```
- `images/fastcgi-helloserver/cloudbuild.yaml` [M]
```diff
diff --git a/images/fastcgi-helloserver/cloudbuild.yaml b/images/fastcgi-helloserver/cloudbuild.yaml
index 9dc5588a1..c2c6135df 100644
--- a/images/fastcgi-helloserver/cloudbuild.yaml
+++ b/images/fastcgi-helloserver/cloudbuild.yaml
@@ -4,7 +4,7 @@ options:
 steps:
   - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
-      - REGISTRY=gcr.io/k8s-staging-ingress-nginx
+      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
     entrypoint: bash
     args:
       - -c
```

### 🔸 Commit `458051a516a5e16abb9e88479ac4f0c15ed02d70` - Images: Migrate to AR. (2/2) (#12850) (2025-02-14) by `k8s-infra-cherrypick-robot`
- `images/httpbun/cloudbuild.yaml` [M]
```diff
diff --git a/images/httpbun/cloudbuild.yaml b/images/httpbun/cloudbuild.yaml
index 741a5ebee..c56820d15 100644
--- a/images/httpbun/cloudbuild.yaml
+++ b/images/httpbun/cloudbuild.yaml
@@ -4,7 +4,7 @@ options:
 steps:
   - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
-      - REGISTRY=gcr.io/k8s-staging-ingress-nginx
+      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
     entrypoint: bash
     args:
       - -c
```
- `images/kube-webhook-certgen/cloudbuild.yaml` [M]
```diff
diff --git a/images/kube-webhook-certgen/cloudbuild.yaml b/images/kube-webhook-certgen/cloudbuild.yaml
index 3f05ff099..e4118ff88 100644
--- a/images/kube-webhook-certgen/cloudbuild.yaml
+++ b/images/kube-webhook-certgen/cloudbuild.yaml
@@ -4,7 +4,7 @@ options:
 steps:
   - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
-      - REGISTRY=gcr.io/k8s-staging-ingress-nginx
+      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
     entrypoint: bash
     args:
       - -c
```
- `images/nginx/Makefile` [M]
```diff
diff --git a/images/nginx/Makefile b/images/nginx/Makefile
index 3ed502759..3cc14e5b3 100644
--- a/images/nginx/Makefile
+++ b/images/nginx/Makefile
@@ -24,7 +24,7 @@ INIT_BUILDX=$(DIR)/../../hack/init-buildx.sh
 SHORT_SHA ?=$(shell git rev-parse --short HEAD)
 TAG ?=$(shell cat TAG)
 
-REGISTRY ?= gcr.io/k8s-staging-ingress-nginx
+REGISTRY ?= us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
 
 IMAGE = $(REGISTRY)/nginx
```
- `images/nginx/cloudbuild.yaml` [M]
```diff
diff --git a/images/nginx/cloudbuild.yaml b/images/nginx/cloudbuild.yaml
index c07c36a92..2563692d7 100644
--- a/images/nginx/cloudbuild.yaml
+++ b/images/nginx/cloudbuild.yaml
@@ -6,7 +6,7 @@ options:
 steps:
   - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
-      - REGISTRY=gcr.io/k8s-staging-ingress-nginx
+      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
     entrypoint: bash
     args:
       - -c
```
- `images/test-runner/cloudbuild.yaml` [M]
```diff
diff --git a/images/test-runner/cloudbuild.yaml b/images/test-runner/cloudbuild.yaml
index bec8f3694..93dce3ec9 100644
--- a/images/test-runner/cloudbuild.yaml
+++ b/images/test-runner/cloudbuild.yaml
@@ -4,7 +4,7 @@ options:
 steps:
   - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
     env:
-      - REGISTRY=gcr.io/k8s-staging-ingress-nginx
+      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
     entrypoint: bash
     args:
       - -c
```

### 🔸 Commit `f8df661b4ba1f859a88e54092ee0cda1d6265711` - CI: Update `kubectl` to v1.32.2. (#12852) (2025-02-14) by `k8s-infra-cherrypick-robot`
- `.github/workflows/ci.yaml` [M]
```diff
diff --git a/.github/workflows/ci.yaml b/.github/workflows/ci.yaml
index 5a4d572de..319ef12ce 100644
--- a/.github/workflows/ci.yaml
+++ b/.github/workflows/ci.yaml
@@ -156,7 +156,7 @@ jobs:
 
       - name: Prepare Host
         run: |
-          curl -LO https://dl.k8s.io/release/v1.31.5/bin/linux/amd64/kubectl
+          curl -LO https://dl.k8s.io/release/v1.32.2/bin/linux/amd64/kubectl
           chmod +x ./kubectl
           sudo mv ./kubectl /usr/local/bin/kubectl
```

### 🔸 Commit `97b93720b9fcc5272bee35e94a0782d9ba0909ed` - Development: Update Kubernetes to v1.32.0. (#12854) (2025-02-14) by `k8s-infra-cherrypick-robot`
- `build/dev-env.sh` [M]
```diff
diff --git a/build/dev-env.sh b/build/dev-env.sh
index 6bbd8c22c..dd1518ee0 100755
--- a/build/dev-env.sh
+++ b/build/dev-env.sh
@@ -64,7 +64,7 @@ echo "[dev-env] building image"
 make build image
 docker tag "${REGISTRY}/controller:${TAG}" "${DEV_IMAGE}"
 
-export K8S_VERSION=${K8S_VERSION:-v1.31.4@sha256:2cb39f7295fe7eafee0842b1052a599a4fb0f8bcf3f83d96c7f4864c357c6c30}
+export K8S_VERSION=${K8S_VERSION:-v1.32.0@sha256:c48c62eac5da28cdadcf560d1d8616cfa6783b58f0d94cf63ad1bf49600cb027}
 
 KIND_CLUSTER_NAME="ingress-nginx-dev"
```
- `test/e2e/run-chart-test.sh` [M]
```diff
diff --git a/test/e2e/run-chart-test.sh b/test/e2e/run-chart-test.sh
index 18b0ee72f..b998600d0 100755
--- a/test/e2e/run-chart-test.sh
+++ b/test/e2e/run-chart-test.sh
@@ -62,7 +62,7 @@ export KUBECONFIG="${KUBECONFIG:-$HOME/.kube/kind-config-$KIND_CLUSTER_NAME}"
 if [ "${SKIP_CLUSTER_CREATION:-false}" = "false" ]; then
   echo "[dev-env] creating Kubernetes cluster with kind"
 
-  export K8S_VERSION=${K8S_VERSION:-v1.31.4@sha256:2cb39f7295fe7eafee0842b1052a599a4fb0f8bcf3f83d96c7f4864c357c6c30}
+  export K8S_VERSION=${K8S_VERSION:-v1.32.0@sha256:c48c62eac5da28cdadcf560d1d8616cfa6783b58f0d94cf63ad1bf49600cb027}
 
   kind create cluster \
     --verbosity=${KIND_LOG_LEVEL} \
```
- `test/e2e/run-kind-e2e.sh` [M]
```diff
diff --git a/test/e2e/run-kind-e2e.sh b/test/e2e/run-kind-e2e.sh
index 34b773242..0fcdc61ca 100755
--- a/test/e2e/run-kind-e2e.sh
+++ b/test/e2e/run-kind-e2e.sh
@@ -64,7 +64,7 @@ echo "Running e2e with nginx base image ${NGINX_BASE_IMAGE}"
 if [ "${SKIP_CLUSTER_CREATION}" = "false" ]; then
   echo "[dev-env] creating Kubernetes cluster with kind"
 
-  export K8S_VERSION=${K8S_VERSION:-v1.31.4@sha256:2cb39f7295fe7eafee0842b1052a599a4fb0f8bcf3f83d96c7f4864c357c6c30}
+  export K8S_VERSION=${K8S_VERSION:-v1.32.0@sha256:c48c62eac5da28cdadcf560d1d8616cfa6783b58f0d94cf63ad1bf49600cb027}
 
   # delete the cluster if it exists
   if kind get clusters | grep "${KIND_CLUSTER_NAME}"; then
```

### 🔸 Commit `a3a05746bf68b7ff40108da10cf89b318b1e93a7` - Images: Update `kubectl` to v1.32.2. (#12855) (2025-02-15) by `k8s-infra-cherrypick-robot`
- `images/test-runner/Makefile` [M]
```diff
diff --git a/images/test-runner/Makefile b/images/test-runner/Makefile
index a449a7cdf..8adbf0b41 100644
--- a/images/test-runner/Makefile
+++ b/images/test-runner/Makefile
@@ -50,7 +50,7 @@ image:
 		--build-arg BASE_IMAGE=${NGINX_BASE_IMAGE} \
 		--build-arg GOLANG_VERSION=${GO_VERSION} \
 		--build-arg ETCD_VERSION=3.5.13-0 \
-		--build-arg K8S_RELEASE=v1.31.5 \
+		--build-arg K8S_RELEASE=v1.32.2 \
 		--build-arg RESTY_CLI_VERSION=0.27 \
 		--build-arg RESTY_CLI_SHA=e5f4f3128af49ba5c4d039d0554e5ae91bbe05866f60eccfa96d3653274bff90 \
 		--build-arg LUAROCKS_VERSION=3.8.0 \
@@ -71,7 +71,7 @@ build: ensure-buildx
 		--build-arg BASE_IMAGE=${NGINX_BASE_IMAGE} \
 		--build-arg GOLANG_VERSION=${GO_VERSION} \
 		--build-arg ETCD_VERSION=3.5.13-0 \
-		--build-arg K8S_RELEASE=v1.31.5 \
+		--build-arg K8S_RELEASE=v1.32.2 \
 		--build-arg RESTY_CLI_VERSION=0.27 \
... (truncated)
```

### 🔸 Commit `be1d67582ff4c7fdd25e586900f7e2e239d6dc59` - Bump github.com/spf13/cobra from 1.8.1 to 1.9.1 in /images/kube-webhook-certgen/rootfs (#12862) (2025-02-17) by `k8s-infra-cherrypick-robot`
- `images/kube-webhook-certgen/rootfs/go.mod` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.mod b/images/kube-webhook-certgen/rootfs/go.mod
index 343e325a7..7836f790f 100644
--- a/images/kube-webhook-certgen/rootfs/go.mod
+++ b/images/kube-webhook-certgen/rootfs/go.mod
@@ -5,7 +5,7 @@ go 1.23.6
 require (
 	github.com/onrik/logrus v0.11.0
 	github.com/sirupsen/logrus v1.9.3
-	github.com/spf13/cobra v1.8.1
+	github.com/spf13/cobra v1.9.1
 	k8s.io/api v0.32.1
 	k8s.io/apimachinery v0.32.1
 	k8s.io/client-go v0.32.1
```
- `images/kube-webhook-certgen/rootfs/go.sum` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.sum b/images/kube-webhook-certgen/rootfs/go.sum
index ba5876b08..77e6a5284 100644
--- a/images/kube-webhook-certgen/rootfs/go.sum
+++ b/images/kube-webhook-certgen/rootfs/go.sum
@@ -1,4 +1,4 @@
-github.com/cpuguy83/go-md2man/v2 v2.0.4/go.mod h1:tgQtvFlXSQOSOSIRvRPT7W67SCa46tRHOmNcaadrF8o=
+github.com/cpuguy83/go-md2man/v2 v2.0.6/go.mod h1:oOW0eioCTA6cOiMLiUPZOpcVxMig6NIQQ7OS05n1F4g=
 github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
 github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
 github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc h1:U9qPSI2PIWSS1VwoXQT9A3Wy9MM3WgvqSxFWenqJduM=
@@ -70,9 +70,8 @@ github.com/rogpeppe/go-internal v1.12.0/go.mod h1:E+RYuTGaKKdloAfM02xzb0FW3Paa99
 github.com/russross/blackfriday/v2 v2.1.0/go.mod h1:+Rmxgy9KzJVeS9/2gXHxylqXiyQDYRxCVz55jmeOWTM=
 github.com/sirupsen/logrus v1.9.3 h1:dueUQJ1C2q9oE3F7wvmSGAaVtTmUizReu6fjN8uqzbQ=
 github.com/sirupsen/logrus v1.9.3/go.mod h1:naHLuLoDiP4jHNo9R0sCBMtWGeIprob74mVsIT4qYEQ=
-github.com/spf13/cobra v1.8.1 h1:e5/vxKd/rZsfSJMUX1agtjeTDf+qv1/JdBF8gg5k9ZM=
-github.com/spf13/cobra v1.8.1/go.mod h1:wHxEcudfqmLYa8iTfL+OuZPbBZkmvliBWKIezN3kD9Y=
-github.com/spf13/pflag v1.0.5/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
+github.com/spf13/cobra v1.9.1 h1:CXSaggrXdbHK9CF+8ywj8Amf7PBRmPCOJugH954Nnlo=
+github.com/spf13/cobra v1.9.1/go.mod h1:nDyEzZ8ogv936Cinf6g1RU9MRY64Ir93oCnqb9wxYW0=
 github.com/spf13/pflag v1.0.6 h1:jFzHGLGAlb3ruxLB8MhbI6A8+AQX/2eW4qeyNZXNp2o=
... (truncated)
```

### 🔸 Commit `b90e059448ddfd9dabbf73c63b4a9bbdfc079a92` - Bump the actions group with 2 updates (#12864) (2025-02-17) by `k8s-infra-cherrypick-robot`
- `.github/workflows/golangci-lint.yml` [M]
```diff
diff --git a/.github/workflows/golangci-lint.yml b/.github/workflows/golangci-lint.yml
index 1c3a94c9d..f57878084 100644
--- a/.github/workflows/golangci-lint.yml
+++ b/.github/workflows/golangci-lint.yml
@@ -28,7 +28,7 @@ jobs:
           check-latest: true
 
       - name: golangci-lint
-        uses: golangci/golangci-lint-action@2e788936b09dd82dc280e845628a40d2ba6b204c # v6.3.1
+        uses: golangci/golangci-lint-action@2226d7cb06a077cd73e56eedd38eecad18e5d837 # v6.5.0
         with:
           version: v1.62
           only-new-issues: true
```
- `.github/workflows/plugin.yaml` [M]
```diff
diff --git a/.github/workflows/plugin.yaml b/.github/workflows/plugin.yaml
index 8e203c373..20f2caeae 100644
--- a/.github/workflows/plugin.yaml
+++ b/.github/workflows/plugin.yaml
@@ -27,7 +27,7 @@ jobs:
 
       - name: Run GoReleaser Snapshot
         if: ${{ ! startsWith(github.ref, 'refs/tags/') }}
-        uses: goreleaser/goreleaser-action@9ed2f89a662bf1735a48bc8557fd212fa902bebf # v6.1.0
+        uses: goreleaser/goreleaser-action@90a3faa9d0182683851fbfa97ca1a2cb983bfca3 # v6.2.1
         with:
           version: "~> v2"
           args: release --snapshot --clean
@@ -36,7 +36,7 @@ jobs:
 
       - name: Run GoReleaser
         if: ${{ startsWith(github.ref, 'refs/tags/') }}
-        uses: goreleaser/goreleaser-action@9ed2f89a662bf1735a48bc8557fd212fa902bebf # v6.1.0
+        uses: goreleaser/goreleaser-action@90a3faa9d0182683851fbfa97ca1a2cb983bfca3 # v6.2.1
         with:
... (truncated)
```
- `.golangci.yml` [M]
```diff
diff --git a/.golangci.yml b/.golangci.yml
index 2d73e14e7..729468711 100644
--- a/.golangci.yml
+++ b/.golangci.yml
@@ -2,6 +2,7 @@ run:
   timeout: 10m
   allow-parallel-runners: true
 
+issues:
   # Maximum issues count per one linter. Set to 0 to disable. Default is 50.
   max-issues-per-linter: 0
 
@@ -226,9 +227,6 @@ linters-settings:
   nolintlint:
     # Enable to ensure that nolint directives are all used. Default is true.
     allow-unused: false
-    # Disable to ensure that nolint directives don't have a leading space. Default is true.
-    # TODO(lint): Enforce machine-readable `nolint` directives
-    allow-leading-space: true
     # Exclude following linters from requiring an explanation.  Default is [].
... (truncated)
```

### 🔸 Commit `65d6d463ef635fd1a950c960c82d9bd7f7f07c1f` - Bump the go group across 3 directories with 11 updates (#12866) (2025-02-17) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 06c564a17..867a4ec00 100644
--- a/go.mod
+++ b/go.mod
@@ -15,7 +15,7 @@ require (
 	github.com/moul/pb v0.0.0-20220425114252-bca18df4138c
 	github.com/ncabatoff/process-exporter v0.8.5
 	github.com/onsi/ginkgo/v2 v2.22.2
-	github.com/opencontainers/runc v1.2.4
+	github.com/opencontainers/runc v1.2.5
 	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2
 	github.com/prometheus/client_golang v1.20.5
 	github.com/prometheus/client_model v0.6.1
@@ -30,17 +30,17 @@ require (
 	google.golang.org/grpc/examples v0.0.0-20240223204917-5ccf176a08ab
 	gopkg.in/go-playground/pool.v3 v3.1.1
 	gopkg.in/mcuadros/go-syslog.v2 v2.3.0
-	k8s.io/api v0.32.1
-	k8s.io/apiextensions-apiserver v0.32.1
-	k8s.io/apimachinery v0.32.1
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 4123f644c..3f91c4f00 100644
--- a/go.sum
+++ b/go.sum
@@ -21,8 +21,8 @@ github.com/coreos/go-systemd/v22 v22.5.0/go.mod h1:Y58oyj3AT4RCenI/lSvhwexgC+NSV
 github.com/cpuguy83/go-md2man/v2 v2.0.4/go.mod h1:tgQtvFlXSQOSOSIRvRPT7W67SCa46tRHOmNcaadrF8o=
 github.com/creack/pty v1.1.18 h1:n56/Zwd5o6whRC5PMGretI4IdRLlmBXYNjScPaBgsbY=
 github.com/creack/pty v1.1.18/go.mod h1:MOBLtS5ELjhRRrroQr9kyvTxUAFNvYEK993ew/Vr4O4=
-github.com/cyphar/filepath-securejoin v0.3.5 h1:L81NHjquoQmcPgXcttUS9qTSR/+bXry6pbSINQGpjj4=
-github.com/cyphar/filepath-securejoin v0.3.5/go.mod h1:edhVd3c6OXKjUmSrVa/tGJRS9joFTxlslFCAyaxigkE=
+github.com/cyphar/filepath-securejoin v0.4.1 h1:JyxxyPEaktOD+GAnqIqTf9A8tHyAG22rowi7HkoSU1s=
+github.com/cyphar/filepath-securejoin v0.4.1/go.mod h1:Sdj7gXlvMcPZsbhwhQ33GguGLDGQL7h7bg04C/+u9jI=
 github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
 github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
 github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc h1:U9qPSI2PIWSS1VwoXQT9A3Wy9MM3WgvqSxFWenqJduM=
@@ -33,8 +33,8 @@ github.com/eapache/queue v1.1.0 h1:YOEu7KNc61ntiQlcEeUIoDTJ2o8mQznoNvUhiigpIqc=
 github.com/eapache/queue v1.1.0/go.mod h1:6eCeP0CKFpHLu8blIFXhExK/dRa7WDZfr6jVFPTqq+I=
 github.com/emicklei/go-restful/v3 v3.12.0 h1:y2DdzBAURM29NFF94q6RaY4vjIH1rtwDapwQtU84iWk=
 github.com/emicklei/go-restful/v3 v3.12.0/go.mod h1:6n3XBCmQQb25CM2LCACGz8ukIrRry+4bhvbpWn3mrbc=
-github.com/evanphx/json-patch/v5 v5.9.0 h1:kcBlZQbplgElYIlo/n1hJbls2z/1awpXxpRi0/FOJfg=
... (truncated)
```
- `images/ext-auth-example-authsvc/rootfs/go.mod` [M]
```diff
diff --git a/images/ext-auth-example-authsvc/rootfs/go.mod b/images/ext-auth-example-authsvc/rootfs/go.mod
index 186467b24..5f33a86ff 100644
--- a/images/ext-auth-example-authsvc/rootfs/go.mod
+++ b/images/ext-auth-example-authsvc/rootfs/go.mod
@@ -2,6 +2,6 @@ module example.com/authsvc
 
 go 1.23.6
 
-require k8s.io/apimachinery v0.32.1
+require k8s.io/apimachinery v0.32.2
 
 require github.com/google/uuid v1.6.0 // indirect
```
- `images/ext-auth-example-authsvc/rootfs/go.sum` [M]
```diff
diff --git a/images/ext-auth-example-authsvc/rootfs/go.sum b/images/ext-auth-example-authsvc/rootfs/go.sum
index 17a075fd0..770c22f6a 100644
--- a/images/ext-auth-example-authsvc/rootfs/go.sum
+++ b/images/ext-auth-example-authsvc/rootfs/go.sum
@@ -1,4 +1,4 @@
 github.com/google/uuid v1.6.0 h1:NIvaJDMOsjHA8n1jAhLSgzrAzy1Hgr+hNrb57e+94F0=
 github.com/google/uuid v1.6.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
-k8s.io/apimachinery v0.32.1 h1:683ENpaCBjma4CYqsmZyhEzrGz6cjn1MY/X2jB2hkZs=
-k8s.io/apimachinery v0.32.1/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
+k8s.io/apimachinery v0.32.2 h1:yoQBR9ZGkA6Rgmhbp/yuT9/g+4lxtsGYwW6dR6BDPLQ=
+k8s.io/apimachinery v0.32.2/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
```
- `images/kube-webhook-certgen/rootfs/go.mod` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.mod b/images/kube-webhook-certgen/rootfs/go.mod
index 7836f790f..2b8567748 100644
--- a/images/kube-webhook-certgen/rootfs/go.mod
+++ b/images/kube-webhook-certgen/rootfs/go.mod
@@ -6,10 +6,10 @@ require (
 	github.com/onrik/logrus v0.11.0
 	github.com/sirupsen/logrus v1.9.3
 	github.com/spf13/cobra v1.9.1
-	k8s.io/api v0.32.1
-	k8s.io/apimachinery v0.32.1
-	k8s.io/client-go v0.32.1
-	k8s.io/kube-aggregator v0.32.1
+	k8s.io/api v0.32.2
+	k8s.io/apimachinery v0.32.2
+	k8s.io/client-go v0.32.2
+	k8s.io/kube-aggregator v0.32.2
 )
 
 require (
```
- `images/kube-webhook-certgen/rootfs/go.sum` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.sum b/images/kube-webhook-certgen/rootfs/go.sum
index 77e6a5284..1c660f020 100644
--- a/images/kube-webhook-certgen/rootfs/go.sum
+++ b/images/kube-webhook-certgen/rootfs/go.sum
@@ -141,16 +141,16 @@ gopkg.in/inf.v0 v0.9.1/go.mod h1:cWUDdTG/fYaXco+Dcufb5Vnc6Gp2YChqWtbxRZE0mXw=
 gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
 gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
 gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
-k8s.io/api v0.32.1 h1:f562zw9cy+GvXzXf0CKlVQ7yHJVYzLfL6JAS4kOAaOc=
-k8s.io/api v0.32.1/go.mod h1:/Yi/BqkuueW1BgpoePYBRdDYfjPF5sgTr5+YqDZra5k=
-k8s.io/apimachinery v0.32.1 h1:683ENpaCBjma4CYqsmZyhEzrGz6cjn1MY/X2jB2hkZs=
-k8s.io/apimachinery v0.32.1/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
-k8s.io/client-go v0.32.1 h1:otM0AxdhdBIaQh7l1Q0jQpmo7WOFIk5FFa4bg6YMdUU=
-k8s.io/client-go v0.32.1/go.mod h1:aTTKZY7MdxUaJ/KiUs8D+GssR9zJZi77ZqtzcGXIiDg=
+k8s.io/api v0.32.2 h1:bZrMLEkgizC24G9eViHGOPbW+aRo9duEISRIJKfdJuw=
+k8s.io/api v0.32.2/go.mod h1:hKlhk4x1sJyYnHENsrdCWw31FEmCijNGPJO5WzHiJ6Y=
+k8s.io/apimachinery v0.32.2 h1:yoQBR9ZGkA6Rgmhbp/yuT9/g+4lxtsGYwW6dR6BDPLQ=
+k8s.io/apimachinery v0.32.2/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
+k8s.io/client-go v0.32.2 h1:4dYCD4Nz+9RApM2b/3BtVvBHw54QjMFUl1OLcJG5yOA=
+k8s.io/client-go v0.32.2/go.mod h1:fpZ4oJXclZ3r2nDOv+Ux3XcJutfrwjKTCHz2H3sww94=
... (truncated)
```

### 🔸 Commit `12a09b31c76d8f9b5ff1fd45d707c288aa599354` - Bump github.com/spf13/cobra from 1.8.1 to 1.9.1 (#12868) (2025-02-17) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 867a4ec00..34584bbf9 100644
--- a/go.mod
+++ b/go.mod
@@ -20,7 +20,7 @@ require (
 	github.com/prometheus/client_golang v1.20.5
 	github.com/prometheus/client_model v0.6.1
 	github.com/prometheus/common v0.62.0
-	github.com/spf13/cobra v1.8.1
+	github.com/spf13/cobra v1.9.1
 	github.com/spf13/pflag v1.0.6
 	github.com/stretchr/testify v1.10.0
 	github.com/yudai/gojsondiff v1.0.0
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 3f91c4f00..6e933d349 100644
--- a/go.sum
+++ b/go.sum
@@ -18,7 +18,7 @@ github.com/common-nighthawk/go-figure v0.0.0-20210622060536-734e95fb86be h1:J5BL
 github.com/common-nighthawk/go-figure v0.0.0-20210622060536-734e95fb86be/go.mod h1:mk5IQ+Y0ZeO87b858TlA645sVcEcbiX6YqP98kt+7+w=
 github.com/coreos/go-systemd/v22 v22.5.0 h1:RrqgGjYQKalulkV8NGVIfkXQf6YYmOyiJKk8iXXhfZs=
 github.com/coreos/go-systemd/v22 v22.5.0/go.mod h1:Y58oyj3AT4RCenI/lSvhwexgC+NSVTIJ3seZv2GcEnc=
-github.com/cpuguy83/go-md2man/v2 v2.0.4/go.mod h1:tgQtvFlXSQOSOSIRvRPT7W67SCa46tRHOmNcaadrF8o=
+github.com/cpuguy83/go-md2man/v2 v2.0.6/go.mod h1:oOW0eioCTA6cOiMLiUPZOpcVxMig6NIQQ7OS05n1F4g=
 github.com/creack/pty v1.1.18 h1:n56/Zwd5o6whRC5PMGretI4IdRLlmBXYNjScPaBgsbY=
 github.com/creack/pty v1.1.18/go.mod h1:MOBLtS5ELjhRRrroQr9kyvTxUAFNvYEK993ew/Vr4O4=
 github.com/cyphar/filepath-securejoin v0.4.1 h1:JyxxyPEaktOD+GAnqIqTf9A8tHyAG22rowi7HkoSU1s=
@@ -195,9 +195,8 @@ github.com/sergi/go-diff v1.3.1 h1:xkr+Oxo4BOQKmkn/B9eMK0g5Kg/983T9DqqPHwYqD+8=
 github.com/sergi/go-diff v1.3.1/go.mod h1:aMJSSKb2lpPvRNec0+w3fl7LP9IOFzdc9Pa4NFbPK1I=
 github.com/sirupsen/logrus v1.9.3 h1:dueUQJ1C2q9oE3F7wvmSGAaVtTmUizReu6fjN8uqzbQ=
 github.com/sirupsen/logrus v1.9.3/go.mod h1:naHLuLoDiP4jHNo9R0sCBMtWGeIprob74mVsIT4qYEQ=
-github.com/spf13/cobra v1.8.1 h1:e5/vxKd/rZsfSJMUX1agtjeTDf+qv1/JdBF8gg5k9ZM=
-github.com/spf13/cobra v1.8.1/go.mod h1:wHxEcudfqmLYa8iTfL+OuZPbBZkmvliBWKIezN3kD9Y=
-github.com/spf13/pflag v1.0.5/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
... (truncated)
```

### 🔸 Commit `9dcb389bf19c132bf85bcb1cd703b072e4f01cf5` - Bump the actions group with 4 updates (#12890) (2025-02-24) by `k8s-infra-cherrypick-robot`
- `.github/workflows/chart.yaml` [M]
```diff
diff --git a/.github/workflows/chart.yaml b/.github/workflows/chart.yaml
index 7c37447af..63c2f1524 100644
--- a/.github/workflows/chart.yaml
+++ b/.github/workflows/chart.yaml
@@ -28,7 +28,7 @@ jobs:
           python-version: 3.x
 
       - name: Set up Helm
-        uses: azure/setup-helm@fe7b79cd5ee1e45176fcad797de68ecaf3ca4814 # v4.2.0
+        uses: azure/setup-helm@b9e51907a09c216f16ebe8536097933489208112 # v4.3.0
 
       - name: Set up Helm Chart Testing
         uses: helm/chart-testing-action@0d28d3144d3a25ea2cc349d6e59901c4ff469b3b # v2.7.0
```
- `.github/workflows/ci.yaml` [M]
```diff
diff --git a/.github/workflows/ci.yaml b/.github/workflows/ci.yaml
index 319ef12ce..7b579daf7 100644
--- a/.github/workflows/ci.yaml
+++ b/.github/workflows/ci.yaml
@@ -186,7 +186,7 @@ jobs:
             | gzip > docker.tar.gz
 
       - name: cache
-        uses: actions/upload-artifact@65c4c4a1ddee5b72f698fdd19549f0f0fb45cf08 # v4.6.0
+        uses: actions/upload-artifact@4cec3d8aa04e39d1a68397de0c4cd6fb9dce8ec1 # v4.6.1
         with:
           name: docker.tar.gz
           path: docker.tar.gz
@@ -207,7 +207,7 @@ jobs:
           python-version: 3.x
 
       - name: Set up Helm
-        uses: azure/setup-helm@fe7b79cd5ee1e45176fcad797de68ecaf3ca4814 # v4.2.0
+        uses: azure/setup-helm@b9e51907a09c216f16ebe8536097933489208112 # v4.3.0
 
... (truncated)
```
- `.github/workflows/scorecards.yml` [M]
```diff
diff --git a/.github/workflows/scorecards.yml b/.github/workflows/scorecards.yml
index a4473710d..08831c91e 100644
--- a/.github/workflows/scorecards.yml
+++ b/.github/workflows/scorecards.yml
@@ -32,7 +32,7 @@ jobs:
           persist-credentials: false
 
       - name: "Run analysis"
-        uses: ossf/scorecard-action@62b2cac7ed8198b15735ed49ab1e5cf35480ba46 # v2.4.0
+        uses: ossf/scorecard-action@f49aabe0b5af0936a0987cfb85d86b75731b0186 # v2.4.1
         with:
           results_file: results.sarif
           results_format: sarif
@@ -51,7 +51,7 @@ jobs:
       # Upload the results as artifacts (optional). Commenting out will disable uploads of run results in SARIF
       # format to the repository Actions tab.
       - name: "Upload artifact"
-        uses: actions/upload-artifact@65c4c4a1ddee5b72f698fdd19549f0f0fb45cf08 # v4.6.0
+        uses: actions/upload-artifact@4cec3d8aa04e39d1a68397de0c4cd6fb9dce8ec1 # v4.6.1
         with:
... (truncated)
```
- `.github/workflows/vulnerability-scans.yaml` [M]
```diff
diff --git a/.github/workflows/vulnerability-scans.yaml b/.github/workflows/vulnerability-scans.yaml
index 4461d9757..385006e25 100644
--- a/.github/workflows/vulnerability-scans.yaml
+++ b/.github/workflows/vulnerability-scans.yaml
@@ -75,7 +75,7 @@ jobs:
 
       # This step checks out a copy of your repository.
       - name: Upload SARIF file
-        uses: github/codeql-action/upload-sarif@9e8d0789d4a0fa9ceb6b1738f7e269594bdd67f0 # v3.28.9
+        uses: github/codeql-action/upload-sarif@b56ba49b26e50535fa1e7f7db0f4f7b4bf65d80d # v3.28.10
         with:
           token: ${{ github.token }}
           # Path to SARIF file relative to the root of the repository
```
- `.github/workflows/zz-tmpl-k8s-e2e.yaml` [M]
```diff
diff --git a/.github/workflows/zz-tmpl-k8s-e2e.yaml b/.github/workflows/zz-tmpl-k8s-e2e.yaml
index b245886ae..a1918b43f 100644
--- a/.github/workflows/zz-tmpl-k8s-e2e.yaml
+++ b/.github/workflows/zz-tmpl-k8s-e2e.yaml
@@ -50,7 +50,7 @@ jobs:
           make kind-e2e-test
 
       - name: Upload e2e junit-reports ${{ inputs.variation }}
-        uses: actions/upload-artifact@65c4c4a1ddee5b72f698fdd19549f0f0fb45cf08 # v4.6.0
+        uses: actions/upload-artifact@4cec3d8aa04e39d1a68397de0c4cd6fb9dce8ec1 # v4.6.1
         if: success() || failure()
         with:
           name: e2e-test-reports-${{ inputs.k8s-version }}${{ inputs.variation }}
```

### 🔸 Commit `c53f60fc847710c3f4b2679d9e3ba9328c239f45` - Bump github.com/prometheus/client_golang from 1.20.5 to 1.21.0 in /images/custom-error-pages/rootfs (#12891) (2025-02-24) by `k8s-infra-cherrypick-robot`
- `images/custom-error-pages/rootfs/go.mod` [M]
```diff
diff --git a/images/custom-error-pages/rootfs/go.mod b/images/custom-error-pages/rootfs/go.mod
index 5c0377284..3cc6f9ca3 100644
--- a/images/custom-error-pages/rootfs/go.mod
+++ b/images/custom-error-pages/rootfs/go.mod
@@ -2,16 +2,16 @@ module k8s.io/ingress-nginx/custom-error-pages
 
 go 1.23.6
 
-require github.com/prometheus/client_golang v1.20.5
+require github.com/prometheus/client_golang v1.21.0
 
 require (
 	github.com/beorn7/perks v1.0.1 // indirect
 	github.com/cespare/xxhash/v2 v2.3.0 // indirect
-	github.com/klauspost/compress v1.17.9 // indirect
+	github.com/klauspost/compress v1.17.11 // indirect
 	github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 // indirect
 	github.com/prometheus/client_model v0.6.1 // indirect
-	github.com/prometheus/common v0.55.0 // indirect
+	github.com/prometheus/common v0.62.0 // indirect
... (truncated)
```
- `images/custom-error-pages/rootfs/go.sum` [M]
```diff
diff --git a/images/custom-error-pages/rootfs/go.sum b/images/custom-error-pages/rootfs/go.sum
index d5318cf86..f3593ed86 100644
--- a/images/custom-error-pages/rootfs/go.sum
+++ b/images/custom-error-pages/rootfs/go.sum
@@ -2,23 +2,31 @@ github.com/beorn7/perks v1.0.1 h1:VlbKKnNfV8bJzeqoa4cOKqO6bYr3WgKZxO8Z16+hsOM=
 github.com/beorn7/perks v1.0.1/go.mod h1:G2ZrVWU2WbWT9wwq4/hrbKbnv/1ERSJQ0ibhJ6rlkpw=
 github.com/cespare/xxhash/v2 v2.3.0 h1:UL815xU9SqsFlibzuggzjXhog7bL6oX9BbNZnL2UFvs=
 github.com/cespare/xxhash/v2 v2.3.0/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
+github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
+github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
 github.com/google/go-cmp v0.6.0 h1:ofyhxvXcZhMsU5ulbFiLKl/XBFqE1GSq7atu8tAmTRI=
 github.com/google/go-cmp v0.6.0/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
-github.com/klauspost/compress v1.17.9 h1:6KIumPrER1LHsvBVuDa0r5xaG0Es51mhhB9BQB2qeMA=
-github.com/klauspost/compress v1.17.9/go.mod h1:Di0epgTjJY877eYKx5yC51cX2A2Vl2ibi7bDH9ttBbw=
+github.com/klauspost/compress v1.17.11 h1:In6xLpyWOi1+C7tXUUWv2ot1QvBjxevKAaI6IXrJmUc=
+github.com/klauspost/compress v1.17.11/go.mod h1:pMDklpSncoRMuLFrf1W9Ss9KT+0rH90U12bZKk7uwG0=
 github.com/kylelemons/godebug v1.1.0 h1:RPNrshWIDI6G2gRW9EHilWtl7Z6Sb1BR0xunSBf0SNc=
 github.com/kylelemons/godebug v1.1.0/go.mod h1:9/0rRGxNHcop5bhtWyNeEfOS8JIWk580+fNqagV/RAw=
 github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 h1:C3w9PqII01/Oq1c1nUAm88MOHcQC9l5mIlSMApZMrHA=
 github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822/go.mod h1:+n7T8mK8HuQTcFwEeznm/DIxMOiR9yIdICNftLE1DvQ=
... (truncated)
```

### 🔸 Commit `378a91eabda9a1714057886254f89f68562c5850` - Bump golang.org/x/crypto from 0.33.0 to 0.34.0 (#12894) (2025-02-24) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 34584bbf9..7d1b36d8f 100644
--- a/go.mod
+++ b/go.mod
@@ -25,7 +25,7 @@ require (
 	github.com/stretchr/testify v1.10.0
 	github.com/yudai/gojsondiff v1.0.0
 	github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30
-	golang.org/x/crypto v0.33.0
+	golang.org/x/crypto v0.34.0
 	google.golang.org/grpc v1.70.0
 	google.golang.org/grpc/examples v0.0.0-20240223204917-5ccf176a08ab
 	gopkg.in/go-playground/pool.v3 v3.1.1
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 6e933d349..0a5ee9d9d 100644
--- a/go.sum
+++ b/go.sum
@@ -243,8 +243,8 @@ go.uber.org/zap v1.27.0/go.mod h1:GB2qFLM7cTU87MWRP2mPIjqfIDnGu+VIO4V/SdhGo2E=
 golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
 golang.org/x/crypto v0.0.0-20191011191535-87dc89f01550/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
 golang.org/x/crypto v0.0.0-20200622213623-75b288015ac9/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
-golang.org/x/crypto v0.33.0 h1:IOBPskki6Lysi0lo9qQvbxiQ+FvsCC/YWOecCHAixus=
-golang.org/x/crypto v0.33.0/go.mod h1:bVdXmD7IV/4GdElGPozy6U7lWdRXA4qyRVGJV57uQ5M=
+golang.org/x/crypto v0.34.0 h1:+/C6tk6rf/+t5DhUketUbD1aNGqiSX3j15Z6xuIDlBA=
+golang.org/x/crypto v0.34.0/go.mod h1:dy7dXNW32cAb/6/PRuTNsix8T+vJAqvuIy5Bli/x0YQ=
 golang.org/x/mod v0.2.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
 golang.org/x/mod v0.3.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
 golang.org/x/mod v0.22.0 h1:D4nJWe9zXqHOmWqj4VMOJhvzj7bEZg4wEYa759z1pH4=
```

### 🔸 Commit `4ed05e40f677c691e01448766ffe2829e5ca00c5` - Config: Remove notes about future defaults. (#12899) (2025-02-24) by `k8s-infra-cherrypick-robot`
- `internal/ingress/controller/config/config.go` [M]
```diff
diff --git a/internal/ingress/controller/config/config.go b/internal/ingress/controller/config/config.go
index bc0ba9d00..2c4c87f3c 100644
--- a/internal/ingress/controller/config/config.go
+++ b/internal/ingress/controller/config/config.go
@@ -97,12 +97,10 @@ type Configuration struct {
 	// AllowCrossNamespaceResources enables users to consume cross namespace resource on annotations
 	// Case disabled, attempts to use secrets or configmaps from a namespace different from Ingress will
 	// be denied
-	// This value will default to `false` on future releases
 	AllowCrossNamespaceResources bool `json:"allow-cross-namespace-resources"`
 
 	// AnnotationsRiskLevel represents the risk accepted on an annotation. If the risk is, for instance `Medium`, annotations
 	// with risk High and Critical will not be accepted.
-	// Default Risk is Critical by default, but this may be changed in future releases
 	AnnotationsRiskLevel string `json:"annotations-risk-level"`
 
 	// AnnotationValueWordBlocklist defines words that should not be part of an user annotation value
```
- `internal/ingress/defaults/main.go` [M]
```diff
diff --git a/internal/ingress/defaults/main.go b/internal/ingress/defaults/main.go
index cfad388ef..e892bf572 100644
--- a/internal/ingress/defaults/main.go
+++ b/internal/ingress/defaults/main.go
@@ -185,7 +185,6 @@ type SecurityConfiguration struct {
 	// AllowCrossNamespaceResources enables users to consume cross namespace resource on annotations
 	// Case disabled, attempts to use secrets or configmaps from a namespace different from Ingress will
 	// be denied
-	// This valid will default to `false` on future releases
 	AllowCrossNamespaceResources bool `json:"allow-cross-namespace-resources"`
 
 	// AnnotationsRiskLevel represents the risk accepted on an annotation. If the risk is, for instance `Medium`, annotations
```

### 🔸 Commit `8c2f46f2d2db2596d53b05a3634ef1d6ad4cece8` - Bump github.com/prometheus/client_golang from 1.20.5 to 1.21.0 (#12901) (2025-02-24) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 7d1b36d8f..6dc3fb006 100644
--- a/go.mod
+++ b/go.mod
@@ -17,7 +17,7 @@ require (
 	github.com/onsi/ginkgo/v2 v2.22.2
 	github.com/opencontainers/runc v1.2.5
 	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2
-	github.com/prometheus/client_golang v1.20.5
+	github.com/prometheus/client_golang v1.21.0
 	github.com/prometheus/client_model v0.6.1
 	github.com/prometheus/common v0.62.0
 	github.com/spf13/cobra v1.9.1
@@ -47,7 +47,7 @@ require (
 require (
 	github.com/common-nighthawk/go-figure v0.0.0-20210622060536-734e95fb86be // indirect
 	github.com/fxamacker/cbor/v2 v2.7.0 // indirect
-	github.com/klauspost/compress v1.17.9 // indirect
+	github.com/klauspost/compress v1.17.11 // indirect
 	github.com/moby/sys/userns v0.1.0 // indirect
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 0a5ee9d9d..507a61b40 100644
--- a/go.sum
+++ b/go.sum
@@ -107,8 +107,8 @@ github.com/json-iterator/go v1.1.12 h1:PV8peI4a0ysnczrg+LtxykD8LfKY9ML6u2jnxaEnr
 github.com/json-iterator/go v1.1.12/go.mod h1:e30LSqwooZae/UwlEbR2852Gd8hjQvJoHmT4TnhNGBo=
 github.com/kisielk/errcheck v1.5.0/go.mod h1:pFxgyoBC7bSaBwPgfKdkLd5X25qrDl4LWUI2bnpBCr8=
 github.com/kisielk/gotool v1.0.0/go.mod h1:XhKaO+MFFWcvkIS/tQcRk01m1F5IRFswLeQ+oQHNcck=
-github.com/klauspost/compress v1.17.9 h1:6KIumPrER1LHsvBVuDa0r5xaG0Es51mhhB9BQB2qeMA=
-github.com/klauspost/compress v1.17.9/go.mod h1:Di0epgTjJY877eYKx5yC51cX2A2Vl2ibi7bDH9ttBbw=
+github.com/klauspost/compress v1.17.11 h1:In6xLpyWOi1+C7tXUUWv2ot1QvBjxevKAaI6IXrJmUc=
+github.com/klauspost/compress v1.17.11/go.mod h1:pMDklpSncoRMuLFrf1W9Ss9KT+0rH90U12bZKk7uwG0=
 github.com/kr/pretty v0.1.0/go.mod h1:dAy3ld7l9f0ibDNOQOHHMYYIIbhfbHSm3C4ZsoJORNo=
 github.com/kr/pretty v0.3.1 h1:flRD4NNwYAUpkphVc1HcthR4KEIFJ65n8Mw5qdRn3LE=
 github.com/kr/pretty v0.3.1/go.mod h1:hoEshYVHaxMs3cyo3Yncou5ZscifuDolrwPKZanG3xk=
@@ -180,8 +180,8 @@ github.com/pkg/errors v0.9.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINE
 github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
 github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2 h1:Jamvg5psRIccs7FGNTlIRMkT8wgtp5eCXdBlqhYGL6U=
 github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
-github.com/prometheus/client_golang v1.20.5 h1:cxppBPuYhUnsO6yo/aoRol4L7q7UFfdm+bR9r+8l63Y=
... (truncated)
```

### 🔸 Commit `662a0776b71bea3dab1f528111139095129743d9` - Development: Update KIND images. (#12910) (2025-02-28) by `k8s-infra-cherrypick-robot`
- `build/dev-env.sh` [M]
```diff
diff --git a/build/dev-env.sh b/build/dev-env.sh
index dd1518ee0..e83369f6c 100755
--- a/build/dev-env.sh
+++ b/build/dev-env.sh
@@ -64,7 +64,7 @@ echo "[dev-env] building image"
 make build image
 docker tag "${REGISTRY}/controller:${TAG}" "${DEV_IMAGE}"
 
-export K8S_VERSION=${K8S_VERSION:-v1.32.0@sha256:c48c62eac5da28cdadcf560d1d8616cfa6783b58f0d94cf63ad1bf49600cb027}
+export K8S_VERSION=${K8S_VERSION:-v1.32.2@sha256:f226345927d7e348497136874b6d207e0b32cc52154ad8323129352923a3142f}
 
 KIND_CLUSTER_NAME="ingress-nginx-dev"
```
- `test/e2e/run-chart-test.sh` [M]
```diff
diff --git a/test/e2e/run-chart-test.sh b/test/e2e/run-chart-test.sh
index b998600d0..ab642c1ae 100755
--- a/test/e2e/run-chart-test.sh
+++ b/test/e2e/run-chart-test.sh
@@ -62,7 +62,7 @@ export KUBECONFIG="${KUBECONFIG:-$HOME/.kube/kind-config-$KIND_CLUSTER_NAME}"
 if [ "${SKIP_CLUSTER_CREATION:-false}" = "false" ]; then
   echo "[dev-env] creating Kubernetes cluster with kind"
 
-  export K8S_VERSION=${K8S_VERSION:-v1.32.0@sha256:c48c62eac5da28cdadcf560d1d8616cfa6783b58f0d94cf63ad1bf49600cb027}
+  export K8S_VERSION=${K8S_VERSION:-v1.32.2@sha256:f226345927d7e348497136874b6d207e0b32cc52154ad8323129352923a3142f}
 
   kind create cluster \
     --verbosity=${KIND_LOG_LEVEL} \
```
- `test/e2e/run-kind-e2e.sh` [M]
```diff
diff --git a/test/e2e/run-kind-e2e.sh b/test/e2e/run-kind-e2e.sh
index 0fcdc61ca..c92ae2d73 100755
--- a/test/e2e/run-kind-e2e.sh
+++ b/test/e2e/run-kind-e2e.sh
@@ -64,7 +64,7 @@ echo "Running e2e with nginx base image ${NGINX_BASE_IMAGE}"
 if [ "${SKIP_CLUSTER_CREATION}" = "false" ]; then
   echo "[dev-env] creating Kubernetes cluster with kind"
 
-  export K8S_VERSION=${K8S_VERSION:-v1.32.0@sha256:c48c62eac5da28cdadcf560d1d8616cfa6783b58f0d94cf63ad1bf49600cb027}
+  export K8S_VERSION=${K8S_VERSION:-v1.32.2@sha256:f226345927d7e348497136874b6d207e0b32cc52154ad8323129352923a3142f}
 
   # delete the cluster if it exists
   if kind get clusters | grep "${KIND_CLUSTER_NAME}"; then
```

### 🔸 Commit `e84dac05f4e195d9aa528a6547934c4335ada394` - NGINX: Update ModSecurity. (#12916) (2025-03-01) by `k8s-infra-cherrypick-robot`
- `images/nginx/rootfs/build.sh` [M]
```diff
diff --git a/images/nginx/rootfs/build.sh b/images/nginx/rootfs/build.sh
index 1d530e640..9d87a0a45 100755
--- a/images/nginx/rootfs/build.sh
+++ b/images/nginx/rootfs/build.sh
@@ -38,8 +38,8 @@ export NGINX_SUBSTITUTIONS=e12e965ac1837ca709709f9a26f572a54d83430e
 # Check for recent changes: https://github.com/SpiderLabs/ModSecurity-nginx/compare/v1.0.3...master
 export MODSECURITY_VERSION=v1.0.3
 
-# Check for recent changes: https://github.com/SpiderLabs/ModSecurity/compare/v3.0.13...v3/master
-export MODSECURITY_LIB_VERSION=v3.0.13
+# Check for recent changes: https://github.com/SpiderLabs/ModSecurity/compare/v3.0.14...v3/master
+export MODSECURITY_LIB_VERSION=v3.0.14
 
 # Check for recent changes: https://github.com/coreruleset/coreruleset/compare/v4.10.0...main
 export OWASP_MODSECURITY_CRS_VERSION=v4.10.0
```

### 🔸 Commit `e7d5e2fb47908e401eb83208c28c99010360ab7f` - Bump the actions group with 3 updates (#12922) (2025-03-03) by `k8s-infra-cherrypick-robot`
- `.github/workflows/ci.yaml` [M]
```diff
diff --git a/.github/workflows/ci.yaml b/.github/workflows/ci.yaml
index 7b579daf7..f6fda7bf5 100644
--- a/.github/workflows/ci.yaml
+++ b/.github/workflows/ci.yaml
@@ -143,11 +143,11 @@ jobs:
           check-latest: true
 
       - name: Set up QEMU
-        uses: docker/setup-qemu-action@4574d27a4764455b42196d70a065bc6853246a25 # v3.4.0
+        uses: docker/setup-qemu-action@29109295f81e9208d7d86ff1c6c12d2833863392 # v3.6.0
 
       - name: Set up Docker Buildx
         id: buildx
-        uses: docker/setup-buildx-action@f7ce87c1d6bead3e36075b2ce75da1f6cc28aaca # v3.9.0
+        uses: docker/setup-buildx-action@b5ca514318bd6ebac0fb2aedd5d36ec1b5c232a2 # v3.10.0
         with:
           version: latest
 
@@ -261,7 +261,7 @@ jobs:
         uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
... (truncated)
```
- `.github/workflows/images.yaml` [M]
```diff
diff --git a/.github/workflows/images.yaml b/.github/workflows/images.yaml
index d9b8b34a1..360dd3799 100644
--- a/.github/workflows/images.yaml
+++ b/.github/workflows/images.yaml
@@ -194,10 +194,10 @@ jobs:
       - name: Checkout
         uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
       - name: Set up QEMU
-        uses: docker/setup-qemu-action@4574d27a4764455b42196d70a065bc6853246a25 # v3.4.0
+        uses: docker/setup-qemu-action@29109295f81e9208d7d86ff1c6c12d2833863392 # v3.6.0
       - name: Set up Docker Buildx
         id: buildx
-        uses: docker/setup-buildx-action@f7ce87c1d6bead3e36075b2ce75da1f6cc28aaca # v3.9.0
+        uses: docker/setup-buildx-action@b5ca514318bd6ebac0fb2aedd5d36ec1b5c232a2 # v3.10.0
         with:
           version: latest
           platforms: ${{ env.PLATFORMS }}
```
- `.github/workflows/zz-tmpl-k8s-e2e.yaml` [M]
```diff
diff --git a/.github/workflows/zz-tmpl-k8s-e2e.yaml b/.github/workflows/zz-tmpl-k8s-e2e.yaml
index a1918b43f..ef8da9edf 100644
--- a/.github/workflows/zz-tmpl-k8s-e2e.yaml
+++ b/.github/workflows/zz-tmpl-k8s-e2e.yaml
@@ -23,7 +23,7 @@ jobs:
         uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
 
       - name: cache
-        uses: actions/download-artifact@fa0a91b85d4f404e444e00e005971372dc801d16 # v4.1.8
+        uses: actions/download-artifact@cc203385981b70ca67e1cc392babf9cc229d5806 # v4.1.9
         with:
           name: docker.tar.gz
```

### 🔸 Commit `fd1fecc4397164310c323d35661c7cfd06cc5077` - Bump golang.org/x/crypto from 0.34.0 to 0.35.0 (#12924) (2025-03-03) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 6dc3fb006..81741f2a1 100644
--- a/go.mod
+++ b/go.mod
@@ -25,7 +25,7 @@ require (
 	github.com/stretchr/testify v1.10.0
 	github.com/yudai/gojsondiff v1.0.0
 	github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30
-	golang.org/x/crypto v0.34.0
+	golang.org/x/crypto v0.35.0
 	google.golang.org/grpc v1.70.0
 	google.golang.org/grpc/examples v0.0.0-20240223204917-5ccf176a08ab
 	gopkg.in/go-playground/pool.v3 v3.1.1
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 507a61b40..57fcd6309 100644
--- a/go.sum
+++ b/go.sum
@@ -243,8 +243,8 @@ go.uber.org/zap v1.27.0/go.mod h1:GB2qFLM7cTU87MWRP2mPIjqfIDnGu+VIO4V/SdhGo2E=
 golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
 golang.org/x/crypto v0.0.0-20191011191535-87dc89f01550/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
 golang.org/x/crypto v0.0.0-20200622213623-75b288015ac9/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
-golang.org/x/crypto v0.34.0 h1:+/C6tk6rf/+t5DhUketUbD1aNGqiSX3j15Z6xuIDlBA=
-golang.org/x/crypto v0.34.0/go.mod h1:dy7dXNW32cAb/6/PRuTNsix8T+vJAqvuIy5Bli/x0YQ=
+golang.org/x/crypto v0.35.0 h1:b15kiHdrGCHrP6LvwaQ3c03kgNhhiMgvlhxHQhmg2Xs=
+golang.org/x/crypto v0.35.0/go.mod h1:dy7dXNW32cAb/6/PRuTNsix8T+vJAqvuIy5Bli/x0YQ=
 golang.org/x/mod v0.2.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
 golang.org/x/mod v0.3.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
 golang.org/x/mod v0.22.0 h1:D4nJWe9zXqHOmWqj4VMOJhvzj7bEZg4wEYa759z1pH4=
```

### 🔸 Commit `7acafd6a925a7f48322182e2dfe6cb39a10d5b12` - Test: Remove gRPC Fortune Teller. (#12930) (2025-03-04) by `k8s-infra-cherrypick-robot`
- `images/README.md` [M]
```diff
diff --git a/images/README.md b/images/README.md
index e7e5f71a6..5a845a0dd 100644
--- a/images/README.md
+++ b/images/README.md
@@ -11,13 +11,12 @@
 </table>
 
 
-Directory | Purpose
------------- | -------------
-custom-error-pages | Example of Custom error pages for the Ingress-Nginx Controller
-e2e | Image to run e2e tests
-fastcgi-helloserver | FastCGI application for e2e tests
-grpc-fortune-teller | grpc server application for the nginx-ingress grpc example
-httpbun | A simple HTTP Request & Response Service for e2e tests
-httpbin | [Removed] we are no longer maintaining the httpbin image due to project being unmaintained 
-nginx | NGINX base image using [alpine linux](https://www.alpinelinux.org)
-cfssl | Image to run cfssl commands
+Directory              | Purpose
+---------------------- | ------------------------------------------------------------------
... (truncated)
```
- `test/e2e/annotations/grpc.go` [M]
```diff
diff --git a/test/e2e/annotations/grpc.go b/test/e2e/annotations/grpc.go
index 530d16729..a474ec4a4 100644
--- a/test/e2e/annotations/grpc.go
+++ b/test/e2e/annotations/grpc.go
@@ -45,29 +45,6 @@ const (
 var _ = framework.DescribeAnnotation("backend-protocol - GRPC", func() {
 	f := framework.NewDefaultFramework("grpc", framework.WithHTTPBunEnabled())
 
-	ginkgo.It("should use grpc_pass in the configuration file", func() {
-		f.NewGRPCFortuneTellerDeployment()
-
-		annotations := map[string]string{
-			"nginx.ingress.kubernetes.io/backend-protocol": "GRPC",
-		}
-
-		ing := framework.NewSingleIngress(host, "/", host, f.Namespace, "fortune-teller", 50051, annotations)
-		f.EnsureIngress(ing)
-
-		f.WaitForNginxServer(host,
-			func(server string) bool {
... (truncated)
```
- `test/e2e/framework/grpc_fortune_teller.go` [D]
```diff
diff --git a/test/e2e/framework/grpc_fortune_teller.go b/test/e2e/framework/grpc_fortune_teller.go
deleted file mode 100644
index a7be46327..000000000
--- a/test/e2e/framework/grpc_fortune_teller.go
+++ /dev/null
@@ -1,105 +0,0 @@
-/*
-Copyright 2017 The Kubernetes Authors.
-
-Licensed under the Apache License, Version 2.0 (the "License");
-you may not use this file except in compliance with the License.
-You may obtain a copy of the License at
-
-    http://www.apache.org/licenses/LICENSE-2.0
-
-Unless required by applicable law or agreed to in writing, software
-distributed under the License is distributed on an "AS IS" BASIS,
-WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-See the License for the specific language governing permissions and
-limitations under the License.
... (truncated)
```

### 🔸 Commit `41f41ccacd9971484e76284c517512ab57a412b9` - CI: Update KIND images. (#12932) (2025-03-04) by `Marco Ebert`
- `.github/workflows/ci.yaml` [M]
```diff
diff --git a/.github/workflows/ci.yaml b/.github/workflows/ci.yaml
index f6fda7bf5..581b5adb0 100644
--- a/.github/workflows/ci.yaml
+++ b/.github/workflows/ci.yaml
@@ -254,7 +254,7 @@ jobs:
 
     strategy:
       matrix:
-        k8s: [v1.26.15, v1.27.16, v1.28.15, v1.29.12, v1.30.8]
+        k8s: [v1.26.15, v1.27.16, v1.28.15, v1.29.14, v1.30.10]
 
     steps:
       - name: Checkout code
@@ -285,7 +285,7 @@ jobs:
       (needs.changes.outputs.go == 'true') || (needs.changes.outputs.baseimage == 'true') || ${{ github.event.workflow_dispatch.run_e2e == 'true' }}
     strategy:
       matrix:
-        k8s: [v1.26.15, v1.27.16, v1.28.15, v1.29.12, v1.30.8]
+        k8s: [v1.26.15, v1.27.16, v1.28.15, v1.29.14, v1.30.10]
     uses: ./.github/workflows/zz-tmpl-k8s-e2e.yaml
... (truncated)
```
- `.github/workflows/images.yaml` [M]
```diff
diff --git a/.github/workflows/images.yaml b/.github/workflows/images.yaml
index 360dd3799..e38d2cb17 100644
--- a/.github/workflows/images.yaml
+++ b/.github/workflows/images.yaml
@@ -138,7 +138,7 @@ jobs:
       (needs.changes.outputs.kube-webhook-certgen == 'true')
     strategy:
       matrix:
-        k8s: [v1.26.15, v1.27.16, v1.28.15, v1.29.12, v1.30.8]
+        k8s: [v1.26.15, v1.27.16, v1.28.15, v1.29.14, v1.30.10]
     steps:
     - name: Checkout
       uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
```

### 🔸 Commit `1f53d60fa99cd36081beb788027c54de546c855c` - Bump google.golang.org/grpc from 1.70.0 to 1.71.0 (#12936) (2025-03-05) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 81741f2a1..391d23f7c 100644
--- a/go.mod
+++ b/go.mod
@@ -26,7 +26,7 @@ require (
 	github.com/yudai/gojsondiff v1.0.0
 	github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30
 	golang.org/x/crypto v0.35.0
-	google.golang.org/grpc v1.70.0
+	google.golang.org/grpc v1.71.0
 	google.golang.org/grpc/examples v0.0.0-20240223204917-5ccf176a08ab
 	gopkg.in/go-playground/pool.v3 v3.1.1
 	gopkg.in/mcuadros/go-syslog.v2 v2.3.0
@@ -50,8 +50,8 @@ require (
 	github.com/klauspost/compress v1.17.11 // indirect
 	github.com/moby/sys/userns v0.1.0 // indirect
 	github.com/x448/float16 v0.8.4 // indirect
-	go.opentelemetry.io/otel v1.32.0 // indirect
-	go.opentelemetry.io/otel/trace v1.32.0 // indirect
+	go.opentelemetry.io/otel v1.34.0 // indirect
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 57fcd6309..05876f371 100644
--- a/go.sum
+++ b/go.sum
@@ -224,16 +224,18 @@ github.com/yuin/goldmark v1.1.27/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9de
 github.com/yuin/goldmark v1.2.1/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9decYSb74=
 github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30 h1:rzHvkiukOVYcf840FqAsHqBMhfLofvQIxWtczkGRklU=
 github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30/go.mod h1:/Hzu8ych2oXCs1iNI+MeASyFzWTncQ6nlu/wgqbqC2A=
-go.opentelemetry.io/otel v1.32.0 h1:WnBN+Xjcteh0zdk01SVqV55d/m62NJLJdIyb4y/WO5U=
-go.opentelemetry.io/otel v1.32.0/go.mod h1:00DCVSB0RQcnzlwyTfqtxSm+DRr9hpYrHjNGiBHVQIg=
-go.opentelemetry.io/otel/metric v1.32.0 h1:xV2umtmNcThh2/a/aCP+h64Xx5wsj8qqnkYZktzNa0M=
-go.opentelemetry.io/otel/metric v1.32.0/go.mod h1:jH7CIbbK6SH2V2wE16W05BHCtIDzauciCRLoc/SyMv8=
-go.opentelemetry.io/otel/sdk v1.32.0 h1:RNxepc9vK59A8XsgZQouW8ue8Gkb4jpWtJm9ge5lEG4=
-go.opentelemetry.io/otel/sdk v1.32.0/go.mod h1:LqgegDBjKMmb2GC6/PrTnteJG39I8/vJCAP9LlJXEjU=
-go.opentelemetry.io/otel/sdk/metric v1.32.0 h1:rZvFnvmvawYb0alrYkjraqJq0Z4ZUJAiyYCU9snn1CU=
-go.opentelemetry.io/otel/sdk/metric v1.32.0/go.mod h1:PWeZlq0zt9YkYAp3gjKZ0eicRYvOh1Gd+X99x6GHpCQ=
-go.opentelemetry.io/otel/trace v1.32.0 h1:WIC9mYrXf8TmY/EXuULKc8hR17vE+Hjv2cssQDe03fM=
-go.opentelemetry.io/otel/trace v1.32.0/go.mod h1:+i4rkvCraA+tG6AzwloGaCtkx53Fa+L+V8e9a7YvhT8=
+go.opentelemetry.io/auto/sdk v1.1.0 h1:cH53jehLUN6UFLY71z+NDOiNJqDdPRaXzTel0sJySYA=
+go.opentelemetry.io/auto/sdk v1.1.0/go.mod h1:3wSPjt5PWp2RhlCcmmOial7AvC4DQqZb7a7wCow3W8A=
... (truncated)
```

### 🔸 Commit `19c0e107e274227d8b15fd8ef1d6c69685205155` - Bump the go group across 2 directories with 1 update (#12939) (2025-03-05) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 391d23f7c..cfb63d5c9 100644
--- a/go.mod
+++ b/go.mod
@@ -17,7 +17,7 @@ require (
 	github.com/onsi/ginkgo/v2 v2.22.2
 	github.com/opencontainers/runc v1.2.5
 	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2
-	github.com/prometheus/client_golang v1.21.0
+	github.com/prometheus/client_golang v1.21.1
 	github.com/prometheus/client_model v0.6.1
 	github.com/prometheus/common v0.62.0
 	github.com/spf13/cobra v1.9.1
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 05876f371..02a684703 100644
--- a/go.sum
+++ b/go.sum
@@ -180,8 +180,8 @@ github.com/pkg/errors v0.9.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINE
 github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
 github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2 h1:Jamvg5psRIccs7FGNTlIRMkT8wgtp5eCXdBlqhYGL6U=
 github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
-github.com/prometheus/client_golang v1.21.0 h1:DIsaGmiaBkSangBgMtWdNfxbMNdku5IK6iNhrEqWvdA=
-github.com/prometheus/client_golang v1.21.0/go.mod h1:U9NM32ykUErtVBxdvD3zfi+EuFkkaBvMb09mIfe0Zgg=
+github.com/prometheus/client_golang v1.21.1 h1:DOvXXTqVzvkIewV/CDPFdejpMCGeMcbGCQ8YOmu+Ibk=
+github.com/prometheus/client_golang v1.21.1/go.mod h1:U9NM32ykUErtVBxdvD3zfi+EuFkkaBvMb09mIfe0Zgg=
 github.com/prometheus/client_model v0.6.1 h1:ZKSh/rekM+n3CeS952MLRAdFwIKqeY8b62p8ais2e9E=
 github.com/prometheus/client_model v0.6.1/go.mod h1:OrxVMOVHjw3lKMa8+x6HeMGkHMQyHDk9E3jmP2AmGiY=
 github.com/prometheus/common v0.62.0 h1:xasJaQlnWAeyHdUBeGjXmutelfJHWMRr+Fg4QszZ2Io=
```
- `images/custom-error-pages/rootfs/go.mod` [M]
```diff
diff --git a/images/custom-error-pages/rootfs/go.mod b/images/custom-error-pages/rootfs/go.mod
index 3cc6f9ca3..7e7408948 100644
--- a/images/custom-error-pages/rootfs/go.mod
+++ b/images/custom-error-pages/rootfs/go.mod
@@ -2,7 +2,7 @@ module k8s.io/ingress-nginx/custom-error-pages
 
 go 1.23.6
 
-require github.com/prometheus/client_golang v1.21.0
+require github.com/prometheus/client_golang v1.21.1
 
 require (
 	github.com/beorn7/perks v1.0.1 // indirect
```
- `images/custom-error-pages/rootfs/go.sum` [M]
```diff
diff --git a/images/custom-error-pages/rootfs/go.sum b/images/custom-error-pages/rootfs/go.sum
index f3593ed86..f737a4c66 100644
--- a/images/custom-error-pages/rootfs/go.sum
+++ b/images/custom-error-pages/rootfs/go.sum
@@ -14,8 +14,8 @@ github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 h1:C3w9PqII01/Oq
 github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822/go.mod h1:+n7T8mK8HuQTcFwEeznm/DIxMOiR9yIdICNftLE1DvQ=
 github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
 github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
-github.com/prometheus/client_golang v1.21.0 h1:DIsaGmiaBkSangBgMtWdNfxbMNdku5IK6iNhrEqWvdA=
-github.com/prometheus/client_golang v1.21.0/go.mod h1:U9NM32ykUErtVBxdvD3zfi+EuFkkaBvMb09mIfe0Zgg=
+github.com/prometheus/client_golang v1.21.1 h1:DOvXXTqVzvkIewV/CDPFdejpMCGeMcbGCQ8YOmu+Ibk=
+github.com/prometheus/client_golang v1.21.1/go.mod h1:U9NM32ykUErtVBxdvD3zfi+EuFkkaBvMb09mIfe0Zgg=
 github.com/prometheus/client_model v0.6.1 h1:ZKSh/rekM+n3CeS952MLRAdFwIKqeY8b62p8ais2e9E=
 github.com/prometheus/client_model v0.6.1/go.mod h1:OrxVMOVHjw3lKMa8+x6HeMGkHMQyHDk9E3jmP2AmGiY=
 github.com/prometheus/common v0.62.0 h1:xasJaQlnWAeyHdUBeGjXmutelfJHWMRr+Fg4QszZ2Io=
```

### 🔸 Commit `1301ba7248dbe38a7b004321a02455d3b4f03500` - Go: Bump to v1.24.1. (#12943) (2025-03-05) by `k8s-infra-cherrypick-robot`
- `.github/workflows/golangci-lint.yml` [M]
```diff
diff --git a/.github/workflows/golangci-lint.yml b/.github/workflows/golangci-lint.yml
index f57878084..6b66a9afa 100644
--- a/.github/workflows/golangci-lint.yml
+++ b/.github/workflows/golangci-lint.yml
@@ -30,5 +30,4 @@ jobs:
       - name: golangci-lint
         uses: golangci/golangci-lint-action@2226d7cb06a077cd73e56eedd38eecad18e5d837 # v6.5.0
         with:
-          version: v1.62
           only-new-issues: true
```
- `GOLANG_VERSION` [M]
```diff
diff --git a/GOLANG_VERSION b/GOLANG_VERSION
index d8c40e539..f9e8384bb 100644
--- a/GOLANG_VERSION
+++ b/GOLANG_VERSION
@@ -1 +1 @@
-1.23.6
+1.24.1
```
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index cfb63d5c9..52d7c8654 100644
--- a/go.mod
+++ b/go.mod
@@ -1,6 +1,6 @@
 module k8s.io/ingress-nginx
 
-go 1.23.6
+go 1.24.1
 
 require (
 	dario.cat/mergo v1.0.1
```
- `images/custom-error-pages/rootfs/go.mod` [M]
```diff
diff --git a/images/custom-error-pages/rootfs/go.mod b/images/custom-error-pages/rootfs/go.mod
index 7e7408948..65612b8d2 100644
--- a/images/custom-error-pages/rootfs/go.mod
+++ b/images/custom-error-pages/rootfs/go.mod
@@ -1,6 +1,6 @@
 module k8s.io/ingress-nginx/custom-error-pages
 
-go 1.23.6
+go 1.24.1
 
 require github.com/prometheus/client_golang v1.21.1
```
- `images/ext-auth-example-authsvc/rootfs/go.mod` [M]
```diff
diff --git a/images/ext-auth-example-authsvc/rootfs/go.mod b/images/ext-auth-example-authsvc/rootfs/go.mod
index 5f33a86ff..57607c938 100644
--- a/images/ext-auth-example-authsvc/rootfs/go.mod
+++ b/images/ext-auth-example-authsvc/rootfs/go.mod
@@ -1,6 +1,6 @@
 module example.com/authsvc
 
-go 1.23.6
+go 1.24.1
 
 require k8s.io/apimachinery v0.32.2
```
- `images/kube-webhook-certgen/rootfs/go.mod` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.mod b/images/kube-webhook-certgen/rootfs/go.mod
index 2b8567748..662a01732 100644
--- a/images/kube-webhook-certgen/rootfs/go.mod
+++ b/images/kube-webhook-certgen/rootfs/go.mod
@@ -1,6 +1,6 @@
 module github.com/jet/kube-webhook-certgen
 
-go 1.23.6
+go 1.24.1
 
 require (
 	github.com/onrik/logrus v0.11.0
```
- `internal/ingress/annotations/mirror/main_test.go` [M]
```diff
diff --git a/internal/ingress/annotations/mirror/main_test.go b/internal/ingress/annotations/mirror/main_test.go
index 805f1ef6d..9dc1e6e7c 100644
--- a/internal/ingress/annotations/mirror/main_test.go
+++ b/internal/ingress/annotations/mirror/main_test.go
@@ -117,7 +117,7 @@ func TestParse(t *testing.T) {
 		ing.SetAnnotations(testCase.annotations)
 		result, err := ap.Parse(ing)
 		if err != nil {
-			t.Errorf(err.Error())
+			t.Error(err)
 		}
 		if !reflect.DeepEqual(result, testCase.expected) {
 			t.Errorf("expected %+v but returned %+v, annotations: %s", testCase.expected, result, testCase.annotations)
```
- `internal/ingress/metric/collectors/nginx_status_test.go` [M]
```diff
diff --git a/internal/ingress/metric/collectors/nginx_status_test.go b/internal/ingress/metric/collectors/nginx_status_test.go
index ec535745d..aef72dcca 100644
--- a/internal/ingress/metric/collectors/nginx_status_test.go
+++ b/internal/ingress/metric/collectors/nginx_status_test.go
@@ -110,7 +110,7 @@ func TestStatusCollector(t *testing.T) {
 					w.WriteHeader(http.StatusOK)
 
 					if r.URL.Path == "/nginx_status" {
-						_, err := fmt.Fprintf(w, c.mock)
+						_, err := fmt.Fprint(w, c.mock)
 						if err != nil {
 							t.Fatal(err)
 						}
```
- `magefiles/go.mod` [M]
```diff
diff --git a/magefiles/go.mod b/magefiles/go.mod
index f11ab740e..fb16884a8 100644
--- a/magefiles/go.mod
+++ b/magefiles/go.mod
@@ -1,6 +1,6 @@
 module k8s.io/ingress-nginx/magefiles
 
-go 1.23.6
+go 1.24.1
 
 require (
 	github.com/blang/semver/v4 v4.0.0
```

### 🔸 Commit `c6c5b48b6b32ab6e797468852d539fed56c1d02c` - fix DNS issues with unresolvable backends with ExternalName (#12952) (2025-03-06) by `k8s-infra-cherrypick-robot`
- `rootfs/etc/nginx/lua/balancer.lua` [M]
```diff
diff --git a/rootfs/etc/nginx/lua/balancer.lua b/rootfs/etc/nginx/lua/balancer.lua
index 00104c89d..e6ddc1907 100644
--- a/rootfs/etc/nginx/lua/balancer.lua
+++ b/rootfs/etc/nginx/lua/balancer.lua
@@ -77,8 +77,10 @@ local function resolve_external_names(original_backend)
   local endpoints = {}
   for _, endpoint in ipairs(backend.endpoints) do
     local ips = dns_lookup(endpoint.address)
-    for _, ip in ipairs(ips) do
-      table.insert(endpoints, { address = ip, port = endpoint.port })
+    if #ips ~= 1 or ips[1] ~= endpoint.address then
+      for _, ip in ipairs(ips) do
+        table.insert(endpoints, { address = ip, port = endpoint.port })
+      end
     end
   end
   backend.endpoints = endpoints
@@ -104,15 +106,19 @@ local function is_backend_with_external_name(backend)
 end
 
... (truncated)
```

### 🔸 Commit `6b6579c595bdefbd740ccd98841f7dc4847903c2` - Bump golang.org/x/crypto from 0.35.0 to 0.36.0 (#12956) (2025-03-06) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 52d7c8654..14fb82444 100644
--- a/go.mod
+++ b/go.mod
@@ -25,7 +25,7 @@ require (
 	github.com/stretchr/testify v1.10.0
 	github.com/yudai/gojsondiff v1.0.0
 	github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30
-	golang.org/x/crypto v0.35.0
+	golang.org/x/crypto v0.36.0
 	google.golang.org/grpc v1.71.0
 	google.golang.org/grpc/examples v0.0.0-20240223204917-5ccf176a08ab
 	gopkg.in/go-playground/pool.v3 v3.1.1
@@ -115,10 +115,10 @@ require (
 	golang.org/x/mod v0.22.0 // indirect
 	golang.org/x/net v0.34.0 // indirect
 	golang.org/x/oauth2 v0.25.0 // indirect
-	golang.org/x/sync v0.11.0 // indirect
-	golang.org/x/sys v0.30.0 // indirect
-	golang.org/x/term v0.29.0 // indirect
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 02a684703..3b602b946 100644
--- a/go.sum
+++ b/go.sum
@@ -245,8 +245,8 @@ go.uber.org/zap v1.27.0/go.mod h1:GB2qFLM7cTU87MWRP2mPIjqfIDnGu+VIO4V/SdhGo2E=
 golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
 golang.org/x/crypto v0.0.0-20191011191535-87dc89f01550/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
 golang.org/x/crypto v0.0.0-20200622213623-75b288015ac9/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
-golang.org/x/crypto v0.35.0 h1:b15kiHdrGCHrP6LvwaQ3c03kgNhhiMgvlhxHQhmg2Xs=
-golang.org/x/crypto v0.35.0/go.mod h1:dy7dXNW32cAb/6/PRuTNsix8T+vJAqvuIy5Bli/x0YQ=
+golang.org/x/crypto v0.36.0 h1:AnAEvhDddvBdpY+uR+MyHmuZzzNqXSe/GvuDeob5L34=
+golang.org/x/crypto v0.36.0/go.mod h1:Y4J0ReaxCR1IMaabaSMugxJES1EpwhBHhv2bDHklZvc=
 golang.org/x/mod v0.2.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
 golang.org/x/mod v0.3.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
 golang.org/x/mod v0.22.0 h1:D4nJWe9zXqHOmWqj4VMOJhvzj7bEZg4wEYa759z1pH4=
@@ -265,8 +265,8 @@ golang.org/x/sync v0.0.0-20180314180146-1d60e4601c6f/go.mod h1:RxMgew5VJxzue5/jJ
 golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
 golang.org/x/sync v0.0.0-20190911185100-cd5d95a43a6e/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
 golang.org/x/sync v0.0.0-20201020160332-67f06af15bc9/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
-golang.org/x/sync v0.11.0 h1:GGz8+XQP4FvTTrjZPzNKTMFtSXH80RAzG+5ghFPgK9w=
... (truncated)
```

### 🔸 Commit `14946c4cad28937686d44ecae12535e23024b706` - Docs: Update link to `values.yaml`. (#12961) (2025-03-09) by `k8s-infra-cherrypick-robot`
- `docs/examples/customization/jwt/README.md` [M]
```diff
diff --git a/docs/examples/customization/jwt/README.md b/docs/examples/customization/jwt/README.md
index a751ccb7b..1fd1ee00f 100644
--- a/docs/examples/customization/jwt/README.md
+++ b/docs/examples/customization/jwt/README.md
@@ -22,7 +22,7 @@ In nginx, we want to modify the property `proxy-buffer-size`. The size is arbitr
 that a high value can lower the performance of your ingress proxy. In general a value of 16k should get you covered.
 
 ### Using helm
-If you're using helm you can simply use the [`config` properties](https://github.com/kubernetes/ingress-nginx/blob/main/charts/ingress-nginx/values.yaml#L37).
+If you're using helm you can simply use the [`config` properties](https://github.com/kubernetes/ingress-nginx/blob/main/charts/ingress-nginx/values.yaml#L56).
 ```yaml
  # -- Will add custom configuration options to Nginx https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/
   config: 
@@ -45,4 +45,4 @@ data:
 ```
 
 References:
- * [Custom Configuration](../custom-configuration/)
\ No newline at end of file
+ * [Custom Configuration](../custom-configuration/)
```

### 🔸 Commit `9ce48ce63495fa3e0f276753f2fe3b336165297c` - Bump github.com/onsi/ginkgo/v2 from 2.22.2 to 2.23.0 (#12959) (2025-03-09) by `k8s-infra-cherrypick-robot`
- `build/run-in-docker.sh` [M]
```diff
diff --git a/build/run-in-docker.sh b/build/run-in-docker.sh
index b5e683f3d..1b2e6e663 100755
--- a/build/run-in-docker.sh
+++ b/build/run-in-docker.sh
@@ -79,7 +79,7 @@ if [[ "$DOCKER_IN_DOCKER_ENABLED" == "true" ]]; then
   echo "..reached DIND check TRUE block, inside run-in-docker.sh"
   echo "FLAGS=$FLAGS"
   #go env
-  go install -mod=mod github.com/onsi/ginkgo/v2/ginkgo@v2.22.2
+  go install -mod=mod github.com/onsi/ginkgo/v2/ginkgo@v2.23.0
   find / -type f -name ginkgo 2>/dev/null
   which ginkgo
   /bin/bash -c "${FLAGS}"
```
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 14fb82444..3d2883449 100644
--- a/go.mod
+++ b/go.mod
@@ -14,7 +14,7 @@ require (
 	github.com/mitchellh/mapstructure v1.5.0
 	github.com/moul/pb v0.0.0-20220425114252-bca18df4138c
 	github.com/ncabatoff/process-exporter v0.8.5
-	github.com/onsi/ginkgo/v2 v2.22.2
+	github.com/onsi/ginkgo/v2 v2.23.0
 	github.com/opencontainers/runc v1.2.5
 	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2
 	github.com/prometheus/client_golang v1.21.1
@@ -112,15 +112,15 @@ require (
 	github.com/xlab/treeprint v1.2.0 // indirect
 	github.com/yudai/golcs v0.0.0-20170316035057-ecda9a501e82 // indirect
 	github.com/yudai/pp v2.0.1+incompatible // indirect
-	golang.org/x/mod v0.22.0 // indirect
-	golang.org/x/net v0.34.0 // indirect
+	golang.org/x/mod v0.23.0 // indirect
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 3b602b946..d5012d22e 100644
--- a/go.sum
+++ b/go.sum
@@ -163,8 +163,8 @@ github.com/onsi/ginkgo v1.6.0/go.mod h1:lLunBs/Ym6LB5Z9jYTR76FiuTmxDTDusOGeTQH+W
 github.com/onsi/ginkgo v1.12.1/go.mod h1:zj2OWP4+oCPe1qIXoGWkgMRwljMUYCdkwsT2108oapk=
 github.com/onsi/ginkgo v1.16.5 h1:8xi0RTUf59SOSfEtZMvwTvXYMzG4gV23XVHOZiXNtnE=
 github.com/onsi/ginkgo v1.16.5/go.mod h1:+E8gABHa3K6zRBolWtd+ROzc/U5bkGt0FwiG042wbpU=
-github.com/onsi/ginkgo/v2 v2.22.2 h1:/3X8Panh8/WwhU/3Ssa6rCKqPLuAkVY2I0RoyDLySlU=
-github.com/onsi/ginkgo/v2 v2.22.2/go.mod h1:oeMosUL+8LtarXBHu/c0bx2D/K9zyQ6uX3cTyztHwsk=
+github.com/onsi/ginkgo/v2 v2.23.0 h1:FA1xjp8ieYDzlgS5ABTpdUDB7wtngggONc8a7ku2NqQ=
+github.com/onsi/ginkgo/v2 v2.23.0/go.mod h1:zXTP6xIp3U8aVuXN8ENK9IXRaTjFnpVB9mGmaSRvxnM=
 github.com/onsi/gomega v1.7.1/go.mod h1:XdKZgCCFLUoM/7CFJVPcG8C1xQ1AJ0vpAezJrB7JYyY=
 github.com/onsi/gomega v1.10.1/go.mod h1:iN09h71vgCQne3DLsj+A5owkum+a2tYe+TOCB1ybHNo=
 github.com/onsi/gomega v1.36.2 h1:koNYke6TVk6ZmnyHrCXba/T/MoLBXFjeC1PtvYgw0A8=
@@ -249,16 +249,16 @@ golang.org/x/crypto v0.36.0 h1:AnAEvhDddvBdpY+uR+MyHmuZzzNqXSe/GvuDeob5L34=
 golang.org/x/crypto v0.36.0/go.mod h1:Y4J0ReaxCR1IMaabaSMugxJES1EpwhBHhv2bDHklZvc=
 golang.org/x/mod v0.2.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
 golang.org/x/mod v0.3.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
-golang.org/x/mod v0.22.0 h1:D4nJWe9zXqHOmWqj4VMOJhvzj7bEZg4wEYa759z1pH4=
... (truncated)
```
- `images/kube-webhook-certgen/rootfs/go.mod` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.mod b/images/kube-webhook-certgen/rootfs/go.mod
index 662a01732..240682ed6 100644
--- a/images/kube-webhook-certgen/rootfs/go.mod
+++ b/images/kube-webhook-certgen/rootfs/go.mod
@@ -33,16 +33,16 @@ require (
 	github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd // indirect
 	github.com/modern-go/reflect2 v1.0.2 // indirect
 	github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 // indirect
-	github.com/onsi/ginkgo/v2 v2.22.2 // indirect
+	github.com/onsi/ginkgo/v2 v2.23.0 // indirect
 	github.com/onsi/gomega v1.36.2 // indirect
 	github.com/pkg/errors v0.9.1 // indirect
 	github.com/spf13/pflag v1.0.6 // indirect
 	github.com/x448/float16 v0.8.4 // indirect
-	golang.org/x/net v0.33.0 // indirect
+	golang.org/x/net v0.35.0 // indirect
 	golang.org/x/oauth2 v0.23.0 // indirect
-	golang.org/x/sys v0.28.0 // indirect
-	golang.org/x/term v0.27.0 // indirect
-	golang.org/x/text v0.21.0 // indirect
... (truncated)
```
- `images/kube-webhook-certgen/rootfs/go.sum` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.sum b/images/kube-webhook-certgen/rootfs/go.sum
index 1c660f020..1cb89d0ec 100644
--- a/images/kube-webhook-certgen/rootfs/go.sum
+++ b/images/kube-webhook-certgen/rootfs/go.sum
@@ -56,8 +56,8 @@ github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 h1:C3w9PqII01/Oq
 github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822/go.mod h1:+n7T8mK8HuQTcFwEeznm/DIxMOiR9yIdICNftLE1DvQ=
 github.com/onrik/logrus v0.11.0 h1:pu+BCaWL36t0yQaj/2UHK2erf88dwssAKOT51mxPUVs=
 github.com/onrik/logrus v0.11.0/go.mod h1:fO2vlZwIdti6PidD3gV5YKt9Lq5ptpnP293RAe1ITwk=
-github.com/onsi/ginkgo/v2 v2.22.2 h1:/3X8Panh8/WwhU/3Ssa6rCKqPLuAkVY2I0RoyDLySlU=
-github.com/onsi/ginkgo/v2 v2.22.2/go.mod h1:oeMosUL+8LtarXBHu/c0bx2D/K9zyQ6uX3cTyztHwsk=
+github.com/onsi/ginkgo/v2 v2.23.0 h1:FA1xjp8ieYDzlgS5ABTpdUDB7wtngggONc8a7ku2NqQ=
+github.com/onsi/ginkgo/v2 v2.23.0/go.mod h1:zXTP6xIp3U8aVuXN8ENK9IXRaTjFnpVB9mGmaSRvxnM=
 github.com/onsi/gomega v1.36.2 h1:koNYke6TVk6ZmnyHrCXba/T/MoLBXFjeC1PtvYgw0A8=
 github.com/onsi/gomega v1.36.2/go.mod h1:DdwyADRjrc825LhMEkD76cHR5+pUnjhUN8GlHlRPHzY=
 github.com/pkg/errors v0.9.1 h1:FEBLx1zS214owpjy7qsBeixbURkuhQAwrK5UwLGTwt4=
@@ -98,8 +98,8 @@ golang.org/x/net v0.0.0-20190404232315-eb5bcb51f2a3/go.mod h1:t9HGtf8HONx5eT2rtn
 golang.org/x/net v0.0.0-20190620200207-3b0461eec859/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
 golang.org/x/net v0.0.0-20200226121028-0de0cce0169b/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
 golang.org/x/net v0.0.0-20201021035429-f5854403a974/go.mod h1:sp8m0HH+o8qH0wwXwYZr8TS3Oi6o0r6Gce1SSxlDquU=
-golang.org/x/net v0.33.0 h1:74SYHlV8BIgHIFC/LrYkOGIwL19eTYXQ5wc6TBuO36I=
... (truncated)
```
- `images/test-runner/Makefile` [M]
```diff
diff --git a/images/test-runner/Makefile b/images/test-runner/Makefile
index 8adbf0b41..f3987204e 100644
--- a/images/test-runner/Makefile
+++ b/images/test-runner/Makefile
@@ -59,7 +59,7 @@ image:
 		--build-arg YAML_LINT_VERSION=1.33.0 \
 		--build-arg YAMALE_VERSION=4.0.4 \
 		--build-arg HELM_VERSION=3.14.4 \
-		--build-arg GINKGO_VERSION=2.22.2 \
+		--build-arg GINKGO_VERSION=2.23.0 \
 		--build-arg GOLINT_VERSION=latest \
 		-t ${IMAGE}:${TAG} rootfs
 
@@ -80,7 +80,7 @@ build: ensure-buildx
 		--build-arg YAML_LINT_VERSION=1.33.0 \
 		--build-arg YAMALE_VERSION=4.0.4 \
 		--build-arg HELM_VERSION=3.14.4 \
-		--build-arg GINKGO_VERSION=2.22.2 \
+		--build-arg GINKGO_VERSION=2.23.0 \
 		--build-arg GOLINT_VERSION=latest \
... (truncated)
```
- `test/e2e/run-chart-test.sh` [M]
```diff
diff --git a/test/e2e/run-chart-test.sh b/test/e2e/run-chart-test.sh
index ab642c1ae..33e879da8 100755
--- a/test/e2e/run-chart-test.sh
+++ b/test/e2e/run-chart-test.sh
@@ -78,7 +78,7 @@ fi
 
 if [ "${SKIP_IMAGE_CREATION:-false}" = "false" ]; then
   if ! command -v ginkgo &> /dev/null; then
-    go install github.com/onsi/ginkgo/v2/ginkgo@v2.22.2
+    go install github.com/onsi/ginkgo/v2/ginkgo@v2.23.0
   fi
   echo "[dev-env] building image"
   make -C ${DIR}/../../ clean-image build image
```
- `test/e2e/run-kind-e2e.sh` [M]
```diff
diff --git a/test/e2e/run-kind-e2e.sh b/test/e2e/run-kind-e2e.sh
index c92ae2d73..855797d70 100755
--- a/test/e2e/run-kind-e2e.sh
+++ b/test/e2e/run-kind-e2e.sh
@@ -96,7 +96,7 @@ fi
 
 if [ "${SKIP_E2E_IMAGE_CREATION}" = "false" ]; then
   if ! command -v ginkgo &> /dev/null; then
-    go install github.com/onsi/ginkgo/v2/ginkgo@v2.22.2
+    go install github.com/onsi/ginkgo/v2/ginkgo@v2.23.0
   fi
 
   echo "[dev-env] .. done building controller images"
```

### 🔸 Commit `eba5025c47292a5fdf37902d6c30b59c1e9071fb` - Go: Update dependencies. (#12964) (2025-03-09) by `Marco Ebert`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 3d2883449..bf9aa2d4a 100644
--- a/go.mod
+++ b/go.mod
@@ -27,7 +27,7 @@ require (
 	github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30
 	golang.org/x/crypto v0.36.0
 	google.golang.org/grpc v1.71.0
-	google.golang.org/grpc/examples v0.0.0-20240223204917-5ccf176a08ab
+	google.golang.org/grpc/examples v0.0.0-20250306213948-5668c66bc670
 	gopkg.in/go-playground/pool.v3 v3.1.1
 	gopkg.in/mcuadros/go-syslog.v2 v2.3.0
 	k8s.io/api v0.32.2
@@ -40,25 +40,26 @@ require (
 	k8s.io/component-base v0.32.2
 	k8s.io/klog/v2 v2.130.1
 	pault.ag/go/sniff v0.0.0-20200207005214-cf7e4d167732
-	sigs.k8s.io/controller-runtime v0.20.2
+	sigs.k8s.io/controller-runtime v0.20.3
 	sigs.k8s.io/mdtoc v1.4.0
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index d5012d22e..73e8364f4 100644
--- a/go.sum
+++ b/go.sum
@@ -1,9 +1,9 @@
 dario.cat/mergo v1.0.1 h1:Ra4+bf83h2ztPIQYNP99R6m+Y7KfnARDfID+a+vLl4s=
 dario.cat/mergo v1.0.1/go.mod h1:uNxQE+84aUszobStD9th8a29P2fMDhsBdgRYvZOxGmk=
-github.com/Anddd7/pb v0.0.0-20240425032658-369b0f6a404c h1:uhBf0CHXi7nCFZXxHV7l1cBcYFEEVRK4FYxvm1l9lKg=
-github.com/Anddd7/pb v0.0.0-20240425032658-369b0f6a404c/go.mod h1:vYWKbnXd2KAZHUECLPzSE0Er3FgiEmOdPtxwSIRihck=
-github.com/Azure/go-ansiterm v0.0.0-20230124172434-306776ec8161 h1:L/gRVlceqvL25UVaW/CKtUDjefjrs0SPonmDGUVOYP0=
-github.com/Azure/go-ansiterm v0.0.0-20230124172434-306776ec8161/go.mod h1:xomTg63KZ2rFqZQzSB4Vz2SUXa1BpHTVz9L5PTmPC4E=
+github.com/Anddd7/pb v0.0.0-20240516033506-f3934fdc18bd h1:kj2kbbayjD7FrXX5JdnzHGOOi7KbWCdA2X1kefdV3dA=
+github.com/Anddd7/pb v0.0.0-20240516033506-f3934fdc18bd/go.mod h1:vYWKbnXd2KAZHUECLPzSE0Er3FgiEmOdPtxwSIRihck=
+github.com/Azure/go-ansiterm v0.0.0-20250102033503-faa5f7b0171c h1:udKWzYgxTojEKWjV8V+WSxDXJ4NFATAsZjh8iIbsQIg=
+github.com/Azure/go-ansiterm v0.0.0-20250102033503-faa5f7b0171c/go.mod h1:xomTg63KZ2rFqZQzSB4Vz2SUXa1BpHTVz9L5PTmPC4E=
 github.com/BurntSushi/toml v1.3.2 h1:o7IhLm0Msx3BaB+n3Ag7L8EVlByGnpq14C4YWiu/gL8=
 github.com/BurntSushi/toml v1.3.2/go.mod h1:CxXYINrC8qIiEnFrOxCa7Jy5BFHlXnUU2pbicEuybxQ=
 github.com/armon/go-proxyproto v0.1.0 h1:TWWcSsjco7o2itn6r25/5AqKBiWmsiuzsUDLT/MTl7k=
@@ -31,8 +31,8 @@ github.com/eapache/channels v1.1.0 h1:F1taHcn7/F0i8DYqKXJnyhJcVpp2kgFcNePxXtnyu4
 github.com/eapache/channels v1.1.0/go.mod h1:jMm2qB5Ubtg9zLd+inMZd2/NUvXgzmWXsDaLyQIGfH0=
... (truncated)
```
- `images/custom-error-pages/rootfs/go.mod` [M]
```diff
diff --git a/images/custom-error-pages/rootfs/go.mod b/images/custom-error-pages/rootfs/go.mod
index 65612b8d2..7d2c24fbd 100644
--- a/images/custom-error-pages/rootfs/go.mod
+++ b/images/custom-error-pages/rootfs/go.mod
@@ -7,11 +7,11 @@ require github.com/prometheus/client_golang v1.21.1
 require (
 	github.com/beorn7/perks v1.0.1 // indirect
 	github.com/cespare/xxhash/v2 v2.3.0 // indirect
-	github.com/klauspost/compress v1.17.11 // indirect
+	github.com/klauspost/compress v1.18.0 // indirect
 	github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 // indirect
 	github.com/prometheus/client_model v0.6.1 // indirect
 	github.com/prometheus/common v0.62.0 // indirect
 	github.com/prometheus/procfs v0.15.1 // indirect
-	golang.org/x/sys v0.28.0 // indirect
-	google.golang.org/protobuf v1.36.1 // indirect
+	golang.org/x/sys v0.31.0 // indirect
+	google.golang.org/protobuf v1.36.5 // indirect
 )
```
- `images/custom-error-pages/rootfs/go.sum` [M]
```diff
diff --git a/images/custom-error-pages/rootfs/go.sum b/images/custom-error-pages/rootfs/go.sum
index f737a4c66..0d8cec06c 100644
--- a/images/custom-error-pages/rootfs/go.sum
+++ b/images/custom-error-pages/rootfs/go.sum
@@ -6,8 +6,8 @@ github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c
 github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
 github.com/google/go-cmp v0.6.0 h1:ofyhxvXcZhMsU5ulbFiLKl/XBFqE1GSq7atu8tAmTRI=
 github.com/google/go-cmp v0.6.0/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
-github.com/klauspost/compress v1.17.11 h1:In6xLpyWOi1+C7tXUUWv2ot1QvBjxevKAaI6IXrJmUc=
-github.com/klauspost/compress v1.17.11/go.mod h1:pMDklpSncoRMuLFrf1W9Ss9KT+0rH90U12bZKk7uwG0=
+github.com/klauspost/compress v1.18.0 h1:c/Cqfb0r+Yi+JtIEq73FWXVkRonBlf0CRNYc8Zttxdo=
+github.com/klauspost/compress v1.18.0/go.mod h1:2Pp+KzxcywXVXMr50+X0Q/Lsb43OQHYWRCY2AiWywWQ=
 github.com/kylelemons/godebug v1.1.0 h1:RPNrshWIDI6G2gRW9EHilWtl7Z6Sb1BR0xunSBf0SNc=
 github.com/kylelemons/godebug v1.1.0/go.mod h1:9/0rRGxNHcop5bhtWyNeEfOS8JIWk580+fNqagV/RAw=
 github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 h1:C3w9PqII01/Oq1c1nUAm88MOHcQC9l5mIlSMApZMrHA=
@@ -24,9 +24,9 @@ github.com/prometheus/procfs v0.15.1 h1:YagwOFzUgYfKKHX6Dr+sHT7km/hxC76UB0leargg
 github.com/prometheus/procfs v0.15.1/go.mod h1:fB45yRUv8NstnjriLhBQLuOUt+WW4BsoGhij/e3PBqk=
 github.com/stretchr/testify v1.10.0 h1:Xv5erBjTwe/5IxqUQTdXv5kgmIvbHo3QQyRwhJsOfJA=
 github.com/stretchr/testify v1.10.0/go.mod h1:r2ic/lqez/lEtzL7wO/rwa5dbSLXVDPFyf8C91i36aY=
-golang.org/x/sys v0.28.0 h1:Fksou7UEQUWlKvIdsqzJmUmCX3cZuD2+P3XyyzwMhlA=
... (truncated)
```
- `images/kube-webhook-certgen/rootfs/go.mod` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.mod b/images/kube-webhook-certgen/rootfs/go.mod
index 240682ed6..45bbcabfb 100644
--- a/images/kube-webhook-certgen/rootfs/go.mod
+++ b/images/kube-webhook-certgen/rootfs/go.mod
@@ -14,22 +14,22 @@ require (
 
 require (
 	github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc // indirect
-	github.com/emicklei/go-restful/v3 v3.11.3 // indirect
+	github.com/emicklei/go-restful/v3 v3.12.2 // indirect
 	github.com/fxamacker/cbor/v2 v2.7.0 // indirect
 	github.com/go-logr/logr v1.4.2 // indirect
 	github.com/go-openapi/jsonpointer v0.21.0 // indirect
-	github.com/go-openapi/jsonreference v0.20.4 // indirect
+	github.com/go-openapi/jsonreference v0.21.0 // indirect
 	github.com/go-openapi/swag v0.23.0 // indirect
 	github.com/gogo/protobuf v1.3.2 // indirect
 	github.com/golang/protobuf v1.5.4 // indirect
-	github.com/google/gnostic-models v0.6.8 // indirect
-	github.com/google/go-cmp v0.6.0 // indirect
... (truncated)
```
- `images/kube-webhook-certgen/rootfs/go.sum` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.sum b/images/kube-webhook-certgen/rootfs/go.sum
index 1cb89d0ec..f0cd3441e 100644
--- a/images/kube-webhook-certgen/rootfs/go.sum
+++ b/images/kube-webhook-certgen/rootfs/go.sum
@@ -3,16 +3,16 @@ github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSs
 github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
 github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc h1:U9qPSI2PIWSS1VwoXQT9A3Wy9MM3WgvqSxFWenqJduM=
 github.com/davecgh/go-spew v1.1.2-0.20180830191138-d8f796af33cc/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
-github.com/emicklei/go-restful/v3 v3.11.3 h1:yagOQz/38xJmcNeZJtrUcKjkHRltIaIFXKWeG1SkWGE=
-github.com/emicklei/go-restful/v3 v3.11.3/go.mod h1:6n3XBCmQQb25CM2LCACGz8ukIrRry+4bhvbpWn3mrbc=
+github.com/emicklei/go-restful/v3 v3.12.2 h1:DhwDP0vY3k8ZzE0RunuJy8GhNpPL6zqLkDf9B/a0/xU=
+github.com/emicklei/go-restful/v3 v3.12.2/go.mod h1:6n3XBCmQQb25CM2LCACGz8ukIrRry+4bhvbpWn3mrbc=
 github.com/fxamacker/cbor/v2 v2.7.0 h1:iM5WgngdRBanHcxugY4JySA0nk1wZorNOpTgCMedv5E=
 github.com/fxamacker/cbor/v2 v2.7.0/go.mod h1:pxXPTn3joSm21Gbwsv0w9OSA2y1HFR9qXEeXQVeNoDQ=
 github.com/go-logr/logr v1.4.2 h1:6pFjapn8bFcIbiKo3XT4j/BhANplGihG6tvd+8rYgrY=
 github.com/go-logr/logr v1.4.2/go.mod h1:9T104GzyrTigFIr8wt5mBrctHMim0Nb2HLGrmQ40KvY=
 github.com/go-openapi/jsonpointer v0.21.0 h1:YgdVicSA9vH5RiHs9TZW5oyafXZFc6+2Vc1rr/O9oNQ=
 github.com/go-openapi/jsonpointer v0.21.0/go.mod h1:IUyH9l/+uyhIYQ/PXVA41Rexl+kOkAPDdXEYns6fzUY=
-github.com/go-openapi/jsonreference v0.20.4 h1:bKlDxQxQJgwpUSgOENiMPzCTBVuc7vTdXSSgNeAhojU=
-github.com/go-openapi/jsonreference v0.20.4/go.mod h1:5pZJyJP2MnYCpoeoMAql78cCHauHj0V9Lhc506VOpw4=
... (truncated)
```
- `magefiles/go.mod` [M]
```diff
diff --git a/magefiles/go.mod b/magefiles/go.mod
index fb16884a8..3c716cf1a 100644
--- a/magefiles/go.mod
+++ b/magefiles/go.mod
@@ -8,15 +8,15 @@ require (
 	github.com/helm/helm v2.17.0+incompatible
 	github.com/magefile/mage v1.15.0
 	github.com/vmware-labs/yaml-jsonpath v0.3.2
-	golang.org/x/oauth2 v0.18.0
+	golang.org/x/oauth2 v0.28.0
 	gopkg.in/yaml.v3 v3.0.1
 )
 
 require (
-	github.com/BurntSushi/toml v1.3.2 // indirect
+	github.com/BurntSushi/toml v1.4.0 // indirect
 	github.com/Masterminds/semver v1.5.0 // indirect
-	github.com/cyphar/filepath-securejoin v0.2.4 // indirect
-	github.com/dprotaso/go-yit v0.0.0-20191028211022-135eb7262960 // indirect
+	github.com/cyphar/filepath-securejoin v0.4.1 // indirect
... (truncated)
```
- `magefiles/go.sum` [M]
```diff
diff --git a/magefiles/go.sum b/magefiles/go.sum
index 8684d4701..bc5a804a4 100644
--- a/magefiles/go.sum
+++ b/magefiles/go.sum
@@ -1,17 +1,22 @@
-github.com/BurntSushi/toml v1.3.2 h1:o7IhLm0Msx3BaB+n3Ag7L8EVlByGnpq14C4YWiu/gL8=
-github.com/BurntSushi/toml v1.3.2/go.mod h1:CxXYINrC8qIiEnFrOxCa7Jy5BFHlXnUU2pbicEuybxQ=
+github.com/BurntSushi/toml v1.4.0 h1:kuoIxZQy2WRRk1pttg9asf+WVv6tWQuBNVmK8+nqPr0=
+github.com/BurntSushi/toml v1.4.0/go.mod h1:ukJfTF/6rtPPRCnwkur4qwRxa8vTRFBF0uk2lLoLwho=
 github.com/Masterminds/semver v1.5.0 h1:H65muMkzWKEuNDnfl9d70GUjFniHKHRbFPGBuZ3QEww=
 github.com/Masterminds/semver v1.5.0/go.mod h1:MB6lktGJrhw8PrUyiEoblNEGEQ+RzHPF078ddwwvV3Y=
 github.com/blang/semver/v4 v4.0.0 h1:1PFHFE6yCCTv8C1TeyNNarDzntLi7wMI5i/pzqYIsAM=
 github.com/blang/semver/v4 v4.0.0/go.mod h1:IbckMUScFkM3pff0VJDNKRiT6TG/YpiHIM2yvyW5YoQ=
+github.com/chzyer/logex v1.1.10/go.mod h1:+Ywpsq7O8HXn0nuIou7OrIPyXbp3wmkHB+jjWRnGsAI=
+github.com/chzyer/readline v0.0.0-20180603132655-2972be24d48e/go.mod h1:nSuG5e5PlCu98SY8svDHJxuZscDgtXS6KTTbou5AhLI=
+github.com/chzyer/test v0.0.0-20180213035817-a1ea475d72b1/go.mod h1:Q3SI9o4m/ZMnBNeIyt5eFwwo7qiLfzFZmjNmxjkiQlU=
 github.com/creack/pty v1.1.9/go.mod h1:oKZEueFk5CKHvIhNR5MUki03XCEU+Q6VDXinZuGJ33E=
-github.com/cyphar/filepath-securejoin v0.2.4 h1:Ugdm7cg7i6ZK6x3xDF1oEu1nfkyfH53EtKeQYTC3kyg=
-github.com/cyphar/filepath-securejoin v0.2.4/go.mod h1:aPGpWjXOXUn2NCNjFvBE6aRxGGx79pTxQpKOJNYHHl4=
+github.com/cyphar/filepath-securejoin v0.4.1 h1:JyxxyPEaktOD+GAnqIqTf9A8tHyAG22rowi7HkoSU1s=
... (truncated)
```

### 🔸 Commit `900e460cf23d2f880811bcea04075b38e0190186` - Bump github/codeql-action from 3.28.10 to 3.28.11 in the actions group (#12969) (2025-03-11) by `k8s-infra-cherrypick-robot`
- `.github/workflows/scorecards.yml` [M]
```diff
diff --git a/.github/workflows/scorecards.yml b/.github/workflows/scorecards.yml
index 08831c91e..3a652197a 100644
--- a/.github/workflows/scorecards.yml
+++ b/.github/workflows/scorecards.yml
@@ -59,6 +59,6 @@ jobs:
 
       # Upload the results to GitHub's code scanning dashboard.
       - name: "Upload to code-scanning"
-        uses: github/codeql-action/upload-sarif@b56ba49b26e50535fa1e7f7db0f4f7b4bf65d80d # v3.28.10
+        uses: github/codeql-action/upload-sarif@6bb031afdd8eb862ea3fc1848194185e076637e5 # v3.28.11
         with:
           sarif_file: results.sarif
```
- `.github/workflows/vulnerability-scans.yaml` [M]
```diff
diff --git a/.github/workflows/vulnerability-scans.yaml b/.github/workflows/vulnerability-scans.yaml
index 385006e25..7e6c2c314 100644
--- a/.github/workflows/vulnerability-scans.yaml
+++ b/.github/workflows/vulnerability-scans.yaml
@@ -75,7 +75,7 @@ jobs:
 
       # This step checks out a copy of your repository.
       - name: Upload SARIF file
-        uses: github/codeql-action/upload-sarif@b56ba49b26e50535fa1e7f7db0f4f7b4bf65d80d # v3.28.10
+        uses: github/codeql-action/upload-sarif@6bb031afdd8eb862ea3fc1848194185e076637e5 # v3.28.11
         with:
           token: ${{ github.token }}
           # Path to SARIF file relative to the root of the repository
```

### 🔸 Commit `bf7d5b2021a7a83c10fa2a4b644f111089a41e1e` - Docs: Use `enable-global-auth` annotation instead of non-existing ConfigMap option. (#12977) (2025-03-15) by `k8s-infra-cherrypick-robot`
- `docs/user-guide/nginx-configuration/annotations.md` [M]
```diff
diff --git a/docs/user-guide/nginx-configuration/annotations.md b/docs/user-guide/nginx-configuration/annotations.md
index d04ad0ab2..05657d526 100755
--- a/docs/user-guide/nginx-configuration/annotations.md
+++ b/docs/user-guide/nginx-configuration/annotations.md
@@ -541,8 +541,9 @@ nginx.ingress.kubernetes.io/auth-snippet: |
 
 #### Global External Authentication
 
-By default the controller redirects all requests to an existing service that provides authentication if `global-auth-url` is set in the NGINX ConfigMap. If you want to disable this behavior for that ingress, you can use `enable-global-auth: "false"` in the NGINX ConfigMap.
-`nginx.ingress.kubernetes.io/enable-global-auth`:
+By default the controller redirects all requests to an existing service that provides authentication if `global-auth-url` is set in the Ingress NGINX ConfigMap. If you want to disable this behavior for that Ingress, you can use the `nginx.ingress.kubernetes.io/enable-global-auth: "false"` annotation.
+
+- `nginx.ingress.kubernetes.io/enable-global-auth`:
    indicates if GlobalExternalAuth configuration should be applied or not to this Ingress rule. Default values is set to `"true"`.
 
 !!! note
```

### 🔸 Commit `b0d3da82ace626157a9e4500715ce90d942715cc` - Bump the actions group with 3 updates (#12983) (2025-03-17) by `k8s-infra-cherrypick-robot`
- `.github/workflows/golangci-lint.yml` [M]
```diff
diff --git a/.github/workflows/golangci-lint.yml b/.github/workflows/golangci-lint.yml
index 6b66a9afa..2ecd4eb3b 100644
--- a/.github/workflows/golangci-lint.yml
+++ b/.github/workflows/golangci-lint.yml
@@ -28,6 +28,6 @@ jobs:
           check-latest: true
 
       - name: golangci-lint
-        uses: golangci/golangci-lint-action@2226d7cb06a077cd73e56eedd38eecad18e5d837 # v6.5.0
+        uses: golangci/golangci-lint-action@4696ba8babb6127d732c3c6dde519db15edab9ea # v6.5.1
         with:
           only-new-issues: true
```
- `.github/workflows/images.yaml` [M]
```diff
diff --git a/.github/workflows/images.yaml b/.github/workflows/images.yaml
index e38d2cb17..7f5ece52d 100644
--- a/.github/workflows/images.yaml
+++ b/.github/workflows/images.yaml
@@ -202,7 +202,7 @@ jobs:
           version: latest
           platforms: ${{ env.PLATFORMS }}
       - name: Login to GitHub Container Registry
-        uses: docker/login-action@9780b0c442fbb1117ed29e0efdff1e18412f7567 # v3.3.0
+        uses: docker/login-action@74a5d142397b4f367a81961eba4e8cd7edddf772 # v3.4.0
         with:
           username: ${{ secrets.DOCKERHUB_USERNAME }}
           password: ${{ secrets.DOCKERHUB_TOKEN }}
```
- `.github/workflows/vulnerability-scans.yaml` [M]
```diff
diff --git a/.github/workflows/vulnerability-scans.yaml b/.github/workflows/vulnerability-scans.yaml
index 7e6c2c314..65039a781 100644
--- a/.github/workflows/vulnerability-scans.yaml
+++ b/.github/workflows/vulnerability-scans.yaml
@@ -60,7 +60,7 @@ jobs:
 
       - name: Scan image with AquaSec/Trivy
         id: scan
-        uses: aquasecurity/trivy-action@18f2510ee396bbf400402947b394f2dd8c87dbb0 # v0.29.0
+        uses: aquasecurity/trivy-action@6c175e9c4083a92bbca2f9724c8a5e33bc2d97a5 # v0.30.0
         with:
           image-ref: registry.k8s.io/ingress-nginx/controller:${{ matrix.versions }}
           format: 'sarif'
```
- `.github/workflows/zz-tmpl-images.yaml` [M]
```diff
diff --git a/.github/workflows/zz-tmpl-images.yaml b/.github/workflows/zz-tmpl-images.yaml
index 5e98ddf70..f937d6f27 100644
--- a/.github/workflows/zz-tmpl-images.yaml
+++ b/.github/workflows/zz-tmpl-images.yaml
@@ -70,7 +70,7 @@ jobs:
       uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
 
     - name: Login to GitHub Container Registry
-      uses: docker/login-action@9780b0c442fbb1117ed29e0efdff1e18412f7567 # v3.3.0
+      uses: docker/login-action@74a5d142397b4f367a81961eba4e8cd7edddf772 # v3.4.0
       with:
         username: ${{ secrets.DOCKERHUB_USERNAME }}
         password: ${{ secrets.DOCKERHUB_TOKEN }}
```

### 🔸 Commit `67f035d0fee86fffecc25c083948b88d7b62b5c0` - Bump the go group across 3 directories with 9 updates (#12986) (2025-03-17) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index bf9aa2d4a..e758bcaa9 100644
--- a/go.mod
+++ b/go.mod
@@ -1,7 +1,6 @@
 module k8s.io/ingress-nginx
 
 go 1.24.1
-
 require (
 	dario.cat/mergo v1.0.1
 	github.com/armon/go-proxyproto v0.1.0
@@ -30,14 +29,14 @@ require (
 	google.golang.org/grpc/examples v0.0.0-20250306213948-5668c66bc670
 	gopkg.in/go-playground/pool.v3 v3.1.1
 	gopkg.in/mcuadros/go-syslog.v2 v2.3.0
-	k8s.io/api v0.32.2
-	k8s.io/apiextensions-apiserver v0.32.2
-	k8s.io/apimachinery v0.32.2
-	k8s.io/apiserver v0.32.2
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 73e8364f4..ae74d0dbf 100644
--- a/go.sum
+++ b/go.sum
@@ -188,8 +188,8 @@ github.com/prometheus/common v0.62.0 h1:xasJaQlnWAeyHdUBeGjXmutelfJHWMRr+Fg4QszZ
 github.com/prometheus/common v0.62.0/go.mod h1:vyBcEuLSvWos9B1+CyL7JZ2up+uFzXhkqml0W5zIY1I=
 github.com/prometheus/procfs v0.15.1 h1:YagwOFzUgYfKKHX6Dr+sHT7km/hxC76UB0learggepc=
 github.com/prometheus/procfs v0.15.1/go.mod h1:fB45yRUv8NstnjriLhBQLuOUt+WW4BsoGhij/e3PBqk=
-github.com/rogpeppe/go-internal v1.12.0 h1:exVL4IDcn6na9z1rAb56Vxr+CgyK3nn3O+epU5NdKM8=
-github.com/rogpeppe/go-internal v1.12.0/go.mod h1:E+RYuTGaKKdloAfM02xzb0FW3Paa99yedzYV+kq4uf4=
+github.com/rogpeppe/go-internal v1.13.1 h1:KvO1DLK/DRN07sQ1LQKScxyZJuNnedQ5/wKSR38lUII=
+github.com/rogpeppe/go-internal v1.13.1/go.mod h1:uMEvuHeurkdAXX61udpOXGD/AzZDWNMNyH2VO9fmH0o=
 github.com/russross/blackfriday/v2 v2.1.0/go.mod h1:+Rmxgy9KzJVeS9/2gXHxylqXiyQDYRxCVz55jmeOWTM=
 github.com/sergi/go-diff v1.3.1 h1:xkr+Oxo4BOQKmkn/B9eMK0g5Kg/983T9DqqPHwYqD+8=
 github.com/sergi/go-diff v1.3.1/go.mod h1:aMJSSKb2lpPvRNec0+w3fl7LP9IOFzdc9Pa4NFbPK1I=
@@ -341,22 +341,22 @@ gopkg.in/yaml.v2 v2.4.0/go.mod h1:RDklbk79AGWmwhnvt/jBztapEOGDOx6ZbXqjP6csGnQ=
 gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
 gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
 gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
-k8s.io/api v0.32.2 h1:bZrMLEkgizC24G9eViHGOPbW+aRo9duEISRIJKfdJuw=
... (truncated)
```
- `images/ext-auth-example-authsvc/rootfs/go.mod` [M]
```diff
diff --git a/images/ext-auth-example-authsvc/rootfs/go.mod b/images/ext-auth-example-authsvc/rootfs/go.mod
index 57607c938..2c494b503 100644
--- a/images/ext-auth-example-authsvc/rootfs/go.mod
+++ b/images/ext-auth-example-authsvc/rootfs/go.mod
@@ -1,7 +1,6 @@
 module example.com/authsvc
 
 go 1.24.1
-
-require k8s.io/apimachinery v0.32.2
+require k8s.io/apimachinery v0.32.3
 
 require github.com/google/uuid v1.6.0 // indirect
```
- `images/ext-auth-example-authsvc/rootfs/go.sum` [M]
```diff
diff --git a/images/ext-auth-example-authsvc/rootfs/go.sum b/images/ext-auth-example-authsvc/rootfs/go.sum
index 770c22f6a..d1ed58995 100644
--- a/images/ext-auth-example-authsvc/rootfs/go.sum
+++ b/images/ext-auth-example-authsvc/rootfs/go.sum
@@ -1,4 +1,4 @@
 github.com/google/uuid v1.6.0 h1:NIvaJDMOsjHA8n1jAhLSgzrAzy1Hgr+hNrb57e+94F0=
 github.com/google/uuid v1.6.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
-k8s.io/apimachinery v0.32.2 h1:yoQBR9ZGkA6Rgmhbp/yuT9/g+4lxtsGYwW6dR6BDPLQ=
-k8s.io/apimachinery v0.32.2/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
+k8s.io/apimachinery v0.32.3 h1:JmDuDarhDmA/Li7j3aPrwhpNBA94Nvk5zLeOge9HH1U=
+k8s.io/apimachinery v0.32.3/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
```
- `images/kube-webhook-certgen/rootfs/go.mod` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.mod b/images/kube-webhook-certgen/rootfs/go.mod
index 45bbcabfb..5747504ae 100644
--- a/images/kube-webhook-certgen/rootfs/go.mod
+++ b/images/kube-webhook-certgen/rootfs/go.mod
@@ -1,15 +1,14 @@
 module github.com/jet/kube-webhook-certgen
 
 go 1.24.1
-
 require (
 	github.com/onrik/logrus v0.11.0
 	github.com/sirupsen/logrus v1.9.3
 	github.com/spf13/cobra v1.9.1
-	k8s.io/api v0.32.2
-	k8s.io/apimachinery v0.32.2
-	k8s.io/client-go v0.32.2
-	k8s.io/kube-aggregator v0.32.2
+	k8s.io/api v0.32.3
+	k8s.io/apimachinery v0.32.3
+	k8s.io/client-go v0.32.3
... (truncated)
```
- `images/kube-webhook-certgen/rootfs/go.sum` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.sum b/images/kube-webhook-certgen/rootfs/go.sum
index f0cd3441e..cb18c6850 100644
--- a/images/kube-webhook-certgen/rootfs/go.sum
+++ b/images/kube-webhook-certgen/rootfs/go.sum
@@ -141,16 +141,16 @@ gopkg.in/inf.v0 v0.9.1/go.mod h1:cWUDdTG/fYaXco+Dcufb5Vnc6Gp2YChqWtbxRZE0mXw=
 gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
 gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
 gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
-k8s.io/api v0.32.2 h1:bZrMLEkgizC24G9eViHGOPbW+aRo9duEISRIJKfdJuw=
-k8s.io/api v0.32.2/go.mod h1:hKlhk4x1sJyYnHENsrdCWw31FEmCijNGPJO5WzHiJ6Y=
-k8s.io/apimachinery v0.32.2 h1:yoQBR9ZGkA6Rgmhbp/yuT9/g+4lxtsGYwW6dR6BDPLQ=
-k8s.io/apimachinery v0.32.2/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
-k8s.io/client-go v0.32.2 h1:4dYCD4Nz+9RApM2b/3BtVvBHw54QjMFUl1OLcJG5yOA=
-k8s.io/client-go v0.32.2/go.mod h1:fpZ4oJXclZ3r2nDOv+Ux3XcJutfrwjKTCHz2H3sww94=
+k8s.io/api v0.32.3 h1:Hw7KqxRusq+6QSplE3NYG4MBxZw1BZnq4aP4cJVINls=
+k8s.io/api v0.32.3/go.mod h1:2wEDTXADtm/HA7CCMD8D8bK4yuBUptzaRhYcYEEYA3k=
+k8s.io/apimachinery v0.32.3 h1:JmDuDarhDmA/Li7j3aPrwhpNBA94Nvk5zLeOge9HH1U=
+k8s.io/apimachinery v0.32.3/go.mod h1:GpHVgxoKlTxClKcteaeuF1Ul/lDVb74KpZcxcmLDElE=
+k8s.io/client-go v0.32.3 h1:RKPVltzopkSgHS7aS98QdscAgtgah/+zmpAogooIqVU=
+k8s.io/client-go v0.32.3/go.mod h1:3v0+3k4IcT9bXTc4V2rt+d2ZPPG700Xy6Oi0Gdl2PaY=
... (truncated)
```

### 🔸 Commit `ffd547ce36515850a6d54d697acb8475938e7dcc` - Bump github.com/prometheus/common from 0.62.0 to 0.63.0 (#12988) (2025-03-17) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index e758bcaa9..9b0a4fe91 100644
--- a/go.mod
+++ b/go.mod
@@ -18,7 +18,7 @@ require (
 	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2
 	github.com/prometheus/client_golang v1.21.1
 	github.com/prometheus/client_model v0.6.1
-	github.com/prometheus/common v0.62.0
+	github.com/prometheus/common v0.63.0
 	github.com/spf13/cobra v1.9.1
 	github.com/spf13/pflag v1.0.6
 	github.com/stretchr/testify v1.10.0
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index ae74d0dbf..43cfe0f2c 100644
--- a/go.sum
+++ b/go.sum
@@ -184,8 +184,8 @@ github.com/prometheus/client_golang v1.21.1 h1:DOvXXTqVzvkIewV/CDPFdejpMCGeMcbGC
 github.com/prometheus/client_golang v1.21.1/go.mod h1:U9NM32ykUErtVBxdvD3zfi+EuFkkaBvMb09mIfe0Zgg=
 github.com/prometheus/client_model v0.6.1 h1:ZKSh/rekM+n3CeS952MLRAdFwIKqeY8b62p8ais2e9E=
 github.com/prometheus/client_model v0.6.1/go.mod h1:OrxVMOVHjw3lKMa8+x6HeMGkHMQyHDk9E3jmP2AmGiY=
-github.com/prometheus/common v0.62.0 h1:xasJaQlnWAeyHdUBeGjXmutelfJHWMRr+Fg4QszZ2Io=
-github.com/prometheus/common v0.62.0/go.mod h1:vyBcEuLSvWos9B1+CyL7JZ2up+uFzXhkqml0W5zIY1I=
+github.com/prometheus/common v0.63.0 h1:YR/EIY1o3mEFP/kZCD7iDMnLPlGyuU2Gb3HIcXnA98k=
+github.com/prometheus/common v0.63.0/go.mod h1:VVFF/fBIoToEnWRVkYoXEkq3R3paCoxG9PXP74SnV18=
 github.com/prometheus/procfs v0.15.1 h1:YagwOFzUgYfKKHX6Dr+sHT7km/hxC76UB0learggepc=
 github.com/prometheus/procfs v0.15.1/go.mod h1:fB45yRUv8NstnjriLhBQLuOUt+WW4BsoGhij/e3PBqk=
 github.com/rogpeppe/go-internal v1.13.1 h1:KvO1DLK/DRN07sQ1LQKScxyZJuNnedQ5/wKSR38lUII=
```

### 🔸 Commit `0344494037dc87c5a55cfa30874f08824ae58c8f` - Bump dorny/test-reporter from 1.9.1 to 2.0.0 (#12990) (2025-03-17) by `k8s-infra-cherrypick-robot`
- `.github/workflows/junit-reports.yaml` [M]
```diff
diff --git a/.github/workflows/junit-reports.yaml b/.github/workflows/junit-reports.yaml
index e2a82910e..23e9db63c 100644
--- a/.github/workflows/junit-reports.yaml
+++ b/.github/workflows/junit-reports.yaml
@@ -13,7 +13,7 @@ jobs:
   report:
     runs-on: ubuntu-latest
     steps:
-      - uses: dorny/test-reporter@31a54ee7ebcacc03a09ea97a7e5465a47b84aea5 # v1.9.1
+      - uses: dorny/test-reporter@6e6a65b7a0bd2c9197df7d0ae36ac5cee784230c # v2.0.0
         with:
           artifact: /e2e-test-reports-(.*)/
           name: JEST Tests $1               # Name of the check run which will be created
```

### 🔸 Commit `133bf2190196eddde8d59d25b92ef67353ca4243` - Custom Error Pages: Accept first of many MIME types. (#13007) (2025-03-22) by `k8s-infra-cherrypick-robot`
- `images/custom-error-pages/rootfs/main.go` [M]
```diff
diff --git a/images/custom-error-pages/rootfs/main.go b/images/custom-error-pages/rootfs/main.go
index 7d3d73029..4228a7214 100644
--- a/images/custom-error-pages/rootfs/main.go
+++ b/images/custom-error-pages/rootfs/main.go
@@ -126,6 +126,12 @@ func errorHandler(path, defaultFormat string) func(http.ResponseWriter, *http.Re
 			log.Printf("format not specified. Using %v", format)
 		}
 
+		// if multiple formats are provided, use the first one
+		index := strings.Index(format, ",")
+		if index != -1 {
+			format = format[:index]
+		}
+
 		cext, err := mime.ExtensionsByType(format)
 		if err != nil {
 			log.Printf("unexpected error reading media type extension: %v. Using %v", err, ext)
```

### 🔸 Commit `79c996ed6333027f47c8812d3a9e0e19e5320a1a` - Images: Rework. (1/3) (#13015) (2025-03-23) by `k8s-infra-cherrypick-robot`
- `Makefile` [M]
```diff
diff --git a/Makefile b/Makefile
index 0b8f1f5c2..dc7f0a204 100644
--- a/Makefile
+++ b/Makefile
@@ -232,19 +232,21 @@ misspell:  ## Check for spelling errors.
 run-ingress-controller: ## Run the ingress controller locally using a kubectl proxy connection.
 	@build/run-ingress-controller.sh
 
-.PHONY: ensure-buildx
-ensure-buildx:
-	./hack/init-buildx.sh
+.PHONY: builder
+builder:
+	docker buildx create --name $(BUILDER) --bootstrap --use || :
+	docker buildx inspect $(BUILDER)
 
 .PHONY: show-version
 show-version:
 	echo -n $(TAG)
 
... (truncated)
```
- `cloudbuild.yaml` [M]
```diff
diff --git a/cloudbuild.yaml b/cloudbuild.yaml
index 0bb2b60a4..1d0228358 100644
--- a/cloudbuild.yaml
+++ b/cloudbuild.yaml
@@ -2,13 +2,11 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
-    env:
-      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
-      - REPO_INFO=https://github.com/kubernetes/ingress-nginx
-      - COMMIT_SHA=${_PULL_BASE_SHA}
-      - BUILD_ID=${BUILD_ID}
-    entrypoint: bash
-    args:
-      - -c
-      - gcloud auth configure-docker && make release
+- name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
+  env:
... (truncated)
```
- `hack/init-buildx.sh` [D]
```diff
diff --git a/hack/init-buildx.sh b/hack/init-buildx.sh
deleted file mode 100755
index bac68e1ae..000000000
--- a/hack/init-buildx.sh
+++ /dev/null
@@ -1,56 +0,0 @@
-#!/usr/bin/env bash
-
-# Copyright 2020 The Kubernetes Authors.
-#
-# Licensed under the Apache License, Version 2.0 (the "License");
-# you may not use this file except in compliance with the License.
-# You may obtain a copy of the License at
-#
-#     http://www.apache.org/licenses/LICENSE-2.0
-#
-# Unless required by applicable law or agreed to in writing, software
-# distributed under the License is distributed on an "AS IS" BASIS,
-# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-# See the License for the specific language governing permissions and
... (truncated)
```
- `images/Makefile` [M]
```diff
diff --git a/images/Makefile b/images/Makefile
index 31560168d..89d98f7a2 100644
--- a/images/Makefile
+++ b/images/Makefile
@@ -1,4 +1,4 @@
-# Copyright 2024 The Kubernetes Authors.
+# Copyright 2025 The Kubernetes Authors. All rights reserved.
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
@@ -12,75 +12,51 @@
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
-.DEFAULT_GOAL:=build
-
-# set default shell
-SHELL=/bin/bash -o pipefail -o errexit
-
-DIR:=$(strip $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST)))))
... (truncated)
```
- `images/nginx/Makefile` [M]
```diff
diff --git a/images/nginx/Makefile b/images/nginx/Makefile
index 3cc14e5b3..803f8ae80 100644
--- a/images/nginx/Makefile
+++ b/images/nginx/Makefile
@@ -1,4 +1,4 @@
-# Copyright 2024 The Kubernetes Authors. All rights reserved.
+# Copyright 2025 The Kubernetes Authors. All rights reserved.
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
@@ -12,48 +12,37 @@
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
-.DEFAULT_GOAL:=build
-
-# set default shell
-SHELL=/bin/bash -o pipefail -o errexit
-
-DIR:=$(strip $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST)))))
... (truncated)
```
- `images/nginx/cloudbuild.yaml` [M]
```diff
diff --git a/images/nginx/cloudbuild.yaml b/images/nginx/cloudbuild.yaml
index 2563692d7..d28af1aa5 100644
--- a/images/nginx/cloudbuild.yaml
+++ b/images/nginx/cloudbuild.yaml
@@ -4,11 +4,9 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
-    env:
-      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
-    entrypoint: bash
-    args:
-      - -c
-      - gcloud auth configure-docker && cd images/nginx && make push
+- name: gcr.io/cloud-builders/docker
+  dir: images/nginx
+  entrypoint: make
+  args:
+  - push
... (truncated)
```
- `images/nginx/rootfs/Dockerfile` [M]
```diff
diff --git a/images/nginx/rootfs/Dockerfile b/images/nginx/rootfs/Dockerfile
index 834a9bcf3..8f6bab137 100644
--- a/images/nginx/rootfs/Dockerfile
+++ b/images/nginx/rootfs/Dockerfile
@@ -11,7 +11,7 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
-FROM alpine:3.21 as builder
+FROM alpine:3.21 AS builder
 
 COPY . /
```
- `images/nginx/rootfs/build.sh` [M]
```diff
diff --git a/images/nginx/rootfs/build.sh b/images/nginx/rootfs/build.sh
index 9d87a0a45..54eb5a410 100755
--- a/images/nginx/rootfs/build.sh
+++ b/images/nginx/rootfs/build.sh
@@ -186,10 +186,6 @@ apk add \
 
 # apk add -X http://dl-cdn.alpinelinux.org/alpine/edge/testing opentelemetry-cpp-dev
 
-# There is some bug with some platforms and git, so force HTTP/1.1
-git config --global http.version HTTP/1.1
-git config --global http.postBuffer 157286400
-
 mkdir -p /etc/nginx
 
 mkdir --verbose -p "$BUILD_PATH"
```
- `images/test-runner/Makefile` [M]
```diff
diff --git a/images/test-runner/Makefile b/images/test-runner/Makefile
index f3987204e..78be8179d 100644
--- a/images/test-runner/Makefile
+++ b/images/test-runner/Makefile
@@ -1,4 +1,4 @@
-# Copyright 2018 The Kubernetes Authors. All rights reserved.
+# Copyright 2025 The Kubernetes Authors. All rights reserved.
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
@@ -12,64 +12,28 @@
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
-# set default shell
-SHELL=/bin/bash -o pipefail -o errexit
+BUILDER ?= ingress-nginx
+PLATFORMS ?= linux/amd64,linux/arm64
+REGISTRY ?= us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
+IMAGE ?= $(REGISTRY)/e2e-test-runner
... (truncated)
```
- `images/test-runner/cloudbuild.yaml` [M]
```diff
diff --git a/images/test-runner/cloudbuild.yaml b/images/test-runner/cloudbuild.yaml
index 93dce3ec9..2f49ddafc 100644
--- a/images/test-runner/cloudbuild.yaml
+++ b/images/test-runner/cloudbuild.yaml
@@ -2,10 +2,8 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
-    env:
-      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
-    entrypoint: bash
-    args:
-      - -c
-      - gcloud auth configure-docker && cd images/test-runner && make push
+- name: gcr.io/cloud-builders/docker
+  dir: images/test-runner
+  entrypoint: make
+  args:
+  - push
```
- `images/test-runner/rootfs/Dockerfile` [M]
```diff
diff --git a/images/test-runner/rootfs/Dockerfile b/images/test-runner/rootfs/Dockerfile
index d871461bf..69fae92d7 100644
--- a/images/test-runner/rootfs/Dockerfile
+++ b/images/test-runner/rootfs/Dockerfile
@@ -15,8 +15,8 @@ ARG BASE_IMAGE
 ARG GOLANG_VERSION
 ARG ETCD_VERSION
 
-FROM golang:${GOLANG_VERSION}-alpine3.21 as GO
-FROM registry.k8s.io/etcd:${ETCD_VERSION} as etcd
+FROM golang:${GOLANG_VERSION}-alpine3.21 AS go
+FROM registry.k8s.io/etcd:${ETCD_VERSION} AS etcd
 
 FROM ${BASE_IMAGE}
 
@@ -41,9 +41,9 @@ RUN set -eux; \
 		echo 'hosts: files dns' > /etc/nsswitch.conf; \
 	fi
 
-COPY --from=GO   /usr/local/go /usr/local/go
... (truncated)
```

### 🔸 Commit `17fb5c9fd399ff08a9d99a3330d18f3b4d30e607` - Images: Rework. (2/3) (#13012) (2025-03-23) by `k8s-infra-cherrypick-robot`
- `images/cfssl/cloudbuild.yaml` [M]
```diff
diff --git a/images/cfssl/cloudbuild.yaml b/images/cfssl/cloudbuild.yaml
index 33fafdb08..10039e5b1 100644
--- a/images/cfssl/cloudbuild.yaml
+++ b/images/cfssl/cloudbuild.yaml
@@ -2,10 +2,10 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
-    env:
-      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
-    entrypoint: bash
-    args:
-      - -c
-      - gcloud auth configure-docker && cd images && make NAME=cfssl push
+- name: gcr.io/cloud-builders/docker
+  dir: images
+  env:
+  - NAME=cfssl
+  entrypoint: make
... (truncated)
```
- `images/custom-error-pages/cloudbuild.yaml` [M]
```diff
diff --git a/images/custom-error-pages/cloudbuild.yaml b/images/custom-error-pages/cloudbuild.yaml
index 324a8f19a..38db680f4 100644
--- a/images/custom-error-pages/cloudbuild.yaml
+++ b/images/custom-error-pages/cloudbuild.yaml
@@ -2,10 +2,10 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
-    env:
-      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
-    entrypoint: bash
-    args:
-      - -c
-      - gcloud auth configure-docker && cd images && make NAME=custom-error-pages push
+- name: gcr.io/cloud-builders/docker
+  dir: images
+  env:
+  - NAME=custom-error-pages
+  entrypoint: make
... (truncated)
```
- `images/e2e-test-echo/cloudbuild.yaml` [M]
```diff
diff --git a/images/e2e-test-echo/cloudbuild.yaml b/images/e2e-test-echo/cloudbuild.yaml
index 02bfc034a..c964f6d3d 100644
--- a/images/e2e-test-echo/cloudbuild.yaml
+++ b/images/e2e-test-echo/cloudbuild.yaml
@@ -2,10 +2,10 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
-    env:
-      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
-    entrypoint: bash
-    args:
-      - -c
-      - gcloud auth configure-docker && cd images && make NAME=e2e-test-echo push
+- name: gcr.io/cloud-builders/docker
+  dir: images
+  env:
+  - NAME=e2e-test-echo
+  entrypoint: make
... (truncated)
```

### 🔸 Commit `a1945904d77de54c388f899e91128974396f8773` - Images: Rework. (3/3) (#13017) (2025-03-23) by `k8s-infra-cherrypick-robot`
- `images/fastcgi-helloserver/cloudbuild.yaml` [M]
```diff
diff --git a/images/fastcgi-helloserver/cloudbuild.yaml b/images/fastcgi-helloserver/cloudbuild.yaml
index c2c6135df..6fa7a236f 100644
--- a/images/fastcgi-helloserver/cloudbuild.yaml
+++ b/images/fastcgi-helloserver/cloudbuild.yaml
@@ -2,10 +2,10 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
-    env:
-      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
-    entrypoint: bash
-    args:
-      - -c
-      - gcloud auth configure-docker && cd images && make NAME=fastcgi-helloserver push
+- name: gcr.io/cloud-builders/docker
+  dir: images
+  env:
+  - NAME=fastcgi-helloserver
+  entrypoint: make
... (truncated)
```
- `images/httpbun/cloudbuild.yaml` [M]
```diff
diff --git a/images/httpbun/cloudbuild.yaml b/images/httpbun/cloudbuild.yaml
index c56820d15..641735dd8 100644
--- a/images/httpbun/cloudbuild.yaml
+++ b/images/httpbun/cloudbuild.yaml
@@ -2,10 +2,10 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
-    env:
-      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
-    entrypoint: bash
-    args:
-      - -c
-      - gcloud auth configure-docker && cd images && make NAME=httpbun push
+- name: gcr.io/cloud-builders/docker
+  dir: images
+  env:
+  - NAME=httpbun
+  entrypoint: make
... (truncated)
```
- `images/kube-webhook-certgen/cloudbuild.yaml` [M]
```diff
diff --git a/images/kube-webhook-certgen/cloudbuild.yaml b/images/kube-webhook-certgen/cloudbuild.yaml
index e4118ff88..bf7c2a67e 100644
--- a/images/kube-webhook-certgen/cloudbuild.yaml
+++ b/images/kube-webhook-certgen/cloudbuild.yaml
@@ -2,10 +2,10 @@ options:
   # Ignore Prow provided substitutions.
   substitution_option: ALLOW_LOOSE
 steps:
-  - name: gcr.io/k8s-staging-test-infra/gcb-docker-gcloud:v20250116-2a05ea7e3d
-    env:
-      - REGISTRY=us-central1-docker.pkg.dev/k8s-staging-images/ingress-nginx
-    entrypoint: bash
-    args:
-      - -c
-      - gcloud auth configure-docker && cd images && make NAME=kube-webhook-certgen push
+- name: gcr.io/cloud-builders/docker
+  dir: images
+  env:
+  - NAME=kube-webhook-certgen
+  entrypoint: make
... (truncated)
```

### 🔸 Commit `2d16da71838b81e473a2ab098b89638ae9b9d7b0` - Bump the actions group with 5 updates (#13024) (2025-03-23) by `k8s-infra-cherrypick-robot`
- `.github/workflows/ci.yaml` [M]
```diff
diff --git a/.github/workflows/ci.yaml b/.github/workflows/ci.yaml
index 581b5adb0..6e1893fa9 100644
--- a/.github/workflows/ci.yaml
+++ b/.github/workflows/ci.yaml
@@ -86,7 +86,7 @@ jobs:
 
       - name: Set up Go
         id: go
-        uses: actions/setup-go@f111f3307d8850f501ac008e886eec1fd1932a34 # v5.3.0
+        uses: actions/setup-go@0aaccfd150d50ccaeb58ebd88d36e91967a5f35b # v5.4.0
         with:
           go-version: ${{ env.GOLANG_VERSION }}
           check-latest: true
@@ -108,7 +108,7 @@ jobs:
         run: echo "GOLANG_VERSION=$(cat GOLANG_VERSION)" >> $GITHUB_ENV
       - name: Set up Go
         id: go
-        uses: actions/setup-go@f111f3307d8850f501ac008e886eec1fd1932a34 # v5.3.0
+        uses: actions/setup-go@0aaccfd150d50ccaeb58ebd88d36e91967a5f35b # v5.4.0
         with:
... (truncated)
```
- `.github/workflows/golangci-lint.yml` [M]
```diff
diff --git a/.github/workflows/golangci-lint.yml b/.github/workflows/golangci-lint.yml
index 2ecd4eb3b..8f957f8f2 100644
--- a/.github/workflows/golangci-lint.yml
+++ b/.github/workflows/golangci-lint.yml
@@ -22,12 +22,12 @@ jobs:
 
       - name: Set up Go
         id: go
-        uses: actions/setup-go@f111f3307d8850f501ac008e886eec1fd1932a34 # v5.3.0
+        uses: actions/setup-go@0aaccfd150d50ccaeb58ebd88d36e91967a5f35b # v5.4.0
         with:
           go-version: ${{ env.GOLANG_VERSION }}
           check-latest: true
 
       - name: golangci-lint
-        uses: golangci/golangci-lint-action@4696ba8babb6127d732c3c6dde519db15edab9ea # v6.5.1
+        uses: golangci/golangci-lint-action@55c2c1448f86e01eaae002a5a3a9624417608d84 # v6.5.2
         with:
           only-new-issues: true
```
- `.github/workflows/images.yaml` [M]
```diff
diff --git a/.github/workflows/images.yaml b/.github/workflows/images.yaml
index 7f5ece52d..6a49b08b9 100644
--- a/.github/workflows/images.yaml
+++ b/.github/workflows/images.yaml
@@ -148,7 +148,7 @@ jobs:
 
     - name: Set up Go
       id: go
-      uses: actions/setup-go@f111f3307d8850f501ac008e886eec1fd1932a34 # v5.3.0
+      uses: actions/setup-go@0aaccfd150d50ccaeb58ebd88d36e91967a5f35b # v5.4.0
       with:
         go-version: ${{ env.GOLANG_VERSION }}
         check-latest: true
```
- `.github/workflows/plugin.yaml` [M]
```diff
diff --git a/.github/workflows/plugin.yaml b/.github/workflows/plugin.yaml
index 20f2caeae..8ec38d5fb 100644
--- a/.github/workflows/plugin.yaml
+++ b/.github/workflows/plugin.yaml
@@ -20,7 +20,7 @@ jobs:
         run: echo "GOLANG_VERSION=$(cat GOLANG_VERSION)" >> $GITHUB_ENV
 
       - name: Set up Go
-        uses: actions/setup-go@f111f3307d8850f501ac008e886eec1fd1932a34 # v5.3.0
+        uses: actions/setup-go@0aaccfd150d50ccaeb58ebd88d36e91967a5f35b # v5.4.0
         with:
           go-version: ${{ env.GOLANG_VERSION }}
           check-latest: true
```
- `.github/workflows/scorecards.yml` [M]
```diff
diff --git a/.github/workflows/scorecards.yml b/.github/workflows/scorecards.yml
index 3a652197a..f57976104 100644
--- a/.github/workflows/scorecards.yml
+++ b/.github/workflows/scorecards.yml
@@ -51,7 +51,7 @@ jobs:
       # Upload the results as artifacts (optional). Commenting out will disable uploads of run results in SARIF
       # format to the repository Actions tab.
       - name: "Upload artifact"
-        uses: actions/upload-artifact@4cec3d8aa04e39d1a68397de0c4cd6fb9dce8ec1 # v4.6.1
+        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4.6.2
         with:
           name: SARIF file
           path: results.sarif
@@ -59,6 +59,6 @@ jobs:
 
       # Upload the results to GitHub's code scanning dashboard.
       - name: "Upload to code-scanning"
-        uses: github/codeql-action/upload-sarif@6bb031afdd8eb862ea3fc1848194185e076637e5 # v3.28.11
+        uses: github/codeql-action/upload-sarif@5f8171a638ada777af81d42b55959a643bb29017 # v3.28.12
         with:
... (truncated)
```
- `.github/workflows/vulnerability-scans.yaml` [M]
```diff
diff --git a/.github/workflows/vulnerability-scans.yaml b/.github/workflows/vulnerability-scans.yaml
index 65039a781..a8f708ad6 100644
--- a/.github/workflows/vulnerability-scans.yaml
+++ b/.github/workflows/vulnerability-scans.yaml
@@ -75,7 +75,7 @@ jobs:
 
       # This step checks out a copy of your repository.
       - name: Upload SARIF file
-        uses: github/codeql-action/upload-sarif@6bb031afdd8eb862ea3fc1848194185e076637e5 # v3.28.11
+        uses: github/codeql-action/upload-sarif@5f8171a638ada777af81d42b55959a643bb29017 # v3.28.12
         with:
           token: ${{ github.token }}
           # Path to SARIF file relative to the root of the repository
```
- `.github/workflows/zz-tmpl-k8s-e2e.yaml` [M]
```diff
diff --git a/.github/workflows/zz-tmpl-k8s-e2e.yaml b/.github/workflows/zz-tmpl-k8s-e2e.yaml
index ef8da9edf..75e602588 100644
--- a/.github/workflows/zz-tmpl-k8s-e2e.yaml
+++ b/.github/workflows/zz-tmpl-k8s-e2e.yaml
@@ -23,7 +23,7 @@ jobs:
         uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
 
       - name: cache
-        uses: actions/download-artifact@cc203385981b70ca67e1cc392babf9cc229d5806 # v4.1.9
+        uses: actions/download-artifact@95815c38cf2ff2164869cbab79da8d1f422bc89e # v4.2.1
         with:
           name: docker.tar.gz
 
@@ -50,7 +50,7 @@ jobs:
           make kind-e2e-test
 
       - name: Upload e2e junit-reports ${{ inputs.variation }}
-        uses: actions/upload-artifact@4cec3d8aa04e39d1a68397de0c4cd6fb9dce8ec1 # v4.6.1
+        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4.6.2
         if: success() || failure()
... (truncated)
```

### 🔸 Commit `ee6686be0f3cae1b40fac6c9f1ccc33746237399` - CI: Update Kubernetes to v1.32.3. (#13026) (2025-03-23) by `k8s-infra-cherrypick-robot`
- `.github/workflows/ci.yaml` [M]
```diff
diff --git a/.github/workflows/ci.yaml b/.github/workflows/ci.yaml
index 6e1893fa9..de8eee751 100644
--- a/.github/workflows/ci.yaml
+++ b/.github/workflows/ci.yaml
@@ -156,7 +156,7 @@ jobs:
 
       - name: Prepare Host
         run: |
-          curl -LO https://dl.k8s.io/release/v1.32.2/bin/linux/amd64/kubectl
+          curl -LO https://dl.k8s.io/release/v1.32.3/bin/linux/amd64/kubectl
           chmod +x ./kubectl
           sudo mv ./kubectl /usr/local/bin/kubectl
```
- `images/test-runner/Makefile` [M]
```diff
diff --git a/images/test-runner/Makefile b/images/test-runner/Makefile
index 78be8179d..d0a7471a6 100644
--- a/images/test-runner/Makefile
+++ b/images/test-runner/Makefile
@@ -35,7 +35,7 @@ build: builder
 		--build-arg BASE_IMAGE=$(BASE_IMAGE) \
 		--build-arg GOLANG_VERSION=$(GOLANG_VERSION) \
 		--build-arg ETCD_VERSION=3.5.13-0 \
-		--build-arg K8S_RELEASE=v1.32.2 \
+		--build-arg K8S_RELEASE=v1.32.3 \
 		--build-arg RESTY_CLI_VERSION=0.27 \
 		--build-arg RESTY_CLI_SHA=e5f4f3128af49ba5c4d039d0554e5ae91bbe05866f60eccfa96d3653274bff90 \
 		--build-arg LUAROCKS_VERSION=3.8.0 \
```

### 🔸 Commit `44e20ccb22427126733e4ede6c2a23469862c57e` - Bump github.com/onsi/ginkgo/v2 from 2.23.0 to 2.23.3 (#13028) (2025-03-23) by `k8s-infra-cherrypick-robot`
- `build/run-in-docker.sh` [M]
```diff
diff --git a/build/run-in-docker.sh b/build/run-in-docker.sh
index 1b2e6e663..47b49183e 100755
--- a/build/run-in-docker.sh
+++ b/build/run-in-docker.sh
@@ -79,7 +79,7 @@ if [[ "$DOCKER_IN_DOCKER_ENABLED" == "true" ]]; then
   echo "..reached DIND check TRUE block, inside run-in-docker.sh"
   echo "FLAGS=$FLAGS"
   #go env
-  go install -mod=mod github.com/onsi/ginkgo/v2/ginkgo@v2.23.0
+  go install -mod=mod github.com/onsi/ginkgo/v2/ginkgo@v2.23.3
   find / -type f -name ginkgo 2>/dev/null
   which ginkgo
   /bin/bash -c "${FLAGS}"
```
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 9b0a4fe91..6f68abdb8 100644
--- a/go.mod
+++ b/go.mod
@@ -1,6 +1,7 @@
 module k8s.io/ingress-nginx
 
 go 1.24.1
+
 require (
 	dario.cat/mergo v1.0.1
 	github.com/armon/go-proxyproto v0.1.0
@@ -13,7 +14,7 @@ require (
 	github.com/mitchellh/mapstructure v1.5.0
 	github.com/moul/pb v0.0.0-20220425114252-bca18df4138c
 	github.com/ncabatoff/process-exporter v0.8.5
-	github.com/onsi/ginkgo/v2 v2.23.0
+	github.com/onsi/ginkgo/v2 v2.23.3
 	github.com/opencontainers/runc v1.2.5
 	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 43cfe0f2c..24866a8d3 100644
--- a/go.sum
+++ b/go.sum
@@ -163,8 +163,8 @@ github.com/onsi/ginkgo v1.6.0/go.mod h1:lLunBs/Ym6LB5Z9jYTR76FiuTmxDTDusOGeTQH+W
 github.com/onsi/ginkgo v1.12.1/go.mod h1:zj2OWP4+oCPe1qIXoGWkgMRwljMUYCdkwsT2108oapk=
 github.com/onsi/ginkgo v1.16.5 h1:8xi0RTUf59SOSfEtZMvwTvXYMzG4gV23XVHOZiXNtnE=
 github.com/onsi/ginkgo v1.16.5/go.mod h1:+E8gABHa3K6zRBolWtd+ROzc/U5bkGt0FwiG042wbpU=
-github.com/onsi/ginkgo/v2 v2.23.0 h1:FA1xjp8ieYDzlgS5ABTpdUDB7wtngggONc8a7ku2NqQ=
-github.com/onsi/ginkgo/v2 v2.23.0/go.mod h1:zXTP6xIp3U8aVuXN8ENK9IXRaTjFnpVB9mGmaSRvxnM=
+github.com/onsi/ginkgo/v2 v2.23.3 h1:edHxnszytJ4lD9D5Jjc4tiDkPBZ3siDeJJkUZJJVkp0=
+github.com/onsi/ginkgo/v2 v2.23.3/go.mod h1:zXTP6xIp3U8aVuXN8ENK9IXRaTjFnpVB9mGmaSRvxnM=
 github.com/onsi/gomega v1.7.1/go.mod h1:XdKZgCCFLUoM/7CFJVPcG8C1xQ1AJ0vpAezJrB7JYyY=
 github.com/onsi/gomega v1.10.1/go.mod h1:iN09h71vgCQne3DLsj+A5owkum+a2tYe+TOCB1ybHNo=
 github.com/onsi/gomega v1.36.2 h1:koNYke6TVk6ZmnyHrCXba/T/MoLBXFjeC1PtvYgw0A8=
```
- `images/kube-webhook-certgen/rootfs/go.mod` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.mod b/images/kube-webhook-certgen/rootfs/go.mod
index 5747504ae..0d6467d6f 100644
--- a/images/kube-webhook-certgen/rootfs/go.mod
+++ b/images/kube-webhook-certgen/rootfs/go.mod
@@ -1,6 +1,7 @@
 module github.com/jet/kube-webhook-certgen
 
 go 1.24.1
+
 require (
 	github.com/onrik/logrus v0.11.0
 	github.com/sirupsen/logrus v1.9.3
@@ -32,7 +33,7 @@ require (
 	github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd // indirect
 	github.com/modern-go/reflect2 v1.0.2 // indirect
 	github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 // indirect
-	github.com/onsi/ginkgo/v2 v2.23.0 // indirect
+	github.com/onsi/ginkgo/v2 v2.23.3 // indirect
 	github.com/onsi/gomega v1.36.2 // indirect
 	github.com/pkg/errors v0.9.1 // indirect
... (truncated)
```
- `images/kube-webhook-certgen/rootfs/go.sum` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.sum b/images/kube-webhook-certgen/rootfs/go.sum
index cb18c6850..3fc75b432 100644
--- a/images/kube-webhook-certgen/rootfs/go.sum
+++ b/images/kube-webhook-certgen/rootfs/go.sum
@@ -56,8 +56,8 @@ github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 h1:C3w9PqII01/Oq
 github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822/go.mod h1:+n7T8mK8HuQTcFwEeznm/DIxMOiR9yIdICNftLE1DvQ=
 github.com/onrik/logrus v0.11.0 h1:pu+BCaWL36t0yQaj/2UHK2erf88dwssAKOT51mxPUVs=
 github.com/onrik/logrus v0.11.0/go.mod h1:fO2vlZwIdti6PidD3gV5YKt9Lq5ptpnP293RAe1ITwk=
-github.com/onsi/ginkgo/v2 v2.23.0 h1:FA1xjp8ieYDzlgS5ABTpdUDB7wtngggONc8a7ku2NqQ=
-github.com/onsi/ginkgo/v2 v2.23.0/go.mod h1:zXTP6xIp3U8aVuXN8ENK9IXRaTjFnpVB9mGmaSRvxnM=
+github.com/onsi/ginkgo/v2 v2.23.3 h1:edHxnszytJ4lD9D5Jjc4tiDkPBZ3siDeJJkUZJJVkp0=
+github.com/onsi/ginkgo/v2 v2.23.3/go.mod h1:zXTP6xIp3U8aVuXN8ENK9IXRaTjFnpVB9mGmaSRvxnM=
 github.com/onsi/gomega v1.36.2 h1:koNYke6TVk6ZmnyHrCXba/T/MoLBXFjeC1PtvYgw0A8=
 github.com/onsi/gomega v1.36.2/go.mod h1:DdwyADRjrc825LhMEkD76cHR5+pUnjhUN8GlHlRPHzY=
 github.com/pkg/errors v0.9.1 h1:FEBLx1zS214owpjy7qsBeixbURkuhQAwrK5UwLGTwt4=
```
- `images/test-runner/Makefile` [M]
```diff
diff --git a/images/test-runner/Makefile b/images/test-runner/Makefile
index d0a7471a6..338651006 100644
--- a/images/test-runner/Makefile
+++ b/images/test-runner/Makefile
@@ -44,7 +44,7 @@ build: builder
 		--build-arg YAML_LINT_VERSION=1.33.0 \
 		--build-arg YAMALE_VERSION=4.0.4 \
 		--build-arg HELM_VERSION=3.14.4 \
-		--build-arg GINKGO_VERSION=2.23.0 \
+		--build-arg GINKGO_VERSION=2.23.3 \
 		--build-arg GOLINT_VERSION=latest \
 		rootfs \
 		--tag $(IMAGE):$(TAG) \
```
- `test/e2e/run-chart-test.sh` [M]
```diff
diff --git a/test/e2e/run-chart-test.sh b/test/e2e/run-chart-test.sh
index 33e879da8..ee200bea5 100755
--- a/test/e2e/run-chart-test.sh
+++ b/test/e2e/run-chart-test.sh
@@ -78,7 +78,7 @@ fi
 
 if [ "${SKIP_IMAGE_CREATION:-false}" = "false" ]; then
   if ! command -v ginkgo &> /dev/null; then
-    go install github.com/onsi/ginkgo/v2/ginkgo@v2.23.0
+    go install github.com/onsi/ginkgo/v2/ginkgo@v2.23.3
   fi
   echo "[dev-env] building image"
   make -C ${DIR}/../../ clean-image build image
```
- `test/e2e/run-kind-e2e.sh` [M]
```diff
diff --git a/test/e2e/run-kind-e2e.sh b/test/e2e/run-kind-e2e.sh
index 855797d70..d43c35d90 100755
--- a/test/e2e/run-kind-e2e.sh
+++ b/test/e2e/run-kind-e2e.sh
@@ -96,7 +96,7 @@ fi
 
 if [ "${SKIP_E2E_IMAGE_CREATION}" = "false" ]; then
   if ! command -v ginkgo &> /dev/null; then
-    go install github.com/onsi/ginkgo/v2/ginkgo@v2.23.0
+    go install github.com/onsi/ginkgo/v2/ginkgo@v2.23.3
   fi
 
   echo "[dev-env] .. done building controller images"
```

### 🔸 Commit `781ab63e0f4b8d71c63464c48605492cd39d18d8` - CI: Update KIND to v1.32.3. (#13030) (2025-03-23) by `Marco Ebert`
- `build/dev-env.sh` [M]
```diff
diff --git a/build/dev-env.sh b/build/dev-env.sh
index e83369f6c..f919a1205 100755
--- a/build/dev-env.sh
+++ b/build/dev-env.sh
@@ -64,7 +64,7 @@ echo "[dev-env] building image"
 make build image
 docker tag "${REGISTRY}/controller:${TAG}" "${DEV_IMAGE}"
 
-export K8S_VERSION=${K8S_VERSION:-v1.32.2@sha256:f226345927d7e348497136874b6d207e0b32cc52154ad8323129352923a3142f}
+export K8S_VERSION=${K8S_VERSION:-v1.32.3@sha256:b36e76b4ad37b88539ce5e07425f77b29f73a8eaaebf3f1a8bc9c764401d118c}
 
 KIND_CLUSTER_NAME="ingress-nginx-dev"
```
- `test/e2e/run-chart-test.sh` [M]
```diff
diff --git a/test/e2e/run-chart-test.sh b/test/e2e/run-chart-test.sh
index ee200bea5..719d098a0 100755
--- a/test/e2e/run-chart-test.sh
+++ b/test/e2e/run-chart-test.sh
@@ -62,7 +62,7 @@ export KUBECONFIG="${KUBECONFIG:-$HOME/.kube/kind-config-$KIND_CLUSTER_NAME}"
 if [ "${SKIP_CLUSTER_CREATION:-false}" = "false" ]; then
   echo "[dev-env] creating Kubernetes cluster with kind"
 
-  export K8S_VERSION=${K8S_VERSION:-v1.32.2@sha256:f226345927d7e348497136874b6d207e0b32cc52154ad8323129352923a3142f}
+  export K8S_VERSION=${K8S_VERSION:-v1.32.3@sha256:b36e76b4ad37b88539ce5e07425f77b29f73a8eaaebf3f1a8bc9c764401d118c}
 
   kind create cluster \
     --verbosity=${KIND_LOG_LEVEL} \
```
- `test/e2e/run-kind-e2e.sh` [M]
```diff
diff --git a/test/e2e/run-kind-e2e.sh b/test/e2e/run-kind-e2e.sh
index d43c35d90..9c751efe3 100755
--- a/test/e2e/run-kind-e2e.sh
+++ b/test/e2e/run-kind-e2e.sh
@@ -64,7 +64,7 @@ echo "Running e2e with nginx base image ${NGINX_BASE_IMAGE}"
 if [ "${SKIP_CLUSTER_CREATION}" = "false" ]; then
   echo "[dev-env] creating Kubernetes cluster with kind"
 
-  export K8S_VERSION=${K8S_VERSION:-v1.32.2@sha256:f226345927d7e348497136874b6d207e0b32cc52154ad8323129352923a3142f}
+  export K8S_VERSION=${K8S_VERSION:-v1.32.3@sha256:b36e76b4ad37b88539ce5e07425f77b29f73a8eaaebf3f1a8bc9c764401d118c}
 
   # delete the cluster if it exists
   if kind get clusters | grep "${KIND_CLUSTER_NAME}"; then
```

### 🔸 Commit `2da8520b9fcc7f31a2b614423046402d1e256b68` - Bump github.com/opencontainers/runc from 1.2.5 to 1.2.6 in the go group across 1 directory (#13034) (2025-03-24) by `k8s-infra-cherrypick-robot`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 6f68abdb8..4d67f63d7 100644
--- a/go.mod
+++ b/go.mod
@@ -15,7 +15,7 @@ require (
 	github.com/moul/pb v0.0.0-20220425114252-bca18df4138c
 	github.com/ncabatoff/process-exporter v0.8.5
 	github.com/onsi/ginkgo/v2 v2.23.3
-	github.com/opencontainers/runc v1.2.5
+	github.com/opencontainers/runc v1.2.6
 	github.com/pmezard/go-difflib v1.0.1-0.20181226105442-5d4384ee4fb2
 	github.com/prometheus/client_golang v1.21.1
 	github.com/prometheus/client_model v0.6.1
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index 24866a8d3..fab4476b7 100644
--- a/go.sum
+++ b/go.sum
@@ -169,8 +169,8 @@ github.com/onsi/gomega v1.7.1/go.mod h1:XdKZgCCFLUoM/7CFJVPcG8C1xQ1AJ0vpAezJrB7J
 github.com/onsi/gomega v1.10.1/go.mod h1:iN09h71vgCQne3DLsj+A5owkum+a2tYe+TOCB1ybHNo=
 github.com/onsi/gomega v1.36.2 h1:koNYke6TVk6ZmnyHrCXba/T/MoLBXFjeC1PtvYgw0A8=
 github.com/onsi/gomega v1.36.2/go.mod h1:DdwyADRjrc825LhMEkD76cHR5+pUnjhUN8GlHlRPHzY=
-github.com/opencontainers/runc v1.2.5 h1:8KAkq3Wrem8bApgOHyhRI/8IeLXIfmZ6Qaw6DNSLnA4=
-github.com/opencontainers/runc v1.2.5/go.mod h1:dOQeFo29xZKBNeRBI0B19mJtfHv68YgCTh1X+YphA+4=
+github.com/opencontainers/runc v1.2.6 h1:P7Hqg40bsMvQGCS4S7DJYhUZOISMLJOB2iGX5COWiPk=
+github.com/opencontainers/runc v1.2.6/go.mod h1:dOQeFo29xZKBNeRBI0B19mJtfHv68YgCTh1X+YphA+4=
 github.com/opencontainers/runtime-spec v1.2.1 h1:S4k4ryNgEpxW1dzyqffOmhI1BHYcjzU8lpJfSlR0xww=
 github.com/opencontainers/runtime-spec v1.2.1/go.mod h1:jwyrGlmzljRJv/Fgzds9SsS/C5hL+LL3ko9hs6T5lQ0=
 github.com/peterbourgon/diskv v2.0.1+incompatible h1:UBdAOUP5p4RWqPBg048CAvpKN+vxiaj6gdUUzhl4XmI=
```

### 🔸 Commit `ebf2c460cc74c38758420e8f14c5f4c210e6b861` - Go: Update dependencies. (#13037) (2025-03-24) by `Marco Ebert`
- `go.mod` [M]
```diff
diff --git a/go.mod b/go.mod
index 4d67f63d7..26cff52e0 100644
--- a/go.mod
+++ b/go.mod
@@ -27,7 +27,7 @@ require (
 	github.com/zakjan/cert-chain-resolver v0.0.0-20221221105603-fcedb00c5b30
 	golang.org/x/crypto v0.36.0
 	google.golang.org/grpc v1.71.0
-	google.golang.org/grpc/examples v0.0.0-20250306213948-5668c66bc670
+	google.golang.org/grpc/examples v0.0.0-20250321200952-b0d120384670
 	gopkg.in/go-playground/pool.v3 v3.1.1
 	gopkg.in/mcuadros/go-syslog.v2 v2.3.0
 	k8s.io/api v0.32.3
@@ -74,9 +74,9 @@ require (
 	github.com/fullsailor/pkcs7 v0.0.0-20190404230743-d7302db945fa // indirect
 	github.com/go-errors/errors v1.5.1 // indirect
 	github.com/go-logr/logr v1.4.2 // indirect
-	github.com/go-openapi/jsonpointer v0.21.0 // indirect
+	github.com/go-openapi/jsonpointer v0.21.1 // indirect
 	github.com/go-openapi/jsonreference v0.21.0 // indirect
... (truncated)
```
- `go.sum` [M]
```diff
diff --git a/go.sum b/go.sum
index fab4476b7..5d55ac28d 100644
--- a/go.sum
+++ b/go.sum
@@ -52,12 +52,12 @@ github.com/go-logr/stdr v1.2.2 h1:hSWxHoqTgW2S2qGc0LTAI563KZ5YKYRhT3MFKZMbjag=
 github.com/go-logr/stdr v1.2.2/go.mod h1:mMo/vtBO5dYbehREoey6XUKy/eSumjCCveDpRre4VKE=
 github.com/go-logr/zapr v1.3.0 h1:XGdV8XW8zdwFiwOA2Dryh1gj2KRQyOOoNmBy4EplIcQ=
 github.com/go-logr/zapr v1.3.0/go.mod h1:YKepepNBd1u/oyhd/yQmtjVXmm9uML4IXUgMOwR8/Gg=
-github.com/go-openapi/jsonpointer v0.21.0 h1:YgdVicSA9vH5RiHs9TZW5oyafXZFc6+2Vc1rr/O9oNQ=
-github.com/go-openapi/jsonpointer v0.21.0/go.mod h1:IUyH9l/+uyhIYQ/PXVA41Rexl+kOkAPDdXEYns6fzUY=
+github.com/go-openapi/jsonpointer v0.21.1 h1:whnzv/pNXtK2FbX/W9yJfRmE2gsmkfahjMKB0fZvcic=
+github.com/go-openapi/jsonpointer v0.21.1/go.mod h1:50I1STOfbY1ycR8jGz8DaMeLCdXiI6aDteEdRNNzpdk=
 github.com/go-openapi/jsonreference v0.21.0 h1:Rs+Y7hSXT83Jacb7kFyjn4ijOuVGSvOdF2+tg1TRrwQ=
 github.com/go-openapi/jsonreference v0.21.0/go.mod h1:LmZmgsrTkVg9LG4EaHeY8cBDslNPMo06cago5JNLkm4=
-github.com/go-openapi/swag v0.23.0 h1:vsEVJDUo2hPJ2tu0/Xc+4noaxyEffXNIs3cOULZ+GrE=
-github.com/go-openapi/swag v0.23.0/go.mod h1:esZ8ITTYEsH1V2trKHjAN8Ai7xHb8RV+YSZ577vPjgQ=
+github.com/go-openapi/swag v0.23.1 h1:lpsStH0n2ittzTnbaSloVZLuB5+fvSY/+hnagBjSNZU=
+github.com/go-openapi/swag v0.23.1/go.mod h1:STZs8TbRvEQQKUA+JZNAm3EWlgaOBGpyFDqQnDHMef0=
 github.com/go-task/slim-sprig v0.0.0-20210107165309-348f09dbbbc0/go.mod h1:fyg7847qk6SyHyPtNmDHnmrv/HOrqktSC+C9fM+CJOE=
 github.com/go-task/slim-sprig/v3 v3.0.0 h1:sUs3vkvUymDpBKi3qH1YSqBQk9+9D/8M2mN1vB6EwHI=
... (truncated)
```
- `images/custom-error-pages/rootfs/go.mod` [M]
```diff
diff --git a/images/custom-error-pages/rootfs/go.mod b/images/custom-error-pages/rootfs/go.mod
index 7d2c24fbd..4cb9ca333 100644
--- a/images/custom-error-pages/rootfs/go.mod
+++ b/images/custom-error-pages/rootfs/go.mod
@@ -10,8 +10,8 @@ require (
 	github.com/klauspost/compress v1.18.0 // indirect
 	github.com/munnerz/goautoneg v0.0.0-20191010083416-a7dc8b61c822 // indirect
 	github.com/prometheus/client_model v0.6.1 // indirect
-	github.com/prometheus/common v0.62.0 // indirect
-	github.com/prometheus/procfs v0.15.1 // indirect
+	github.com/prometheus/common v0.63.0 // indirect
+	github.com/prometheus/procfs v0.16.0 // indirect
 	golang.org/x/sys v0.31.0 // indirect
-	google.golang.org/protobuf v1.36.5 // indirect
+	google.golang.org/protobuf v1.36.6 // indirect
 )
```
- `images/custom-error-pages/rootfs/go.sum` [M]
```diff
diff --git a/images/custom-error-pages/rootfs/go.sum b/images/custom-error-pages/rootfs/go.sum
index 0d8cec06c..387ac2742 100644
--- a/images/custom-error-pages/rootfs/go.sum
+++ b/images/custom-error-pages/rootfs/go.sum
@@ -4,8 +4,8 @@ github.com/cespare/xxhash/v2 v2.3.0 h1:UL815xU9SqsFlibzuggzjXhog7bL6oX9BbNZnL2UF
 github.com/cespare/xxhash/v2 v2.3.0/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
 github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
 github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
-github.com/google/go-cmp v0.6.0 h1:ofyhxvXcZhMsU5ulbFiLKl/XBFqE1GSq7atu8tAmTRI=
-github.com/google/go-cmp v0.6.0/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
+github.com/google/go-cmp v0.7.0 h1:wk8382ETsv4JYUZwIsn6YpYiWiBsYLSJiTsyBybVuN8=
+github.com/google/go-cmp v0.7.0/go.mod h1:pXiqmnSA92OHEEa9HXL2W4E7lf9JzCmGVUdgjX3N/iU=
 github.com/klauspost/compress v1.18.0 h1:c/Cqfb0r+Yi+JtIEq73FWXVkRonBlf0CRNYc8Zttxdo=
 github.com/klauspost/compress v1.18.0/go.mod h1:2Pp+KzxcywXVXMr50+X0Q/Lsb43OQHYWRCY2AiWywWQ=
 github.com/kylelemons/godebug v1.1.0 h1:RPNrshWIDI6G2gRW9EHilWtl7Z6Sb1BR0xunSBf0SNc=
@@ -18,15 +18,15 @@ github.com/prometheus/client_golang v1.21.1 h1:DOvXXTqVzvkIewV/CDPFdejpMCGeMcbGC
 github.com/prometheus/client_golang v1.21.1/go.mod h1:U9NM32ykUErtVBxdvD3zfi+EuFkkaBvMb09mIfe0Zgg=
 github.com/prometheus/client_model v0.6.1 h1:ZKSh/rekM+n3CeS952MLRAdFwIKqeY8b62p8ais2e9E=
 github.com/prometheus/client_model v0.6.1/go.mod h1:OrxVMOVHjw3lKMa8+x6HeMGkHMQyHDk9E3jmP2AmGiY=
-github.com/prometheus/common v0.62.0 h1:xasJaQlnWAeyHdUBeGjXmutelfJHWMRr+Fg4QszZ2Io=
... (truncated)
```
- `images/ext-auth-example-authsvc/rootfs/go.mod` [M]
```diff
diff --git a/images/ext-auth-example-authsvc/rootfs/go.mod b/images/ext-auth-example-authsvc/rootfs/go.mod
index 2c494b503..e1ecc0392 100644
--- a/images/ext-auth-example-authsvc/rootfs/go.mod
+++ b/images/ext-auth-example-authsvc/rootfs/go.mod
@@ -1,6 +1,7 @@
 module example.com/authsvc
 
 go 1.24.1
+
 require k8s.io/apimachinery v0.32.3
 
 require github.com/google/uuid v1.6.0 // indirect
```
- `images/kube-webhook-certgen/rootfs/go.mod` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.mod b/images/kube-webhook-certgen/rootfs/go.mod
index 0d6467d6f..2e2f0e411 100644
--- a/images/kube-webhook-certgen/rootfs/go.mod
+++ b/images/kube-webhook-certgen/rootfs/go.mod
@@ -17,9 +17,9 @@ require (
 	github.com/emicklei/go-restful/v3 v3.12.2 // indirect
 	github.com/fxamacker/cbor/v2 v2.7.0 // indirect
 	github.com/go-logr/logr v1.4.2 // indirect
-	github.com/go-openapi/jsonpointer v0.21.0 // indirect
+	github.com/go-openapi/jsonpointer v0.21.1 // indirect
 	github.com/go-openapi/jsonreference v0.21.0 // indirect
-	github.com/go-openapi/swag v0.23.0 // indirect
+	github.com/go-openapi/swag v0.23.1 // indirect
 	github.com/gogo/protobuf v1.3.2 // indirect
 	github.com/golang/protobuf v1.5.4 // indirect
 	github.com/google/gnostic-models v0.6.9 // indirect
@@ -44,13 +44,13 @@ require (
 	golang.org/x/term v0.30.0 // indirect
 	golang.org/x/text v0.23.0 // indirect
 	golang.org/x/time v0.11.0 // indirect
... (truncated)
```
- `images/kube-webhook-certgen/rootfs/go.sum` [M]
```diff
diff --git a/images/kube-webhook-certgen/rootfs/go.sum b/images/kube-webhook-certgen/rootfs/go.sum
index 3fc75b432..2233937b9 100644
--- a/images/kube-webhook-certgen/rootfs/go.sum
+++ b/images/kube-webhook-certgen/rootfs/go.sum
@@ -9,12 +9,12 @@ github.com/fxamacker/cbor/v2 v2.7.0 h1:iM5WgngdRBanHcxugY4JySA0nk1wZorNOpTgCMedv
 github.com/fxamacker/cbor/v2 v2.7.0/go.mod h1:pxXPTn3joSm21Gbwsv0w9OSA2y1HFR9qXEeXQVeNoDQ=
 github.com/go-logr/logr v1.4.2 h1:6pFjapn8bFcIbiKo3XT4j/BhANplGihG6tvd+8rYgrY=
 github.com/go-logr/logr v1.4.2/go.mod h1:9T104GzyrTigFIr8wt5mBrctHMim0Nb2HLGrmQ40KvY=
-github.com/go-openapi/jsonpointer v0.21.0 h1:YgdVicSA9vH5RiHs9TZW5oyafXZFc6+2Vc1rr/O9oNQ=
-github.com/go-openapi/jsonpointer v0.21.0/go.mod h1:IUyH9l/+uyhIYQ/PXVA41Rexl+kOkAPDdXEYns6fzUY=
+github.com/go-openapi/jsonpointer v0.21.1 h1:whnzv/pNXtK2FbX/W9yJfRmE2gsmkfahjMKB0fZvcic=
+github.com/go-openapi/jsonpointer v0.21.1/go.mod h1:50I1STOfbY1ycR8jGz8DaMeLCdXiI6aDteEdRNNzpdk=
 github.com/go-openapi/jsonreference v0.21.0 h1:Rs+Y7hSXT83Jacb7kFyjn4ijOuVGSvOdF2+tg1TRrwQ=
 github.com/go-openapi/jsonreference v0.21.0/go.mod h1:LmZmgsrTkVg9LG4EaHeY8cBDslNPMo06cago5JNLkm4=
-github.com/go-openapi/swag v0.23.0 h1:vsEVJDUo2hPJ2tu0/Xc+4noaxyEffXNIs3cOULZ+GrE=
-github.com/go-openapi/swag v0.23.0/go.mod h1:esZ8ITTYEsH1V2trKHjAN8Ai7xHb8RV+YSZ577vPjgQ=
+github.com/go-openapi/swag v0.23.1 h1:lpsStH0n2ittzTnbaSloVZLuB5+fvSY/+hnagBjSNZU=
+github.com/go-openapi/swag v0.23.1/go.mod h1:STZs8TbRvEQQKUA+JZNAm3EWlgaOBGpyFDqQnDHMef0=
 github.com/go-task/slim-sprig/v3 v3.0.0 h1:sUs3vkvUymDpBKi3qH1YSqBQk9+9D/8M2mN1vB6EwHI=
 github.com/go-task/slim-sprig/v3 v3.0.0/go.mod h1:W848ghGpv3Qj3dhTPRyJypKRiqCdHZiAzKg9hl15HA8=
... (truncated)
```
- `magefiles/go.mod` [M]
```diff
diff --git a/magefiles/go.mod b/magefiles/go.mod
index 3c716cf1a..7c232dada 100644
--- a/magefiles/go.mod
+++ b/magefiles/go.mod
@@ -13,7 +13,7 @@ require (
 )
 
 require (
-	github.com/BurntSushi/toml v1.4.0 // indirect
+	github.com/BurntSushi/toml v1.5.0 // indirect
 	github.com/Masterminds/semver v1.5.0 // indirect
 	github.com/cyphar/filepath-securejoin v0.4.1 // indirect
 	github.com/dprotaso/go-yit v0.0.0-20240618133044-5a0af90af097 // indirect
@@ -27,9 +27,9 @@ require (
 	github.com/sergi/go-diff v1.3.1 // indirect
 	golang.org/x/crypto v0.36.0 // indirect
 	golang.org/x/sys v0.31.0 // indirect
-	google.golang.org/protobuf v1.36.5 // indirect
+	google.golang.org/protobuf v1.36.6 // indirect
 	gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c // indirect
... (truncated)
```
- `magefiles/go.sum` [M]
```diff
diff --git a/magefiles/go.sum b/magefiles/go.sum
index bc5a804a4..b0028616c 100644
--- a/magefiles/go.sum
+++ b/magefiles/go.sum
@@ -1,5 +1,5 @@
-github.com/BurntSushi/toml v1.4.0 h1:kuoIxZQy2WRRk1pttg9asf+WVv6tWQuBNVmK8+nqPr0=
-github.com/BurntSushi/toml v1.4.0/go.mod h1:ukJfTF/6rtPPRCnwkur4qwRxa8vTRFBF0uk2lLoLwho=
+github.com/BurntSushi/toml v1.5.0 h1:W5quZX/G/csjUnuI8SUYlsHs9M38FC7znL0lIO+DvMg=
+github.com/BurntSushi/toml v1.5.0/go.mod h1:ukJfTF/6rtPPRCnwkur4qwRxa8vTRFBF0uk2lLoLwho=
 github.com/Masterminds/semver v1.5.0 h1:H65muMkzWKEuNDnfl9d70GUjFniHKHRbFPGBuZ3QEww=
 github.com/Masterminds/semver v1.5.0/go.mod h1:MB6lktGJrhw8PrUyiEoblNEGEQ+RzHPF078ddwwvV3Y=
 github.com/blang/semver/v4 v4.0.0 h1:1PFHFE6yCCTv8C1TeyNNarDzntLi7wMI5i/pzqYIsAM=
@@ -152,8 +152,8 @@ google.golang.org/protobuf v1.21.0/go.mod h1:47Nbq4nVaFHyn7ilMalzfO3qCViNmqZ2kzi
 google.golang.org/protobuf v1.23.0/go.mod h1:EGpADcykh3NcUnDUJcl1+ZksZNG86OlYog2l/sGQquU=
 google.golang.org/protobuf v1.26.0-rc.1/go.mod h1:jlhhOSvTdKEhbULTjvd4ARK9grFBp09yW+WbY/TyQbw=
 google.golang.org/protobuf v1.26.0/go.mod h1:9q0QmTI4eRPtz6boOQmLYwt+qCgq0jsYwAQnmE0givc=
-google.golang.org/protobuf v1.36.5 h1:tPhr+woSbjfYvY6/GPufUoYizxw1cF/yFoxJ2fmpwlM=
-google.golang.org/protobuf v1.36.5/go.mod h1:9fA7Ob0pmnwhb644+1+CVWFRbNajQ6iRojtC/QF5bRE=
+google.golang.org/protobuf v1.36.6 h1:z1NpPI8ku2WgiWnf+t9wTPsn6eP1L7ksHUlkfLvd9xY=
+google.golang.org/protobuf v1.36.6/go.mod h1:jduwjTPXsFjZGTmRluh+L6NjiWu7pchiJ2/5YcXBHnY=
... (truncated)
```

### 🔸 Commit `aa97baa2d728a001e2c650e620649d27da7a546f` - Images: Trigger NGINX build. (#13040) (2025-03-24) by `Marco Ebert`
- `images/nginx/TAG` [M]
```diff
diff --git a/images/nginx/TAG b/images/nginx/TAG
index 268b0334e..937cd7846 100644
--- a/images/nginx/TAG
+++ b/images/nginx/TAG
@@ -1 +1 @@
-v0.3.0
+v0.3.1
```

### 🔸 Commit `9c32f26cc62e3b13d8e723edca84686f42bd0b9e` - Images: Bump `NGINX_BASE` to v0.3.1. (#13041) (2025-03-24) by `Marco Ebert`
- `NGINX_BASE` [M]
```diff
diff --git a/NGINX_BASE b/NGINX_BASE
index d082857a7..b515713b2 100644
--- a/NGINX_BASE
+++ b/NGINX_BASE
@@ -1 +1 @@
-registry.k8s.io/ingress-nginx/nginx:v0.3.0@sha256:73b4df804b128dc7aed9a769e17e9eaa70304895f26115c3d57e44e08ecc3685
+registry.k8s.io/ingress-nginx/nginx:v0.3.1@sha256:95583e4278a30f52e2690432a6625c9b86a400c780a657bb0a6f170994a10eb4
```

### 🔸 Commit `19cfa1aee6446bfde54dd3e63e6cc275442ff309` - Images: Trigger Test Runner build. (#13046) (2025-03-24) by `Marco Ebert`
- `images/test-runner/TAG` [M]
```diff
diff --git a/images/test-runner/TAG b/images/test-runner/TAG
index 18fa8e74f..757407982 100644
--- a/images/test-runner/TAG
+++ b/images/test-runner/TAG
@@ -1 +1 @@
-v1.3.0
+v1.3.1
```

### 🔸 Commit `6718acf2d27dfa568a0067ca2198fc524ca26acb` - Tests: Bump Test Runner to v1.3.1. (#13049) (2025-03-24) by `Marco Ebert`
- `build/run-in-docker.sh` [M]
```diff
diff --git a/build/run-in-docker.sh b/build/run-in-docker.sh
index 47b49183e..763e55e7c 100755
--- a/build/run-in-docker.sh
+++ b/build/run-in-docker.sh
@@ -41,7 +41,7 @@ function cleanup {
 }
 trap cleanup EXIT
 
-E2E_IMAGE=${E2E_IMAGE:-registry.k8s.io/ingress-nginx/e2e-test-runner:v20250112-01b7af21@sha256:f77bb4625985462fe1a2bc846c430d668113abc90e5e5de6b4533403f56a048c}
+E2E_IMAGE=${E2E_IMAGE:-registry.k8s.io/ingress-nginx/e2e-test-runner:v1.3.1@sha256:e5342d52e2eb6459483b9538b3456d67b3b15e4c55eb9f67993b55ed2ed61901}
 
 if [[ "$RUNTIME" == podman ]]; then
   # Podman does not support both tag and digest
```
- `test/e2e-image/Makefile` [M]
```diff
diff --git a/test/e2e-image/Makefile b/test/e2e-image/Makefile
index 023fe68d3..1b5767ac3 100644
--- a/test/e2e-image/Makefile
+++ b/test/e2e-image/Makefile
@@ -1,6 +1,6 @@
 
 DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
-E2E_BASE_IMAGE ?= "registry.k8s.io/ingress-nginx/e2e-test-runner:v20250112-01b7af21@sha256:f77bb4625985462fe1a2bc846c430d668113abc90e5e5de6b4533403f56a048c"
+E2E_BASE_IMAGE ?= "registry.k8s.io/ingress-nginx/e2e-test-runner:v1.3.1@sha256:e5342d52e2eb6459483b9538b3456d67b3b15e4c55eb9f67993b55ed2ed61901"
 
 image:
 	echo "..entered Makefile in /test/e2e-image"
```
- `test/e2e/run-chart-test.sh` [M]
```diff
diff --git a/test/e2e/run-chart-test.sh b/test/e2e/run-chart-test.sh
index 719d098a0..585a2b69d 100755
--- a/test/e2e/run-chart-test.sh
+++ b/test/e2e/run-chart-test.sh
@@ -114,5 +114,5 @@ docker run \
   --workdir /workdir \
   --entrypoint ct \
   --rm \
-  registry.k8s.io/ingress-nginx/e2e-test-runner:v20250112-01b7af21@sha256:f77bb4625985462fe1a2bc846c430d668113abc90e5e5de6b4533403f56a048c \
+  registry.k8s.io/ingress-nginx/e2e-test-runner:v1.3.1@sha256:e5342d52e2eb6459483b9538b3456d67b3b15e4c55eb9f67993b55ed2ed61901 \
     install --charts charts/ingress-nginx
```

### 🔸 Commit `8bd6f4bf32e7d0b040f80debc66d73414452af3d` - Images: Trigger other builds (1/2). (#13058) (2025-03-24) by `k8s-infra-cherrypick-robot`
- `images/cfssl/TAG` [M]
```diff
diff --git a/images/cfssl/TAG b/images/cfssl/TAG
index 56130fb3a..0f1acbd56 100644
--- a/images/cfssl/TAG
+++ b/images/cfssl/TAG
@@ -1 +1 @@
-v1.1.1
+v1.1.2
```
- `images/custom-error-pages/TAG` [M]
```diff
diff --git a/images/custom-error-pages/TAG b/images/custom-error-pages/TAG
index 56130fb3a..0f1acbd56 100644
--- a/images/custom-error-pages/TAG
+++ b/images/custom-error-pages/TAG
@@ -1 +1 @@
-v1.1.1
+v1.1.2
```
- `images/e2e-test-echo/TAG` [M]
```diff
diff --git a/images/e2e-test-echo/TAG b/images/e2e-test-echo/TAG
index 56130fb3a..0f1acbd56 100644
--- a/images/e2e-test-echo/TAG
+++ b/images/e2e-test-echo/TAG
@@ -1 +1 @@
-v1.1.1
+v1.1.2
```
- `images/ext-auth-example-authsvc/TAG` [M]
```diff
diff --git a/images/ext-auth-example-authsvc/TAG b/images/ext-auth-example-authsvc/TAG
index 56130fb3a..0f1acbd56 100644
--- a/images/ext-auth-example-authsvc/TAG
+++ b/images/ext-auth-example-authsvc/TAG
@@ -1 +1 @@
-v1.1.1
+v1.1.2
```

### 🔸 Commit `4d3318ffd8106f213486e69342f13b5097daa319` - Images: Trigger other builds (2/2). (#13060) (2025-03-24) by `k8s-infra-cherrypick-robot`
- `images/fastcgi-helloserver/TAG` [M]
```diff
diff --git a/images/fastcgi-helloserver/TAG b/images/fastcgi-helloserver/TAG
index 56130fb3a..0f1acbd56 100644
--- a/images/fastcgi-helloserver/TAG
+++ b/images/fastcgi-helloserver/TAG
@@ -1 +1 @@
-v1.1.1
+v1.1.2
```
- `images/go-grpc-greeter-server/TAG` [M]
```diff
diff --git a/images/go-grpc-greeter-server/TAG b/images/go-grpc-greeter-server/TAG
index 56130fb3a..0f1acbd56 100644
--- a/images/go-grpc-greeter-server/TAG
+++ b/images/go-grpc-greeter-server/TAG
@@ -1 +1 @@
-v1.1.1
+v1.1.2
```
- `images/httpbun/TAG` [M]
```diff
diff --git a/images/httpbun/TAG b/images/httpbun/TAG
index 56130fb3a..0f1acbd56 100644
--- a/images/httpbun/TAG
+++ b/images/httpbun/TAG
@@ -1 +1 @@
-v1.1.1
+v1.1.2
```
- `images/kube-webhook-certgen/TAG` [M]
```diff
diff --git a/images/kube-webhook-certgen/TAG b/images/kube-webhook-certgen/TAG
index 53b5bbb12..a503124bd 100644
--- a/images/kube-webhook-certgen/TAG
+++ b/images/kube-webhook-certgen/TAG
@@ -1 +1 @@
-v1.5.1
+v1.5.2
```

### 🔸 Commit `138ade74b4c0e5420025410e0c8207b4b69e180f` - Tests & Docs: Bump images. (#13065) (2025-03-24) by `k8s-infra-cherrypick-robot`
- `docs/examples/canary/README.md` [M]
```diff
diff --git a/docs/examples/canary/README.md b/docs/examples/canary/README.md
index 885991a3b..07f2c41b0 100644
--- a/docs/examples/canary/README.md
+++ b/docs/examples/canary/README.md
@@ -31,7 +31,7 @@ spec:
     spec:
       containers:
       - name: production
-        image: registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.1@sha256:a1e0152e2eeab26e3f6fd3986f3d82b17bc7711717cae5392dcd18dd447ba6ef
+        image: registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.2@sha256:b43ed89fb7ae67c430470d4eb9ea4058c1c74c42b10aa064244eb971b9a370d8
         ports:
         - containerPort: 80
         env:
@@ -97,7 +97,7 @@ spec:
     spec:
       containers:
       - name: canary
-        image: registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.1@sha256:a1e0152e2eeab26e3f6fd3986f3d82b17bc7711717cae5392dcd18dd447ba6ef
+        image: registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.2@sha256:b43ed89fb7ae67c430470d4eb9ea4058c1c74c42b10aa064244eb971b9a370d8
         ports:
... (truncated)
```
- `docs/examples/customization/custom-errors/custom-default-backend.helm.values.yaml` [M]
```diff
diff --git a/docs/examples/customization/custom-errors/custom-default-backend.helm.values.yaml b/docs/examples/customization/custom-errors/custom-default-backend.helm.values.yaml
index d72001d58..cf19fc847 100644
--- a/docs/examples/customization/custom-errors/custom-default-backend.helm.values.yaml
+++ b/docs/examples/customization/custom-errors/custom-default-backend.helm.values.yaml
@@ -6,7 +6,7 @@ defaultBackend:
   image:
     registry: registry.k8s.io
     image: ingress-nginx/custom-error-pages
-    tag: v1.1.1@sha256:8c10776191ae44b5c387b8c7696d8bc17ceec90d7184a3a38b89ac8434b6c56b
+    tag: v1.1.2@sha256:49a5154b3f918aae436ae342ac410a947524f1da8a2f9c249b564a092cf44955
   extraVolumes:
   - name: custom-error-pages
     configMap:
```
- `docs/examples/customization/custom-errors/custom-default-backend.yaml` [M]
```diff
diff --git a/docs/examples/customization/custom-errors/custom-default-backend.yaml b/docs/examples/customization/custom-errors/custom-default-backend.yaml
index 088ca1374..61eb4cf82 100644
--- a/docs/examples/customization/custom-errors/custom-default-backend.yaml
+++ b/docs/examples/customization/custom-errors/custom-default-backend.yaml
@@ -36,7 +36,7 @@ spec:
     spec:
       containers:
       - name: nginx-error-server
-        image: registry.k8s.io/ingress-nginx/custom-error-pages:v1.1.1@sha256:8c10776191ae44b5c387b8c7696d8bc17ceec90d7184a3a38b89ac8434b6c56b
+        image: registry.k8s.io/ingress-nginx/custom-error-pages:v1.1.2@sha256:49a5154b3f918aae436ae342ac410a947524f1da8a2f9c249b564a092cf44955
         ports:
         - containerPort: 8080
         # Setting the environment variable DEBUG we can see the headers sent
```
- `docs/examples/customization/external-auth-headers/echo-service.yaml` [M]
```diff
diff --git a/docs/examples/customization/external-auth-headers/echo-service.yaml b/docs/examples/customization/external-auth-headers/echo-service.yaml
index 10244458d..4c782185d 100644
--- a/docs/examples/customization/external-auth-headers/echo-service.yaml
+++ b/docs/examples/customization/external-auth-headers/echo-service.yaml
@@ -18,7 +18,7 @@ spec:
       terminationGracePeriodSeconds: 60
       containers:
       - name: echo-service
-        image: registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.1@sha256:a1e0152e2eeab26e3f6fd3986f3d82b17bc7711717cae5392dcd18dd447ba6ef
+        image: registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.2@sha256:b43ed89fb7ae67c430470d4eb9ea4058c1c74c42b10aa064244eb971b9a370d8
         ports:
         - containerPort: 8080
         resources:
```
- `test/e2e/HTTPBUN_IMAGE` [M]
```diff
diff --git a/test/e2e/HTTPBUN_IMAGE b/test/e2e/HTTPBUN_IMAGE
index 491b333c7..027851fa2 100644
--- a/test/e2e/HTTPBUN_IMAGE
+++ b/test/e2e/HTTPBUN_IMAGE
@@ -1 +1 @@
-registry.k8s.io/ingress-nginx/httpbun:v1.1.1@sha256:4569515d9b74470c915566a010792e7202b6769443fb1f3bb1b1e87376028634
+registry.k8s.io/ingress-nginx/httpbun:v1.1.2@sha256:b712d92006f36c0e65df64d41dca6b649154ee9f183091955cb9e1e6e3520b12
```
- `test/e2e/framework/deployment.go` [M]
```diff
diff --git a/test/e2e/framework/deployment.go b/test/e2e/framework/deployment.go
index f213e2e98..36c945424 100644
--- a/test/e2e/framework/deployment.go
+++ b/test/e2e/framework/deployment.go
@@ -47,7 +47,7 @@ const NIPService = "external-nip"
 var HTTPBunImage = os.Getenv("HTTPBUN_IMAGE")
 
 // EchoImage is the default image to be used by the echo service
-const EchoImage = "registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.1@sha256:a1e0152e2eeab26e3f6fd3986f3d82b17bc7711717cae5392dcd18dd447ba6ef" //#nosec G101
+const EchoImage = "registry.k8s.io/ingress-nginx/e2e-test-echo:v1.1.2@sha256:b43ed89fb7ae67c430470d4eb9ea4058c1c74c42b10aa064244eb971b9a370d8" //#nosec G101
 
 // TODO: change all Deployment functions to use these options
 // in order to reduce complexity and have a unified API across the
```
- `test/e2e/framework/fastcgi_helloserver.go` [M]
```diff
diff --git a/test/e2e/framework/fastcgi_helloserver.go b/test/e2e/framework/fastcgi_helloserver.go
index c414c4da3..82138c8a7 100644
--- a/test/e2e/framework/fastcgi_helloserver.go
+++ b/test/e2e/framework/fastcgi_helloserver.go
@@ -59,7 +59,7 @@ func (f *Framework) NewNewFastCGIHelloServerDeploymentWithReplicas(replicas int3
 					Containers: []corev1.Container{
 						{
 							Name:  "fastcgi-helloserver",
-							Image: "registry.k8s.io/ingress-nginx/fastcgi-helloserver:v1.1.1@sha256:6af4d8c7745c6727aab759db616a58fd68d784d07ce7a32d1ad149c331fd9a6f",
+							Image: "registry.k8s.io/ingress-nginx/fastcgi-helloserver:v1.1.2@sha256:67133b24b7a9f556aa6977484db5af7e16f6a9509dba757cc2c003834c0af489",
 							Env:   []corev1.EnvVar{},
 							Ports: []corev1.ContainerPort{
 								{
```
- `test/e2e/settings/ocsp/ocsp.go` [M]
```diff
diff --git a/test/e2e/settings/ocsp/ocsp.go b/test/e2e/settings/ocsp/ocsp.go
index 282194bfe..482f552ec 100644
--- a/test/e2e/settings/ocsp/ocsp.go
+++ b/test/e2e/settings/ocsp/ocsp.go
@@ -295,7 +295,7 @@ func ocspserveDeployment(namespace string) (*appsv1.Deployment, *corev1.Service)
 						Containers: []corev1.Container{
 							{
 								Name:  name,
-								Image: "registry.k8s.io/ingress-nginx/cfssl:v1.1.1@sha256:bcd576c6d0a01d4710969195e804c02da62b71b5c35c6816df9b7584d5445437",
+								Image: "registry.k8s.io/ingress-nginx/cfssl:v1.1.2@sha256:fd43e7671a6c0338c0f3fe60866d58baef6baa7c13254d788b7180d215b4d933",
 								Command: []string{
 									"/bin/bash",
 									"-c",
```

### 🔸 Commit `cd854d91e247a5cc1d936404468265d4a7a70fa6` - Chart: Bump Kube Webhook CertGen. (#13067) (2025-03-24) by `Marco Ebert`
- `charts/ingress-nginx/README.md` [M]
```diff
diff --git a/charts/ingress-nginx/README.md b/charts/ingress-nginx/README.md
index de032d5ee..d4372045f 100644
--- a/charts/ingress-nginx/README.md
+++ b/charts/ingress-nginx/README.md
@@ -271,11 +271,11 @@ metadata:
 | controller.admissionWebhooks.namespaceSelector | object | `{}` |  |
 | controller.admissionWebhooks.objectSelector | object | `{}` |  |
 | controller.admissionWebhooks.patch.enabled | bool | `true` |  |
-| controller.admissionWebhooks.patch.image.digest | string | `"sha256:0de05718b59dc33b57ddfb4d8ad5f637cefd13eafdec0e1579d782b3483c27c3"` |  |
+| controller.admissionWebhooks.patch.image.digest | string | `"sha256:e8825994b7a2c7497375a9b945f386506ca6a3eda80b89b74ef2db743f66a5ea"` |  |
 | controller.admissionWebhooks.patch.image.image | string | `"ingress-nginx/kube-webhook-certgen"` |  |
 | controller.admissionWebhooks.patch.image.pullPolicy | string | `"IfNotPresent"` |  |
 | controller.admissionWebhooks.patch.image.registry | string | `"registry.k8s.io"` |  |
-| controller.admissionWebhooks.patch.image.tag | string | `"v1.5.1"` |  |
+| controller.admissionWebhooks.patch.image.tag | string | `"v1.5.2"` |  |
 | controller.admissionWebhooks.patch.labels | object | `{}` | Labels to be added to patch job resources |
 | controller.admissionWebhooks.patch.networkPolicy.enabled | bool | `false` | Enable 'networkPolicy' or not |
 | controller.admissionWebhooks.patch.nodeSelector."kubernetes.io/os" | string | `"linux"` |  |
```
- `charts/ingress-nginx/values.yaml` [M]
```diff
diff --git a/charts/ingress-nginx/values.yaml b/charts/ingress-nginx/values.yaml
index 7d911d90e..76323a0cc 100644
--- a/charts/ingress-nginx/values.yaml
+++ b/charts/ingress-nginx/values.yaml
@@ -808,8 +808,8 @@ controller:
         ## for backwards compatibility consider setting the full image url via the repository value below
         ## use *either* current default registry/image or repository format or installing chart by providing the values.yaml will fail
         ## repository:
-        tag: v1.5.1
-        digest: sha256:0de05718b59dc33b57ddfb4d8ad5f637cefd13eafdec0e1579d782b3483c27c3
+        tag: v1.5.2
+        digest: sha256:e8825994b7a2c7497375a9b945f386506ca6a3eda80b89b74ef2db743f66a5ea
         pullPolicy: IfNotPresent
       # -- Provide a priority class name to the webhook patching job
       ##
```

### 🔸 Commit `e6716b13f237fb42a05117784fdee004e74fc801` - Controller: Several security fixes. (#13070) (2025-03-25) by `Marco Ebert`
- `internal/ingress/annotations/auth/main.go` [M]
```diff
diff --git a/internal/ingress/annotations/auth/main.go b/internal/ingress/annotations/auth/main.go
index 7c7fde7b8..79e3ce5d3 100644
--- a/internal/ingress/annotations/auth/main.go
+++ b/internal/ingress/annotations/auth/main.go
@@ -19,6 +19,7 @@ package auth
 import (
 	"fmt"
 	"os"
+	"path/filepath"
 	"regexp"
 	"strings"
 
@@ -203,16 +204,24 @@ func (a auth) Parse(ing *networking.Ingress) (interface{}, error) {
 		return nil, err
 	}
 
-	passFilename := fmt.Sprintf("%v/%v-%v-%v.passwd", a.authDirectory, ing.GetNamespace(), ing.UID, secret.UID)
+	passFileName := fmt.Sprintf("%v-%v-%v.passwd", ing.GetNamespace(), ing.UID, secret.UID)
+	passFilePath := filepath.Join(a.authDirectory, passFileName)
+
... (truncated)
```
- `internal/ingress/controller/controller.go` [M]
```diff
diff --git a/internal/ingress/controller/controller.go b/internal/ingress/controller/controller.go
index 9250ded08..cb4408d98 100644
--- a/internal/ingress/controller/controller.go
+++ b/internal/ingress/controller/controller.go
@@ -421,11 +421,15 @@ func (n *NGINXController) CheckIngress(ing *networking.Ingress) error {
 		return err
 	}
 
+	/* Deactivated to mitigate CVE-2025-1974
+	// TODO: Implement sandboxing so this test can be done safely
 	err = n.testTemplate(content)
 	if err != nil {
 		n.metricCollector.IncCheckErrorCount(ing.ObjectMeta.Namespace, ing.Name)
 		return err
 	}
+	*/
+
 	n.metricCollector.IncCheckCount(ing.ObjectMeta.Namespace, ing.Name)
 	endCheck := time.Now().UnixNano() / 1000000
 	n.metricCollector.SetAdmissionMetrics(
```
- `internal/ingress/controller/controller_test.go` [M]
```diff
diff --git a/internal/ingress/controller/controller_test.go b/internal/ingress/controller/controller_test.go
index 9d3fea470..3b7a3c4eb 100644
--- a/internal/ingress/controller/controller_test.go
+++ b/internal/ingress/controller/controller_test.go
@@ -250,6 +250,8 @@ func TestCheckIngress(t *testing.T) {
 			}
 		})
 
+		/* Deactivated to mitigate CVE-2025-1974
+		// TODO: Implement sandboxing so this test can be done safely
 		t.Run("When nginx test returns an error", func(t *testing.T) {
 			nginx.command = testNginxTestCommand{
 				t:        t,
@@ -261,6 +263,7 @@ func TestCheckIngress(t *testing.T) {
 				t.Errorf("with a new ingress with an error, an error should be returned")
 			}
 		})
+		*/
 
 		t.Run("When the default annotation prefix is used despite an override", func(t *testing.T) {
... (truncated)
```
- `internal/ingress/controller/template/template.go` [M]
```diff
diff --git a/internal/ingress/controller/template/template.go b/internal/ingress/controller/template/template.go
index 8628f8090..ca68bdbbb 100644
--- a/internal/ingress/controller/template/template.go
+++ b/internal/ingress/controller/template/template.go
@@ -1645,11 +1645,11 @@ func buildMirrorLocations(locs []*ingress.Location) string {
 		mapped.Insert(loc.Mirror.Source)
 		buffer.WriteString(fmt.Sprintf(`location = %v {
 internal;
-proxy_set_header Host "%v";
-proxy_pass "%v";
+proxy_set_header Host %v;
+proxy_pass %v;
 }
 
-`, loc.Mirror.Source, loc.Mirror.Host, loc.Mirror.Target))
+`, strconv.Quote(loc.Mirror.Source), strconv.Quote(loc.Mirror.Host), strconv.Quote(loc.Mirror.Target)))
 	}
 
 	return buffer.String()
```
- `rootfs/etc/nginx/template/nginx.tmpl` [M]
```diff
diff --git a/rootfs/etc/nginx/template/nginx.tmpl b/rootfs/etc/nginx/template/nginx.tmpl
index 93a04e3e6..242397531 100644
--- a/rootfs/etc/nginx/template/nginx.tmpl
+++ b/rootfs/etc/nginx/template/nginx.tmpl
@@ -1013,7 +1013,7 @@ stream {
 
         {{ if not ( empty $server.CertificateAuth.MatchCN ) }}
         {{ if gt (len $server.CertificateAuth.MatchCN) 0 }}
-        if ( $ssl_client_s_dn !~ {{ $server.CertificateAuth.MatchCN }} ) {
+        if ( $ssl_client_s_dn !~ {{ $server.CertificateAuth.MatchCN | quote }} ) {
             return 403 "client certificate unauthorized";
         }
         {{ end }}
@@ -1219,7 +1219,7 @@ stream {
             set $target {{ changeHostPort $externalAuth.URL $authUpstreamName }};
             {{ else }}
             proxy_http_version {{ $location.Proxy.ProxyHTTPVersion }};
-            set $target {{ $externalAuth.URL }};
+            set $target {{ $externalAuth.URL | quote }};
             {{ end }}
... (truncated)
```
- `test/e2e/admission/admission.go` [M]
```diff
diff --git a/test/e2e/admission/admission.go b/test/e2e/admission/admission.go
index c41105e2d..e7c0fbef6 100644
--- a/test/e2e/admission/admission.go
+++ b/test/e2e/admission/admission.go
@@ -26,7 +26,6 @@ import (
 
 	"github.com/onsi/ginkgo/v2"
 	"github.com/stretchr/testify/assert"
-	apierrors "k8s.io/apimachinery/pkg/api/errors"
 	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
 
 	"k8s.io/ingress-nginx/test/e2e/framework"
@@ -126,6 +125,8 @@ var _ = framework.IngressNginxDescribeSerial("[Admission] admission controller",
 		assert.NotNil(ginkgo.GinkgoT(), err, "creating an ingress with invalid path should return an error")
 	})
 
+	/* Deactivated to mitigate CVE-2025-1974
+	// TODO: Implement sandboxing so this test can be done safely
 	ginkgo.It("should return an error if there is an error validating the ingress definition", func() {
 		f.SetNginxConfigMapData(map[string]string{
... (truncated)
```
- `test/e2e/annotations/mirror.go` [M]
```diff
diff --git a/test/e2e/annotations/mirror.go b/test/e2e/annotations/mirror.go
index 787cbfa3b..a398a21e3 100644
--- a/test/e2e/annotations/mirror.go
+++ b/test/e2e/annotations/mirror.go
@@ -43,7 +43,7 @@ var _ = framework.DescribeAnnotation("mirror-*", func() {
 
 		f.WaitForNginxServer(host,
 			func(server string) bool {
-				return strings.Contains(server, fmt.Sprintf("mirror /_mirror-%v;", ing.UID)) &&
+				return strings.Contains(server, fmt.Sprintf("mirror \"/_mirror-%v\";", ing.UID)) &&
 					strings.Contains(server, "mirror_request_body on;")
 			})
 	})
@@ -58,7 +58,7 @@ var _ = framework.DescribeAnnotation("mirror-*", func() {
 
 		f.WaitForNginxServer(host,
 			func(server string) bool {
-				return strings.Contains(server, fmt.Sprintf("mirror /_mirror-%v;", ing.UID)) &&
+				return strings.Contains(server, fmt.Sprintf("mirror \"/_mirror-%v\";", ing.UID)) &&
 					strings.Contains(server, "mirror_request_body on;") &&
... (truncated)
```

### 🔸 Commit `97ffeeee0fabd4b1c6b1cdabeaed881faab612de` - Images: Trigger controller build. (#13072) (2025-03-25) by `Marco Ebert`
- `TAG` [M]
```diff
diff --git a/TAG b/TAG
index f5f1545d8..62e1a5028 100644
--- a/TAG
+++ b/TAG
@@ -1 +1 @@
-v1.11.4
+v1.11.5
```

### 🔸 Commit `795b6964d3cbcdebf5c857faca12750d76158920` - Release controller v1.11.5 & chart v4.11.5. (#13074) (2025-03-25) by `Marco Ebert`
- `README.md` [M]
```diff
diff --git a/README.md b/README.md
index 0dea68548..b59f11db7 100644
--- a/README.md
+++ b/README.md
@@ -39,6 +39,7 @@ the versions listed. Ingress-Nginx versions **may** work on older versions, but
 
 | Supported | Ingress-NGINX version | k8s supported version         | Alpine Version | Nginx Version | Helm Chart Version |
 | :-------: | --------------------- | ----------------------------- | -------------- | ------------- | ------------------ |
+|    🔄     | **v1.11.5**           | 1.30, 1.29, 1.28, 1.27, 1.26  | 3.21.3         | 1.25.5        | 4.11.5             |
 |    🔄     | **v1.11.4**           | 1.30, 1.29, 1.28, 1.27, 1.26  | 3.21.0         | 1.25.5        | 4.11.4             |
 |    🔄     | **v1.11.3**           | 1.30, 1.29, 1.28, 1.27, 1.26  | 3.20.3         | 1.25.5        | 4.11.3             |
 |    🔄     | **v1.11.2**           | 1.30, 1.29, 1.28, 1.27, 1.26  | 3.20.0         | 1.25.5        | 4.11.2             |
```
- `changelog/controller-1.11.5.md` [A]
```diff
diff --git a/changelog/controller-1.11.5.md b/changelog/controller-1.11.5.md
new file mode 100644
index 000000000..9c1fcbf3b
--- /dev/null
+++ b/changelog/controller-1.11.5.md
@@ -0,0 +1,115 @@
+# Changelog
+
+### controller-v1.11.5
+
+Images:
+
+* registry.k8s.io/ingress-nginx/controller:v1.11.5@sha256:a1cbad75b0a7098bf9325132794dddf9eef917e8a7fe246749a4cea7ff6f01eb
+* registry.k8s.io/ingress-nginx/controller-chroot:v1.11.5@sha256:ec9df3eb6b06563a079ee46045da94cbf750f7dbb16fdbcb9e3265b551ed72ad
+
+### All changes:
+
+* Images: Trigger controller build. (#13072)
+* Controller: Several security fixes. (#13070)
+* Chart: Bump Kube Webhook CertGen. (#13067)
... (truncated)
```
- `charts/ingress-nginx/Chart.yaml` [M]
```diff
diff --git a/charts/ingress-nginx/Chart.yaml b/charts/ingress-nginx/Chart.yaml
index 300330c92..39142ef4d 100644
--- a/charts/ingress-nginx/Chart.yaml
+++ b/charts/ingress-nginx/Chart.yaml
@@ -1,10 +1,9 @@
 annotations:
   artifacthub.io/changes: |
-    - 'CI: Fix chart testing. (#12259)'
-    - Update Ingress-Nginx version controller-v1.11.4
+    - Update Ingress-Nginx version controller-v1.11.5
   artifacthub.io/prerelease: "false"
 apiVersion: v2
-appVersion: 1.11.4
+appVersion: 1.11.5
 description: Ingress controller for Kubernetes using NGINX as a reverse proxy and
   load balancer
 home: https://github.com/kubernetes/ingress-nginx
@@ -21,4 +20,4 @@ maintainers:
 name: ingress-nginx
 sources:
... (truncated)
```
- `charts/ingress-nginx/README.md` [M]
```diff
diff --git a/charts/ingress-nginx/README.md b/charts/ingress-nginx/README.md
index d4372045f..d36a564ca 100644
--- a/charts/ingress-nginx/README.md
+++ b/charts/ingress-nginx/README.md
@@ -2,7 +2,7 @@
 
 [ingress-nginx](https://github.com/kubernetes/ingress-nginx) Ingress controller for Kubernetes using NGINX as a reverse proxy and load balancer
 
-![Version: 4.11.4](https://img.shields.io/badge/Version-4.11.4-informational?style=flat-square) ![AppVersion: 1.11.4](https://img.shields.io/badge/AppVersion-1.11.4-informational?style=flat-square)
+![Version: 4.11.5](https://img.shields.io/badge/Version-4.11.5-informational?style=flat-square) ![AppVersion: 1.11.5](https://img.shields.io/badge/AppVersion-1.11.5-informational?style=flat-square)
 
 To use, add `ingressClassName: nginx` spec field or the `kubernetes.io/ingress.class: nginx` annotation to your Ingress resources.
 
@@ -343,8 +343,8 @@ metadata:
 | controller.hostname | object | `{}` | Optionally customize the pod hostname. |
 | controller.image.allowPrivilegeEscalation | bool | `false` |  |
 | controller.image.chroot | bool | `false` |  |
-| controller.image.digest | string | `"sha256:981a97d78bee3109c0b149946c07989f8f1478a9265031d2d23dea839ba05b52"` |  |
-| controller.image.digestChroot | string | `"sha256:f29d0f9e7a9ef4947eda59ed0c09ec13380b13639d1518cf1ab8ec09c3e22ef8"` |  |
+| controller.image.digest | string | `"sha256:a1cbad75b0a7098bf9325132794dddf9eef917e8a7fe246749a4cea7ff6f01eb"` |  |
... (truncated)
```
- `charts/ingress-nginx/changelog/helm-chart-4.11.5.md` [A]
```diff
diff --git a/charts/ingress-nginx/changelog/helm-chart-4.11.5.md b/charts/ingress-nginx/changelog/helm-chart-4.11.5.md
new file mode 100644
index 000000000..70a39a26c
--- /dev/null
+++ b/charts/ingress-nginx/changelog/helm-chart-4.11.5.md
@@ -0,0 +1,9 @@
+# Changelog
+
+This file documents all notable changes to [ingress-nginx](https://github.com/kubernetes/ingress-nginx) Helm Chart. The release numbering uses [semantic versioning](http://semver.org).
+
+### 4.11.5
+
+* Update Ingress-Nginx version controller-v1.11.5
+
+**Full Changelog**: https://github.com/kubernetes/ingress-nginx/compare/helm-chart-4.11.4...helm-chart-4.11.5
```
- `charts/ingress-nginx/values.yaml` [M]
```diff
diff --git a/charts/ingress-nginx/values.yaml b/charts/ingress-nginx/values.yaml
index 76323a0cc..1c9f1c587 100644
--- a/charts/ingress-nginx/values.yaml
+++ b/charts/ingress-nginx/values.yaml
@@ -26,9 +26,9 @@ controller:
     ## for backwards compatibility consider setting the full image url via the repository value below
     ## use *either* current default registry/image or repository format or installing chart by providing the values.yaml will fail
     ## repository:
-    tag: "v1.11.4"
-    digest: sha256:981a97d78bee3109c0b149946c07989f8f1478a9265031d2d23dea839ba05b52
-    digestChroot: sha256:f29d0f9e7a9ef4947eda59ed0c09ec13380b13639d1518cf1ab8ec09c3e22ef8
+    tag: "v1.11.5"
+    digest: sha256:a1cbad75b0a7098bf9325132794dddf9eef917e8a7fe246749a4cea7ff6f01eb
+    digestChroot: sha256:ec9df3eb6b06563a079ee46045da94cbf750f7dbb16fdbcb9e3265b551ed72ad
     pullPolicy: IfNotPresent
     runAsNonRoot: true
     # www-data -> uid 101
```
- `deploy/static/provider/aws/deploy.yaml` [M]
```diff
diff --git a/deploy/static/provider/aws/deploy.yaml b/deploy/static/provider/aws/deploy.yaml
index 88d3226c6..0a2f3ac5f 100644
--- a/deploy/static/provider/aws/deploy.yaml
+++ b/deploy/static/provider/aws/deploy.yaml
@@ -15,7 +15,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx
   namespace: ingress-nginx
 ---
@@ -28,7 +28,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx-admission
... (truncated)
```
- `deploy/static/provider/aws/nlb-with-tls-termination/deploy.yaml` [M]
```diff
diff --git a/deploy/static/provider/aws/nlb-with-tls-termination/deploy.yaml b/deploy/static/provider/aws/nlb-with-tls-termination/deploy.yaml
index 3463fe2d9..ecbe42ffe 100644
--- a/deploy/static/provider/aws/nlb-with-tls-termination/deploy.yaml
+++ b/deploy/static/provider/aws/nlb-with-tls-termination/deploy.yaml
@@ -15,7 +15,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx
   namespace: ingress-nginx
 ---
@@ -28,7 +28,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx-admission
... (truncated)
```
- `deploy/static/provider/baremetal/deploy.yaml` [M]
```diff
diff --git a/deploy/static/provider/baremetal/deploy.yaml b/deploy/static/provider/baremetal/deploy.yaml
index 720788035..a822e82ea 100644
--- a/deploy/static/provider/baremetal/deploy.yaml
+++ b/deploy/static/provider/baremetal/deploy.yaml
@@ -15,7 +15,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx
   namespace: ingress-nginx
 ---
@@ -28,7 +28,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx-admission
... (truncated)
```
- `deploy/static/provider/cloud/deploy.yaml` [M]
```diff
diff --git a/deploy/static/provider/cloud/deploy.yaml b/deploy/static/provider/cloud/deploy.yaml
index 1a3c18a6c..88df84bf5 100644
--- a/deploy/static/provider/cloud/deploy.yaml
+++ b/deploy/static/provider/cloud/deploy.yaml
@@ -15,7 +15,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx
   namespace: ingress-nginx
 ---
@@ -28,7 +28,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx-admission
... (truncated)
```
- `deploy/static/provider/do/deploy.yaml` [M]
```diff
diff --git a/deploy/static/provider/do/deploy.yaml b/deploy/static/provider/do/deploy.yaml
index 1c2e5da6a..cc5756524 100644
--- a/deploy/static/provider/do/deploy.yaml
+++ b/deploy/static/provider/do/deploy.yaml
@@ -15,7 +15,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx
   namespace: ingress-nginx
 ---
@@ -28,7 +28,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx-admission
... (truncated)
```
- `deploy/static/provider/exoscale/deploy.yaml` [M]
```diff
diff --git a/deploy/static/provider/exoscale/deploy.yaml b/deploy/static/provider/exoscale/deploy.yaml
index c7e912955..958e829d1 100644
--- a/deploy/static/provider/exoscale/deploy.yaml
+++ b/deploy/static/provider/exoscale/deploy.yaml
@@ -15,7 +15,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx
   namespace: ingress-nginx
 ---
@@ -28,7 +28,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx-admission
... (truncated)
```
- `deploy/static/provider/kind/deploy.yaml` [M]
```diff
diff --git a/deploy/static/provider/kind/deploy.yaml b/deploy/static/provider/kind/deploy.yaml
index e40f95391..4b0a37e7a 100644
--- a/deploy/static/provider/kind/deploy.yaml
+++ b/deploy/static/provider/kind/deploy.yaml
@@ -15,7 +15,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx
   namespace: ingress-nginx
 ---
@@ -28,7 +28,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx-admission
... (truncated)
```
- `deploy/static/provider/oracle/deploy.yaml` [M]
```diff
diff --git a/deploy/static/provider/oracle/deploy.yaml b/deploy/static/provider/oracle/deploy.yaml
index 2fb1ff0ab..914ffb3d9 100644
--- a/deploy/static/provider/oracle/deploy.yaml
+++ b/deploy/static/provider/oracle/deploy.yaml
@@ -15,7 +15,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx
   namespace: ingress-nginx
 ---
@@ -28,7 +28,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx-admission
... (truncated)
```
- `deploy/static/provider/scw/deploy.yaml` [M]
```diff
diff --git a/deploy/static/provider/scw/deploy.yaml b/deploy/static/provider/scw/deploy.yaml
index 2a4dca406..407a56e52 100644
--- a/deploy/static/provider/scw/deploy.yaml
+++ b/deploy/static/provider/scw/deploy.yaml
@@ -15,7 +15,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx
   namespace: ingress-nginx
 ---
@@ -28,7 +28,7 @@ metadata:
     app.kubernetes.io/instance: ingress-nginx
     app.kubernetes.io/name: ingress-nginx
     app.kubernetes.io/part-of: ingress-nginx
-    app.kubernetes.io/version: 1.11.4
+    app.kubernetes.io/version: 1.11.5
   name: ingress-nginx-admission
... (truncated)
```
- `docs/deploy/index.md` [M]
```diff
diff --git a/docs/deploy/index.md b/docs/deploy/index.md
index f74a06bf4..21984dd0a 100644
--- a/docs/deploy/index.md
+++ b/docs/deploy/index.md
@@ -92,7 +92,7 @@ helm show values ingress-nginx --repo https://kubernetes.github.io/ingress-nginx
 **If you don't have Helm** or if you prefer to use a YAML manifest, you can run the following command instead:
 
 ```console
-kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.11.4/deploy/static/provider/cloud/deploy.yaml
+kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.11.5/deploy/static/provider/cloud/deploy.yaml
 ```
 
 !!! info
@@ -274,7 +274,7 @@ In AWS, we use a Network load balancer (NLB) to expose the Ingress-Nginx Control
 ##### Network Load Balancer (NLB)
 
 ```console
-kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.11.4/deploy/static/provider/aws/deploy.yaml
+kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.11.5/deploy/static/provider/aws/deploy.yaml
 ```
... (truncated)
```
- `docs/e2e-tests.md` [M]
```diff
diff --git a/docs/e2e-tests.md b/docs/e2e-tests.md
index 8a2e80b22..473f39594 100644
--- a/docs/e2e-tests.md
+++ b/docs/e2e-tests.md
@@ -6,19 +6,19 @@ Do not try to edit it manually.
 # e2e test suite for [Ingress NGINX Controller](https://github.com/kubernetes/ingress-nginx/tree/main/)
 
 
-### [[Admission] admission controller](https://github.com/kubernetes/ingress-nginx/tree/main//test/e2e/admission/admission.go#L39)
-- [reject ingress with global-rate-limit annotations when memcached is not configured](https://github.com/kubernetes/ingress-nginx/tree/main//test/e2e/admission/admission.go#L47)
-- [should not allow overlaps of host and paths without canary annotations](https://github.com/kubernetes/ingress-nginx/tree/main//test/e2e/admission/admission.go#L74)
-- [should allow overlaps of host and paths with canary annotation](https://github.com/kubernetes/ingress-nginx/tree/main//test/e2e/admission/admission.go#L91)
-- [should block ingress with invalid path](https://github.com/kubernetes/ingress-nginx/tree/main//test/e2e/admission/admission.go#L112)
-- [should return an error if there is an error validating the ingress definition](https://github.com/kubernetes/ingress-nginx/tree/main//test/e2e/admission/admission.go#L129)
-- [should return an error if there is an invalid value in some annotation](https://github.com/kubernetes/ingress-nginx/tree/main//test/e2e/admission/admission.go#L149)
-- [should return an error if there is a forbidden value in some annotation](https://github.com/kubernetes/ingress-nginx/tree/main//test/e2e/admission/admission.go#L163)
-- [should return an error if there is an invalid path and wrong pathType is set](https://github.com/kubernetes/ingress-nginx/tree/main//test/e2e/admission/admission.go#L177)
-- [should not return an error if the Ingress V1 definition is valid with Ingress Class](https://github.com/kubernetes/ingress-nginx/tree/main//test/e2e/admission/admission.go#L211)
-- [should not return an error if the Ingress V1 definition is valid with IngressClass annotation](https://github.com/kubernetes/ingress-nginx/tree/main//test/e2e/admission/admission.go#L227)
-- [should return an error if the Ingress V1 definition contains invalid annotations](https://github.com/kubernetes/ingress-nginx/tree/main//test/e2e/admission/admission.go#L243)
... (truncated)
```


✅ End of Report
