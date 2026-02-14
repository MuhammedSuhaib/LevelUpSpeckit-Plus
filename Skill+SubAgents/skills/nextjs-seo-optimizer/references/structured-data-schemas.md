## Common Schema Structures for JSON-LD

### Article Schema
For blog posts, news articles, and other written content:
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "description": "Brief description of the article",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://example.com/author"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Publisher Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "datePublished": "2023-01-01T12:00:00+00:00",
  "dateModified": "2023-01-02T14:30:00+00:00",
  "image": {
    "@type": "ImageObject",
    "url": "https://example.com/article-image.jpg",
    "width": 1200,
    "height": 800
  }
}
```

### Product Schema
For e-commerce products and items for sale:
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "description": "Product description",
  "brand": {
    "@type": "Brand",
    "name": "Brand Name"
  },
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "Seller Name"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "89"
  },
  "image": [
    "https://example.com/product1.jpg",
    "https://example.com/product2.jpg"
  ]
}
```

### BreadcrumbList Schema
For navigation breadcrumbs:
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Category",
      "item": "https://example.com/category"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Current Page",
      "item": "https://example.com/category/current-page"
    }
  ]
}
```

### Organization Schema
For company/organization information:
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Company Name",
  "legalName": "Legal Company Name",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "foundingDate": "2020",
  "founders": [
    {
      "@type": "Person",
      "name": "Founder Name"
    }
  ],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345",
    "addressCountry": "US"
  },
  "contactPoint": [
    {
      "@type": "ContactPoint",
      "telephone": "+1-555-555-5555",
      "contactType": "customer service"
    }
  ]
}
```

### FAQPage Schema
For frequently asked questions:
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Question 1?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Answer to question 1."
      }
    },
    {
      "@type": "Question",
      "name": "Question 2?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Answer to question 2."
      }
    }
  ]
}
```