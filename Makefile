.PHONY: build-bindings
build-bindings: ## Builds the C bindings ands makes them available to the package
	cd uplink-c && make build
	cp uplink-c/.build/libuplink.so src/storj_uplink/

