'use strict';
const MANIFEST = 'flutter-app-manifest';
const TEMP = 'flutter-temp-cache';
const CACHE_NAME = 'flutter-app-cache';

const RESOURCES = {"flutter_bootstrap.js": "896d22ee31297e3408830c34a6b7a5e4",
"README%20copy.md": "992549d73ed5dfd04d092eb5d12978ae",
"version.json": "1aabc1f97df788e21f1390402c739778",
"index.html": "7a98e6fc3c1980ae55165e8642c341fa",
"/": "7a98e6fc3c1980ae55165e8642c341fa",
"main.dart.js": "af180ae6e2710e3c257fa104e2890906",
"flutter.js": "888483df48293866f9f41d3d9274a779",
"README.md": "992549d73ed5dfd04d092eb5d12978ae",
"manifest.json": "a20d746752bbc844e8c1e0a95e39c91d",
".git/AUTO_MERGE": "701acb38c1786f365c66ced6736fa614",
".git/REBASE_HEAD": "8d1b5caa9a4048bd67269e5d96c695f4",
".git/ORIG_HEAD": "1c5f29f77e7aad37e0acddb794e8c8a0",
".git/config": "2a8932dd16a7784882f75ae0d63086fd",
".git/objects/61/419b7049948b281fe9676081a6d563cfebb396": "6560aa199cbc49e1d28f5fce786ff2fa",
".git/objects/59/8b2f9b3b3869aaa7fe3d32dc2250d5c0fa1c93": "ebb4af936cbb671634fdfe66f7b94018",
".git/objects/59/14739a3431810a93b12f5891d0fc1ecfba085c": "759c7caa169404b66cf4bfe178574037",
".git/objects/92/1040e02c54202f1f62db8198017b94d0bf34d8": "547d69e7cf8362825c9620fd48029cc4",
".git/objects/0c/791dfdde83a52d2eb3eccf4ce20ac35e8ada1e": "3b6cc037e8bf21f4b557a264027a9b81",
".git/objects/50/fddbcd58ac996245417d975d2c381ddecf2714": "c43194e6d36f3c71265e650d031f6cfd",
".git/objects/57/63c3d078d993069d614298436a0a579af4d105": "755b769b2633123e07860b95af366559",
".git/objects/9b/3ef5f169177a64f91eafe11e52b58c60db3df2": "6f7adccbcd8159696c9843a547f82033",
".git/objects/9b/271136565fdf71eccc77b279d70218849bfed0": "7678190c688aa23cbe337847cb9ccb8d",
".git/objects/9e/3b4630b3b8461ff43c272714e00bb47942263e": "2cfcd8c860f921fceab454ee54abae46",
".git/objects/56/f4f50d2a5914c0a4e7c17121ec32c89a875c29": "b57922ed400d03db4417d57da4d22afa",
".git/objects/0b/a7ae0e995c9808d36b291b55814636187d2c10": "c174645cf010ad9e21599e11ac353f00",
".git/objects/0b/b1dd73667332a8227b2d0e38c9b338586010c6": "5c17e3f50198d9087ab3b42d09b34880",
".git/objects/9d/736eab770bfe85d26b0079cd59c28e68d7a185": "c53fea9c374cc73791ef1c160831b624",
".git/objects/b2/64575a5d1e13797692af70b4190a8fa9140ded": "568ba975795ec08782f33679b1acc662",
".git/objects/d0/e665e985b0c0e64b787c45585390deacb11279": "1b2d27099cbac80291e29ebd351f44b4",
".git/objects/da/0d5aa44a8c93eda469f7a99ed8feac32d5b19d": "7815e5e63c9760a611e45b802d701cb4",
".git/objects/ae/757857f33fe2e7bc8d6ab8470ce9421a81898e": "da8e69549f07763b86e4ff7ccfc43982",
".git/objects/d8/8128adaad90d2fd7cdabe7b36eaaaed0d3a25b": "2e169ce78040a612b123be7b4b3c1f2f",
".git/objects/ab/0aa35702bc6aa0d1cb399caaa82784cefdde56": "56609b018c20d77525b8a9e303325861",
".git/objects/eb/5b999a36ab5cf35cde5222b946f63d53b063d2": "cf945e02d8ccd4998f4a043d2dc49ccb",
".git/objects/f2/04823a42f2d890f945f70d88b8e2d921c6ae26": "a3bcb2075c8ac99bd68c577183925bd2",
".git/objects/f5/e791e97d451e9eed8e1b0c5b4fa7ca9cc0e385": "0811219975be388964cacd5d78964e52",
".git/objects/ca/3bba02c77c467ef18cffe2d4c857e003ad6d5d": "c454afab7281e6f0a346fe1131741cca",
".git/objects/fe/3b987e61ed346808d9aa023ce3073530ad7426": "8ca829b0b36b29e4be13297797866b8d",
".git/objects/c8/6490a2540186e1fe04e4acbc880756d294b995": "675d7989e7f5c93e76b619f6baf4cc1f",
".git/objects/fb/96aba7265c577dd75350d0b29a991a366e7db4": "55dcc20786acefb88c0dc8676beee389",
".git/objects/ed/b55d4deb8363b6afa65df71d1f9fd8c7787f22": "24ff37338bd045d48203cf331771729e",
".git/objects/c1/dbd2cbad220887a291a3b96cd954a8558a06f2": "0bf058c2d7437bcc0868670ead59ff70",
".git/objects/ec/cd51686f8339118e1037d9c71b4900a4516f71": "c9ac6973ccfcdacab4b44a97795ab2fb",
".git/objects/20/3a3ff5cc524ede7e585dff54454bd63a1b0f36": "c6274b2aab2e5341d5afe75b20d9db20",
".git/objects/4b/44b25ab6b65fbc32ec33d31f8f9535ba8b0cca": "3326dfbcd43d413af5fc45e48048ba61",
".git/objects/11/7cd1fc6786d55f5fa856439f1066172ce83679": "321ba92143501f3713d40b1aac42ba21",
".git/objects/7d/d0189125709ab8f04309b23e28aececf1e2d5d": "654863cff500dd6837733b73007e4442",
".git/objects/29/878a4a6e9f8ae52cd5d96f61ead12b9e4d0e7c": "ca3c43c3346bd3894c6940f93c2bd512",
".git/objects/29/f22f56f0c9903bf90b2a78ef505b36d89a9725": "f5434dd611cf7832a2da98f9fd2a29f8",
".git/objects/7c/36a1c907f7965ad977cee1b9b2b06ffe81d27b": "4334718d598336ec1cbd4d3ce34274d9",
".git/objects/16/7c8c9db5bf593ea5ed6f792cbbaf930908b289": "25843ba500a3b9909fb2c5ad3e1f7760",
".git/objects/89/e6702177007dbc0c88250d80dfc6e79639d5d2": "c94dfb883b751ea53ee26625d051c37e",
".git/objects/89/fee3b8d71e7a3d9cb812dbe0040e38cb9cf540": "b0d3779cad752f68846fe7e6d2a1f5ef",
".git/objects/1f/6f415cd008dabe25caf06221ff04d48025c819": "06167a075f2b5a29aeb5bdb5fe1b704e",
".git/objects/87/5e3e65b90318d19b535b8487db62b04420df62": "d0e991a6d55964bdca33712bb3f0d294",
".git/objects/87/33f9f109e3ddc7fa3ec7064a4877bf59ebdcb1": "4f40455062bd303bd4db8c96199686ac",
".git/objects/87/b02f002652658924297b4930dc4615e7756572": "9962156031aa786035c4da7a1cdd51ab",
".git/objects/80/26ff2dfe34547fcaf62d29ccbb9e3b92e38dbd": "b299dda9c8f3ec46890077165269043e",
".git/objects/7b/127a6c9721b4f0a4f0a2a84528f7971bd0477c": "83f85f36d8296c21573e3fc86e2a8b45",
".git/objects/26/6ef034ded37fb32a4179171039b158e952886d": "4a46db46d8b0b972d2223ab8b90a6e8d",
".git/objects/4d/bf9da7bcce5387354fe394985b98ebae39df43": "f51ce74f4b30d985773489942de9706e",
".git/objects/86/1792788de650d30e38529944b5e1ad984275e7": "4948fef6bde6a6a312ae91b294b70092",
".git/objects/72/0994aacdaceea25e7053354e8c315bf9457c07": "e1f81315d3ba1ceac9485f05512e82e5",
".git/objects/43/478dcccbdff9dc2182a3d86e9851f1397bf755": "db2ba9b4cb223773ebad2a0f43fb2cd3",
".git/objects/88/bb15fa9adb722b520065c318e4380e2755542c": "ed09d0631e8bda29b5c73db7d2bdb8f0",
".git/objects/07/dc1e019cde9153a91025e21de0ccd2c24a6843": "9012282c8e0a351bd13e1266970e85ee",
".git/objects/36/0c852bb827e498414a6afa7f240ab573ccd8df": "d0763dd2c519454c34cd57dcd482db6f",
".git/objects/36/aa6d9302825e26fe69f3e0e06440ac2feb5ff1": "7c8b1297a90778b9a6d64c8bc340c06e",
".git/objects/36/61c862ab8640c2173961a97b8f63390e2e370b": "c6314c5786172d5cec85991ba91fa318",
".git/objects/31/ff033174bf7e1132b3ba7acf3411cd645b2852": "22778e59d7e92d67fa93526048772f5c",
".git/objects/98/0d49437042d93ffa850a60d02cef584a35a85c": "90e6fa94406f2f812d040574aa0da80a",
".git/objects/30/1a61f218a0c350c6f0d05606cadef1b00c7253": "604209b03e1970ac1ac0da6cfde154ac",
".git/objects/30/c9a76710470b493a568ede1d2dadbdb799a8eb": "1d4a2b41da259e11baed32b268394e0a",
".git/objects/5b/862207b73fbb325a39aa80cbde9aa6618a7f40": "c8b5c7e6ca5ec38b6d27859468c0c07e",
".git/objects/37/bff8171f52b8cac017a261f2010a9d58868a22": "65b021e3b6bda3907a047d41a67963e4",
".git/objects/6c/7b9134ab1b68dd62b748d8c9df216fa0b14170": "0143376d1f0917533d6dba6df1abdb05",
".git/objects/52/07c006a91e2a86374dc1af095264f49c1e1539": "34604ad9b89629a1ffcf46774ffa7340",
".git/objects/63/e9ad7790a76fb2284a5168e0da978afc1e6356": "21ea69f1d70bcb29c6195b509470cf70",
".git/objects/0a/ecdbee78eeb6cdc874778fd3c5b34b2ae78021": "162e87dd205f60bef33fa0bd14bee2b3",
".git/objects/64/8cb51113f2ac53d335a4fd3b8b1af5439440a9": "0e99f1e45d02108ddd65c148b3579201",
".git/objects/64/121c2c11f095110e80b6e7a038682beb370b17": "e602bb8f1ca57be9fdaee6be9ef3ea3a",
".git/objects/d4/3532a2348cc9c26053ddb5802f0e5d4b8abc05": "43dc1abdf318479619f8ba30d339447d",
".git/objects/ba/d1dbd0d2fa13ec91cf91fbb758250f6b64a96c": "c4a78ff52c899240311739f76d6a5edf",
".git/objects/b8/942205c0632fbf0412f71be1ae63f4819047a5": "508c3454dd1b86d01a6d9caf5f26a579",
".git/objects/b1/1c4e7d225d2c387c878ee3ccf724206f935a4c": "ce246df53198a19d9053105305336d02",
".git/objects/dd/3ff0856225950abf613f15113ba3ef5a33ea2f": "dcee499f84d0aa397a049c994b25b673",
".git/objects/b6/b8806f5f9d33389d53c2868e6ea1aca7445229": "a5750dc478ecba60aad59689a9defcc0",
".git/objects/b0/724a06209edf3f9ca3d9757056ab9b72feb866": "25e73393ae0989884be66ed5e3327eb8",
".git/objects/b9/d98ea70d584fb6c7a2633a6b47f5e84b9e934d": "4ffeaa15f29af1617efa369fc5eca722",
".git/objects/c4/016f7d68c0d70816a0c784867168ffa8f419e1": "f2d65397f0e87e6bcb5a23b72d6ae074",
".git/objects/ea/7a6c408d947dc30bae3796f1ad83a3eb508b9a": "a307fb091b968f0ddd7dadb64c9ab2b4",
".git/objects/ea/ba0c5e088000b49012647832aaabe5da3afba3": "c99e670fe2264b8d125ec81df3efb12e",
".git/objects/f9/92e6a74ef34f6b43faad886e5e47d6b33a45da": "166e27f467287ab787756f053b4191a3",
".git/objects/f6/c0c0cc66c772ec9558039ed67aec83abd723da": "3e7d292768f727e0bb26ed68cd3b1633",
".git/objects/e7/c596830ce6911c53580da5a2d430a0e222384c": "aa258151998b0058d8097e487c4a04a8",
".git/objects/cb/a1d1f2ff5ff962da551aabff02376beb7f4d44": "019a0e9a37e7e7e289829455c5da368b",
".git/objects/f8/b5486ac4a98531c09fe4037f06d9b594df2978": "3f7668193d4c066fb5a049807d3a7234",
".git/objects/e0/274b85dba417cb799a130a6fa3161c1f008fe2": "b61beb94f7772db7028fdc769b427ac5",
".git/objects/79/5c6bb959b0a39121efad739a974b8b1d86256f": "9b574465b87e52c505c674629e114287",
".git/objects/2d/cf45c36f82d61562747b1ecaca8d4062cefa67": "3b917fad4feac6af2dad0744c2601865",
".git/objects/77/54fba4c342e77ac43f1a031e36a24483f87de4": "3c5694e3e11f474f9b276eb0af2322fb",
".git/objects/84/096d2026c7eaa90217e6816da2168426221b5d": "ea6ba620af899e21503c2f8e3997745a",
".git/objects/4f/fbe6ec4693664cb4ff395edf3d949bd4607391": "fbf413e3e575c13db63f06544f500549",
".git/objects/8d/5be1d1d634656fabc7f9d0ff9f915b22ce5ce4": "7a5f38bae6970bbdad8551e238eb8818",
".git/objects/8d/e00b21d360d102f4f805b149144a6aab8f460c": "3903a48032c44f9c2768177a170fdacb",
".git/objects/12/afd337a1406325fbe50918b162b1ebca81da9a": "b041111aee1bb7ff8420bd795dd57c7d",
".git/objects/85/332df97d5368bdc2fdf7d1c762db4b65ffd3a7": "4f87f312b0c9a5c56d63ce145e257301",
".git/objects/76/0b978deb1d37d01f39424a8a5819679e096590": "97662f1b61e64f695a5c599d51f0ff54",
".git/objects/1c/23b965b1261dab6b0be6f316634eb2e2936328": "cefafca7027f11378bcc16589450c08f",
".git/objects/2b/bb1d07766920b70c2b0132268a5dfa40e29687": "f4da678eeac98f557cb882f51fbc7699",
".git/objects/8b/e6a41e9074969a870d82c32a0f1684bf03261e": "3717e7fbce6148af84952e597ecddef2",
".git/objects/7a/6c1911dddaea52e2dbffc15e45e428ec9a9915": "754eb3121a5999866afd25a8201d7816",
".git/objects/14/d566e466ddf58ea5024aef6920821150bd443e": "35a9a13d01c3ea36e6a6043db30b8203",
".git/objects/8e/92b9126af373efa140903d4adc36b6b67ddd76": "639b27905633ca9ebf5e78a603b5d250",
".git/objects/25/c9a83e82effb32058d7065cbd6479296aecb04": "8f1849d557b823c0fd08193378e13675",
".git/HEAD": "cf7dd3ce51958c5f13fece957cc417fb",
".git/info/exclude": "036208b4a1ab4a235d75c181e685e5a3",
".git/logs/HEAD": "5181762af6bc75418b598e89c5540c55",
".git/logs/refs/heads/main": "f639dc0ce423925a0e3a4525f2de9a73",
".git/logs/refs/remotes/origin/main": "00bff0711e5fa4c6c9012eabc71d1cff",
".git/description": "a0a7c3fff21f2aea3cfa1d0316dd816c",
".git/hooks/commit-msg.sample": "579a3c1e12a1e74a98169175fb913012",
".git/hooks/pre-rebase.sample": "56e45f2bcbc8226d2b4200f7c46371bf",
".git/hooks/pre-commit.sample": "305eadbbcd6f6d2567e033ad12aabbc4",
".git/hooks/applypatch-msg.sample": "ce562e08d8098926a3862fc6e7905199",
".git/hooks/fsmonitor-watchman.sample": "a0b2633a2c8e97501610bd3f73da66fc",
".git/hooks/pre-receive.sample": "2ad18ec82c20af7b5926ed9cea6aeedd",
".git/hooks/prepare-commit-msg.sample": "2b5c047bdb474555e1787db32b2d2fc5",
".git/hooks/post-update.sample": "2b7ea5cee3c49ff53d41e00785eb974c",
".git/hooks/pre-merge-commit.sample": "39cb268e2a85d436b9eb6f47614c3cbc",
".git/hooks/pre-applypatch.sample": "054f9ffb8bfe04a599751cc757226dda",
".git/hooks/pre-push.sample": "2c642152299a94e05ea26eae11993b13",
".git/hooks/update.sample": "647ae13c682f7827c22f5fc08a03674e",
".git/hooks/push-to-checkout.sample": "c7ab00c7784efeadad3ae9b228d4b4db",
".git/refs/heads/main": "8017673dace0b6e3c21a283e77e2f256",
".git/refs/remotes/origin/main": "8017673dace0b6e3c21a283e77e2f256",
".git/index": "966941ca9d90d93b362d7d94d68c9493",
".git/packed-refs": "a891e6bb26eb0d480aef486a7e8ea166",
".git/COMMIT_EDITMSG": "a8297d555dd34879e8e48e1cf12acefa",
".git/FETCH_HEAD": "da1e218c300bf96f9949249b7a02ed64",
"assets/AssetManifest.json": "418466c0819added040bd655c664d3bd",
"assets/NOTICES": "845655ceeaaf861a686947293f66b36a",
"assets/FontManifest.json": "a31e45ac92800e57362e2330914035ce",
"assets/AssetManifest.bin.json": "3c999549e3d95065d345e95afaedc228",
"assets/packages/font_awesome_flutter/lib/fonts/Font%2520Awesome%25207%2520Free-Solid-900.otf": "e151d7a6f42f17e9ea335c91d07b3739",
"assets/packages/font_awesome_flutter/lib/fonts/Font%2520Awesome%25207%2520Free-Regular-400.otf": "df86a1976d76bd04cf3fcaf5add2dd0f",
"assets/packages/font_awesome_flutter/lib/fonts/Font%2520Awesome%25207%2520Brands-Regular-400.otf": "440da663f17184f21f007a3a2bf60f69",
"assets/packages/lucide_icons_flutter/assets/lucide.ttf": "5b249b2a80c50f482a9bc65046acd324",
"assets/packages/lucide_icons_flutter/assets/build_font/LucideVariable-w500.ttf": "2380c4b0a5e2fc1290cdd266003d6a5e",
"assets/packages/lucide_icons_flutter/assets/build_font/LucideVariable-w100.ttf": "64144aa1aa76d2b82813658df2a26c79",
"assets/packages/lucide_icons_flutter/assets/build_font/LucideVariable-w300.ttf": "930b720a5d939c5e880b5b5db9087ad1",
"assets/packages/lucide_icons_flutter/assets/build_font/LucideVariable-w400.ttf": "0fa0c68ca0b2e71120150346577b89cf",
"assets/packages/lucide_icons_flutter/assets/build_font/LucideVariable-w600.ttf": "1dd6fffeb3cb7e347be36f9d80e51767",
"assets/packages/lucide_icons_flutter/assets/build_font/LucideVariable-w200.ttf": "d88bfd6ad62ffb93fb21a930431405f7",
"assets/shaders/ink_sparkle.frag": "ecc85a2e95f5e9f53123dcaf8cb9b6ce",
"assets/AssetManifest.bin": "b0810e236d4e2470cb9fac0b12d14545",
"assets/fonts/MaterialIcons-Regular.otf": "5c3ce806884d0ffaedde98e3137b385d",
"assets/assets/images/moon_temp.png": "f520fb6641cd94055192f6ed6a25267d",
"assets/assets/images/moon.png": "0f0fee609106e1e52371e038c9aab2f3",
"assets/assets/images/sun_temp.png": "f8eb87e8ee89f29428837269bb6429ed",
"assets/assets/images/sun.png": "29a998c33a91c1873fe4d06c057767ab",
"assets/assets/icons/github.svg": "bd4115feff40afa66c02080d152414f1",
"assets/assets/icons/github1.svg": "f666cabb6611ba406a5bb558688061a8",
"assets/assets/icons/sun.svg": "e8fd6c5c3296080d2958830d5254ba74",
"assets/assets/icons/linkedin.svg": "f9dbbcb6071e35e9575975eb16c1330d",
"assets/assets/icons/moon.svg": "d8ddb8c313335b48df90f2a6eeae79b5",
"canvaskit/skwasm.js": "1ef3ea3a0fec4569e5d531da25f34095",
"canvaskit/skwasm_heavy.js": "413f5b2b2d9345f37de148e2544f584f",
"canvaskit/skwasm.js.symbols": "0088242d10d7e7d6d2649d1fe1bda7c1",
"canvaskit/canvaskit.js.symbols": "58832fbed59e00d2190aa295c4d70360",
"canvaskit/skwasm_heavy.js.symbols": "3c01ec03b5de6d62c34e17014d1decd3",
"canvaskit/skwasm.wasm": "264db41426307cfc7fa44b95a7772109",
"canvaskit/chromium/canvaskit.js.symbols": "193deaca1a1424049326d4a91ad1d88d",
"canvaskit/chromium/canvaskit.js": "5e27aae346eee469027c80af0751d53d",
"canvaskit/chromium/canvaskit.wasm": "24c77e750a7fa6d474198905249ff506",
"canvaskit/canvaskit.js": "140ccb7d34d0a55065fbd422b843add6",
"canvaskit/canvaskit.wasm": "07b9f5853202304d3b0749d9306573cc",
"canvaskit/skwasm_heavy.wasm": "8034ad26ba2485dab2fd49bdd786837b"};
// The application shell files that are downloaded before a service worker can
// start.
const CORE = ["main.dart.js",
"index.html",
"flutter_bootstrap.js",
"assets/AssetManifest.bin.json",
"assets/FontManifest.json"];

