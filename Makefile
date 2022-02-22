APP_VERSION    = $(shell cat VERSION)
IMAGE_NAME     = "dialect-map-public-api"
SOURCE_FOLDER  = "src"
TESTS_PARAMS   = "-p no:cacheprovider"

GCP_PROJECT   ?= "ds3-dialect-map"
GCP_REGISTRY  ?= "us.gcr.io"
GCP_IMAGE_NAME = $(GCP_REGISTRY)/$(GCP_PROJECT)/$(IMAGE_NAME)

export DOCKER_BUILDKIT = 1


.PHONY: build
build:
	@echo "Building Docker image"
	@docker build . --ssh default --tag $(IMAGE_NAME):$(APP_VERSION)


.PHONY: check
check:
	@echo "Checking code format"
	@black --check $(SOURCE_FOLDER)
	@echo "Checking type annotations"
	@mypy $(SOURCE_FOLDER)


.PHONY: install-dev
install-dev:
	@echo "Installing Development packages"
	@pip install -r reqs/requirements-all.txt
	@pre-commit install


.PHONY: push
push: build
	@echo "Pushing Docker image to GCP"
	@docker tag $(IMAGE_NAME):$(APP_VERSION) $(GCP_IMAGE_NAME):$(APP_VERSION)
	@docker push $(GCP_IMAGE_NAME):$(APP_VERSION)
	@docker rmi $(GCP_IMAGE_NAME):$(APP_VERSION)


.PHONY: test
test:
	@echo "Testing code"
	@pytest "$(TESTS_PARAMS)"
