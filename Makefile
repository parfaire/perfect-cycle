run:
	uvicorn perfect_cycle.view:app --reload

test:
	pytest