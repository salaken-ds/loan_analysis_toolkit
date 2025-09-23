jupyter-book build notebook/ --builder html --path-output docs
cp -r docs/_build/html/* docs/
rm -rf docs/_build/
git add .
git commit -m "Updated docs"
git push origin master