// During install, the TEMP cache is populated with the application shell files.
self.addEventListener("install", (event) => {
  self.skipWaiting();
  return event.waitUntil(
    caches.open(TEMP).then((cache) => {
      return cache.addAll(
        CORE.map((value) => new Request(value, {'cache': 'reload'})));
    })
  );
});
// During activate, the cache is populated with the temp files downloaded in
// install. If this service worker is upgrading from one with a saved
// MANIFEST, then use this to retain unchanged resource files.
self.addEventListener("activate", function(event) {
  return event.waitUntil(async function() {
    try {
      var contentCache = await caches.open(CACHE_NAME);
      var tempCache = await caches.open(TEMP);
      var manifestCache = await caches.open(MANIFEST);
      var manifest = await manifestCache.match('manifest');
      // When there is no prior manifest, clear the entire cache.
      if (!manifest) {
        await caches.delete(CACHE_NAME);
        contentCache = await caches.open(CACHE_NAME);
        for (var request of await tempCache.keys()) {
          var response = await tempCache.match(request);
          await contentCache.put(request, response);
        }
        await caches.delete(TEMP);
        // Save the manifest to make future upgrades efficient.
        await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
        // Claim client to enable caching on first launch
        self.clients.claim();
        return;
      }
      var oldManifest = await manifest.json();
      var origin = self.location.origin;
      for (var request of await contentCache.keys()) {
        var key = request.url.substring(origin.length + 1);
        if (key == "") {
          key = "/";
        }
        // If a resource from the old manifest is not in the new cache, or if
        // the MD5 sum has changed, delete it. Otherwise the resource is left
        // in the cache and can be reused by the new service worker.
        if (!RESOURCES[key] || RESOURCES[key] != oldManifest[key]) {
          await contentCache.delete(request);
        }
      }
      // Populate the cache with the app shell TEMP files, potentially overwriting
      // cache files preserved above.
      for (var request of await tempCache.keys()) {
        var response = await tempCache.match(request);
        await contentCache.put(request, response);
      }
      await caches.delete(TEMP);
      // Save the manifest to make future upgrades efficient.
      await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
      // Claim client to enable caching on first launch
      self.clients.claim();
      return;
    } catch (err) {
      // On an unhandled exception the state of the cache cannot be guaranteed.
      console.error('Failed to upgrade service worker: ' + err);
      await caches.delete(CACHE_NAME);
      await caches.delete(TEMP);
      await caches.delete(MANIFEST);
    }
  }());
});
// The fetch handler redirects requests for RESOURCE files to the service
// worker cache.
self.addEventListener("fetch", (event) => {
  if (event.request.method !== 'GET') {
    return;
  }
  var origin = self.location.origin;
  var key = event.request.url.substring(origin.length + 1);
  // Redirect URLs to the index.html
  if (key.indexOf('?v=') != -1) {
    key = key.split('?v=')[0];
  }
  if (event.request.url == origin || event.request.url.startsWith(origin + '/#') || key == '') {
    key = '/';
  }
  // If the URL is not the RESOURCE list then return to signal that the
  // browser should take over.
  if (!RESOURCES[key]) {
    return;
  }
  // If the URL is the index.html, perform an online-first request.
  if (key == '/') {
    return onlineFirst(event);
  }
  event.respondWith(caches.open(CACHE_NAME)
    .then((cache) =>  {
      return cache.match(event.request).then((response) => {
        // Either respond with the cached resource, or perform a fetch and
        // lazily populate the cache only if the resource was successfully fetched.
        return response || fetch(event.request).then((response) => {
          if (response && Boolean(response.ok)) {
            cache.put(event.request, response.clone());
          }
          return response;
        });
      })
    })
  );
});
self.addEventListener('message', (event) => {
  // SkipWaiting can be used to immediately activate a waiting service worker.
  // This will also require a page refresh triggered by the main worker.
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
    return;
  }
  if (event.data === 'downloadOffline') {
    downloadOffline();
    return;
  }
});
// Download offline will check the RESOURCES for all files not in the cache
// and populate them.
async function downloadOffline() {
  var resources = [];
  var contentCache = await caches.open(CACHE_NAME);
  var currentContent = {};
  for (var request of await contentCache.keys()) {
    var key = request.url.substring(origin.length + 1);
    if (key == "") {
      key = "/";
    }
    currentContent[key] = true;
  }
  for (var resourceKey of Object.keys(RESOURCES)) {
    if (!currentContent[resourceKey]) {
      resources.push(resourceKey);
    }
  }
  return contentCache.addAll(resources);
}
// Attempt to download the resource online before falling back to
// the offline cache.
function onlineFirst(event) {
  return event.respondWith(
    fetch(event.request).then((response) => {
      return caches.open(CACHE_NAME).then((cache) => {
        cache.put(event.request, response.clone());
        return response;
      });
    }).catch((error) => {
      return caches.open(CACHE_NAME).then((cache) => {
        return cache.match(event.request).then((response) => {
          if (response != null) {
            return response;
          }
          throw error;
        });
      });
    })
  );
}
