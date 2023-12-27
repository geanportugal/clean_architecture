NEXT_ID=`ls alembic/versions/* | grep -P '/revision_\d{4}.*\.py$' | wc -l`
alembic revision --rev-id=`printf "%04d" ${NEXT_ID}` --autogenerate