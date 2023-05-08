import config from '@/config'
import { CacheableResponsePlugin } from 'workbox-cacheable-response'
import { ExpirationPlugin } from 'workbox-expiration'

import { precacheAndRoute } from 'workbox-precaching'
import { registerRoute, Route } from 'workbox-routing'
import { CacheFirst } from 'workbox-strategies'

precacheAndRoute(self.__WB_MANIFEST)

// todo check of alle pathnames wel kloppen

/*
* Start with the service workers for the static files
* */

// Handle static images:
const imageRoute = new Route(({ request }) => {
  return request.destination === 'image'
}, new CacheFirst({
  cacheName: 'static-images',
  plugins: [
    new ExpirationPlugin({
      maxEntries: 30, // should be plenty for the whole site once
      maxAgeSeconds: 30 * 24 * 60 * 60 // 30 Days
    }),
    new CacheableResponsePlugin({
      statuses: [0, 200]
    })
  ]
}))

// Handle scripts:
const scriptsRoute = new Route(({ request }) => {
  return request.destination === 'script'
}, new CacheFirst({
  cacheName: 'scripts',
  plugins: [
    new ExpirationPlugin({
      maxEntries: 30, // should be plenty for the whole site once
      maxAgeSeconds: 30 * 24 * 60 * 60 // 30 Days
    }),
    new CacheableResponsePlugin({
      statuses: [0, 200]
    })
  ]
}))

// Handle styles:
const stylesRoute = new Route(({ request }) => {
  return request.destination === 'style'
}, new CacheFirst({
  cacheName: 'styles',
  plugins: [
    new ExpirationPlugin({
      maxEntries: 30, // should be plenty for the whole site once
      maxAgeSeconds: 30 * 24 * 60 * 60 // 30 Days
    }),
    new CacheableResponsePlugin({
      statuses: [0, 200]
    })
  ]
}))
registerRoute(imageRoute)
registerRoute(scriptsRoute)
registerRoute(stylesRoute)

/*
* Service workers and caches for the "dynamic" files
* */
registerRoute(
  ({ url }) => url.pathname.startsWith(`${config.BACKEND.URL}/planning/buildingpicture`),
  new CacheFirst({
    cacheName: 'images',
    plugins: [
      new ExpirationPlugin({
        maxEntries: 60, // todo test of dit veel/weinig is
        maxAgeSeconds: 30 * 24 * 60 * 60 // 30 Days
      }),
      new CacheableResponsePlugin({
        statuses: [0, 200]
      })
    ]
  })
)

registerRoute(
  ({ url }) => url.pathname.startsWith(`${config.BACKEND.URL}/admin/mailtemplates`),
  new CacheFirst({
    cacheName: 'mailtemplates',
    plugins: [
      new ExpirationPlugin({
        maxEntries: 60, // todo test of dit veel/weinig is
        maxAgeSeconds: 30 * 24 * 60 * 60 // 30 Days
      }),
      new CacheableResponsePlugin({
        statuses: [0, 200]
      })
    ]
  })
)

registerRoute(
  ({ url }) => url.pathname.startsWith(`${config.BACKEND.URL}/ronde/building/manual`),
  new CacheFirst({
    cacheName: 'manuals',
    plugins: [
      new ExpirationPlugin({
        maxEntries: 60, // todo test of dit veel/weinig is
        maxAgeSeconds: 30 * 24 * 60 * 60 // 30 Days
      }),
      new CacheableResponsePlugin({
        statuses: [0, 200]
      })
    ]
  })
)

/* Matches everything */
registerRoute(new Route(({ request }) => {
  return true
}, new CacheFirst({
  cacheName: 'scripts',
  plugins: [
    new ExpirationPlugin({
      maxEntries: 30, // should be plenty for the whole site once
      maxAgeSeconds: 30 * 24 * 60 * 60 // 30 Days
    }),
    new CacheableResponsePlugin({
      statuses: [0, 200]
    })
  ]
})))
