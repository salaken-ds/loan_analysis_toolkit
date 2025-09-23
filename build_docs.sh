jupyter-book build notebook/ --builder html --path-output docs
jupyter-book clean notebook/
cp -r notebook/_build/html/* docs/
rm -rf docs/_build
git add .
git commit -m "Updated docs"
git push origin master