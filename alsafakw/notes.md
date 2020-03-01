```
npm install webpack --save-dev
```
> --save-dev means packages to use on development dependencies not on production level

```
```
npm install webpack-cli --save-dev

npm install webpack-dev-server --save-dev
```
> contains packages like hot-reloading compile sass files and so on.

npm install @fortawesome/fontawesome-free --save-dev
npx webpack --config webpack.config.js

npm install fibers --save-dev

npm install sass --save-dev

npm install sass-loader node-sass css-loader auto-prefixer postcss-loader   --save-dev
> to auto relaod sass and fetch into css and so

npm install mini-css-extract-plugin --save-dev
> to extract css as a regular file and minify it

npm install bootstrap

npm install --save jquery popper.js
> we are not using dev here because it's a production files

npm install file-loader --save-dev

project folder
--------------
├── node_modules/
├── src
|   ├── dist
│   │   ├── css/
│   │   ├── fonts/
│   │   ├── index.html
│   │   └── js/
│   ├── js
│   │   ├── app.js
│   │   └── custom.js
│   └── scss
│       ├── app
│       │   ├── components
│       │   ├── _customize-bootstrap.scss
│       │   ├── pages
│       │   ├── _vars.scss
│       │   └── vendors
│       └── main.scss
├── package.json
├── package-lock.json
└── webpack.config.js