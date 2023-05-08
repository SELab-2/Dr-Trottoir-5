import config from '@/config'
import { CacheableResponsePlugin } from 'workbox-cacheable-response'
import { ExpirationPlugin } from 'workbox-expiration'

import { precacheAndRoute } from 'workbox-precaching'
import { registerRoute, Route } from 'workbox-routing'
import { CacheFirst, NetworkOnly, StaleWhileRevalidate } from 'workbox-strategies'

precacheAndRoute(self.__WB_MANIFEST)

const backend = config.BACKEND
const frontend = config.FRONTEND

/*
* Start with the service workers for the static files
* */

// Handle static images like the favicon and others in the assets folder in the frontend
registerRoute(
  new Route(({ request }) => {
      return request.destination === 'image'
    },
    new CacheFirst({
      cacheName: 'static-images',
      plugins: [
        new ExpirationPlugin({
          maxEntries: 30,
          maxAgeSeconds: 30 * 24 * 60 * 60 // 30 Days
        }),
        /* Needed because of CORS but it's easier to add it to all the routes */
        new CacheableResponsePlugin({
          statuses: [0, 200]
        })
      ]
    })
  )
);
// Handle scripts:
registerRoute(
  new Route(({ request }) => {
    return request.destination === 'script';
  }, new CacheFirst({
    cacheName: 'static-scripts',
    plugins: [
      new ExpirationPlugin({
        maxEntries: 30, // should be plenty for the whole site. We have 4 js files now
        maxAgeSeconds: 30 * 24 * 60 * 60 // 30 Days
      }),
      new CacheableResponsePlugin({
        statuses: [0, 200]
      })
    ]
  }))
);

// Handle css files:
registerRoute(
  new Route(
    ({ request }) => {
      return request.destination === 'style';
    }, new CacheFirst({
      cacheName: 'static-styles',
      plugins: [
        new ExpirationPlugin({
          maxEntries: 30, // should be plenty we have 2 of them now
          maxAgeSeconds: 30 * 24 * 60 * 60 // 30 Days
        }),
        new CacheableResponsePlugin({
          statuses: [0, 200]
        })
      ]
    }))
);

/*
*********************************************************
* Service workers and caches for the "dynamic" files
* AKA responses from the API
* */

registerRoute(
  new Route(
    /* When to use the handler */
    ({ request }) => {
      return request.url.startsWith(backend + "/login")
    },
    /* The handler if the route matches */
    new NetworkOnly({
      cacheName: 'login',
      plugins: [
        /* No expiration plugin because this does not get cached */
        new CacheableResponsePlugin({
          /* Only 0 - 200 responses get cached */
          statuses: [0, 200]
        })
      ]
    })
  )
);

registerRoute(
  new Route(
    /* When to use the handler */
    ({ request }) => {
      return request.url.startsWith(backend + "/logout")
    },
    /* The handler if the route matches */
    new NetworkOnly({
      cacheName: 'logout',
      plugins: [
        /* No expiration plugin because this does not get cached */
        new CacheableResponsePlugin({
          /* Only 0 - 200 responses get cached */
          statuses: [0, 200]
        })
      ]
    })
  )
);

registerRoute(
  new Route(
    /* When to use the handler */
    ({ request }) => {
      return request.url.startsWith(backend + "/planning/buildingpicture")
    },
    /* Cache First since these pictures do not get updated */
    new CacheFirst({
      cacheName: 'buildingPictures',
      plugins: [
        new ExpirationPlugin({
          maxEntries: 60,
          maxAgeSeconds: 30 * 24 * 60 * 60 // 30 Days
        }),
        new CacheableResponsePlugin({
          statuses: [0, 200]
        })
      ]
    })
  )
);

registerRoute(
  new Route(
    ({ request }) => {
      return request.url.startsWith(backend + "/admin/mailtemplates")
    },
    new StaleWhileRevalidate({
      cacheName: 'mailtemplates',
      plugins: [
        new ExpirationPlugin({
          maxEntries: 60, //todo test of dit veel/weinig is
          maxAgeSeconds: 30 * 24 * 60 * 60 // 30 Days
        }),
        new CacheableResponsePlugin({
          statuses: [0, 200]
        })
      ]
    })
  )
);

registerRoute(
  new Route(
    ({ request }) => {
      return request.url.startsWith(backend + "/ronde/building/manual")
    },
    /* Cache First because these mostly do not get updated */
    new CacheFirst({
      cacheName: 'buildingmanuals',
      plugins: [
        new ExpirationPlugin({
          maxEntries: 60, // manuals of 60 buildings should be enough to span 1 week of work. I think
          maxAgeSeconds: 7 * 24 * 60 * 60 // 7 Days, 1 week
        }),
        new CacheableResponsePlugin({
          statuses: [0, 200]
        })
      ]
    })
  )
);

/* Matches everything */
registerRoute(new Route(({ request }) => {
  return !(
    request.url.startsWith(backend + "/login") ||
    request.url.startsWith(backend + "/logout") ||
    request.url.startsWith(backend + "/planning/buildingpicture") ||
    request.url.startsWith(backend + "/admin/mailtemplates") ||
    request.url.startsWith(backend + "/ronde/building/manual")
  );
}, new StaleWhileRevalidate({
  /* For response time reasons things may get cached but are always revalidated. */
  cacheName: 'everything',
  plugins: [
    new ExpirationPlugin({
      maxEntries: 100, // May be enough for everything since they are always revalidated.
      maxAgeSeconds: 7 * 24 * 60 * 60 // 7 Days. But does not really matter, they are always updated
    }),
    new CacheableResponsePlugin({
      statuses: [0, 200]
    })
  ]
})))
