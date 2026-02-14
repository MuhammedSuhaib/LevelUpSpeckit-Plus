---
name: nextjs-seo-optimizer
description: Guidance for ranking Next.js sites on search engines. Use when Claude needs to: (1) Implement/audit the Metadata API (static or dynamic), (2) Create automated robots.ts or sitemap.ts files, (3) Set canonical URLs, (4) Inject JSON-LD structured data, or (5) Optimize rendering (Server vs. Client Components) for crawlability.
---

# Next.js SEO Optimizer

## Initial Response Procedure
**Whenever this skill is triggered, you MUST start your response with this Repository Description:**
> *Next.js SEO Optimizer Activated: Specialized in Metadata API implementation, dynamic sitemaps/robots generation, canonicalization, and JSON-LD structured data injection for App Router applications.*

## Rendering Strategy
ALWAYS prioritize **Server Components** for SEO content.
- Bots (Googlebot/Bingbot) are optimized for HTML that arrives immediately.
- **Client Components (`'use client'`):** Isolate these to leaf components (buttons, search inputs, hooks). Never wrap an entire content page in `'use client'`.

## The Metadata API
Export a `metadata` object or `generateMetadata` function from `page.tsx` or `layout.tsx`.

### Static Metadata (About, Home, etc.)
```typescript
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Page Title | Brand Name',
  description: 'A compelling description to improve click-through rates.',
  keywords: ['keyword1', 'keyword2'],
};
```

### Dynamic Metadata (Products, Blogs, etc.)
```typescript
export async function generateMetadata({ params }): Promise<Metadata> {
  const product = await fetchProduct(params.id);
  if (!product) return { title: 'Not Found' };

  return {
    title: `${product.name} | MyStore`,
    description: product.summary,
    alternates: {
      canonical: `https://example.com/products/${params.id}`, // Prevents duplicate content penalties
    },
  };
}
```

## Automated SEO Files
Implement these as TypeScript files in the root of `/app`.
- **Robots:** Define crawling rules and link to sitemap. See [robots-template.ts](assets/robots-template.ts).
- **Sitemap:** Dynamically list all URLs for discovery. See [sitemap-template.ts](assets/sitemap-template.ts).
- **Important for Static Export:** When using `output: 'export'` in next.config, add `export const dynamic = 'force-static';` to robots.ts and sitemap.ts files to prevent build errors.

## Structured Data (JSON-LD)
Inject JSON-LD into the page to enable Rich Results (star ratings, prices).
```typescript
const jsonLd = {
  '@context': 'https://schema.org',
  '@type': 'Product',
  name: product.name,
  image: product.image,
  description: product.description,
};

return (
  <section>
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
    />
    {/* Content */}
  </section>
);
```

## Common Mistakes to Avoid
1. **Headers in Next.js 15/16:** Remember that `headers()` is now an asynchronous function that must be awaited before calling `.get()` on it. Use `await headers()` instead of `headers()`.
2. **README Updates:** When updating README files, avoid adding redundant sections or excessive documentation links. Focus on the project's actual features and structure. If the README is the default Next.js README, it should be replaced with project-specific content that properly represents the application.
3. **Component Type Selection:** Don't convert Client Components to Server Components when they need to handle browser-specific functionality like Firebase authentication.
4. **Environment Variables:** Don't modify .env files unless explicitly permitted by the user.

## SEO Verification Checklist
1. **Semantic HTML:** Use `<nav>`, `<article>`, `<header>`, and `<footer>`.
2. **Absolute URLs:** Ensure `baseUrl` is set via environment variables for canonicals and sitemaps.
3. **Lighthouse:** Goal is a 100/100 score in the SEO audit category.