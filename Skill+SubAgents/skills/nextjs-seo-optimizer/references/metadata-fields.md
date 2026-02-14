## Detailed Metadata Properties for Social Sharing

### Open Graph Properties
- **title** - The title of the page (recommended: 50-60 characters)
- **description** - The description of the page (recommended: under 200 characters)
- **siteName** - The name of the website
- **images** - Array of image objects with:
  - `url` - Absolute URL of the image
  - `width` - Width of the image in pixels
  - `height` - Height of the image in pixels
  - `alt` - Alternative text for the image
- **locale** - Language and territory (e.g., 'en_US', 'es_ES')
- **type** - Type of content ('website', 'article', 'video.movie', etc.)

### Twitter Card Properties
- **card** - Type of card ('summary', 'summary_large_image', 'app', 'player')
- **site** - Twitter handle of the website (e.g., '@username')
- **creator** - Twitter handle of the content creator
- **title** - Title of the content
- **description** - Description of the content
- **images** - Array of image objects (similar to Open Graph)

### Robots Properties
- **index** - Whether the page should be indexed (default: true)
- **follow** - Whether links on the page should be followed (default: true)
- **nocache** - Whether to prevent caching (default: false)
- **googleBot** - Google-specific directives:
  - `index` - Google-specific indexing directive
  - `follow` - Google-specific follow directive
  - `maxSnippet` - Maximum length of text snippet in search results
  - `maxImagePreview` - Maximum size of image preview ('none', 'standard', 'large')
  - `maxVideoPreview` - Maximum duration of video snippet in seconds