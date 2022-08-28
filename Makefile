PROJECT_NAME = $(shell pwd | rev | cut -f1 -d'/' - | rev')
AWS_ACCOUNT_ID = $(shell aws sts get-caller-identity --query --output text)
CURRENT_VERSION = $(shell aws ecr describe-images --repository-name $(PROJECT_NAME) \
		-- region us-east-1 \
		-- query 'sort_by(imageDetails,& imagePushAt)[-1].imageTags' \
		| grep -Eo '[0-9]{1,4}'| sort -rn | head -1)
NEW_VERSION = $(shell expr $(CURRENT_VERSION) + 1)

update-precommit:
	poetry run pre-commit autoupdate

lint:
	poetry run pre-commit install && poetry run pre-commit run -a -v

test:
	poetry run pytest apps/tests/
