const now = new Date().toISOString().split('T')[0];

module.exports = function(eleventyConfig) {
  // Custom filters
  eleventyConfig.addFilter("dateISO", () => now);
  eleventyConfig.addFilter("pad", (num, len, char) => {
    return String(num).padStart(len || 2, char || '0');
  });

  return {
    dir: {
      input: "src",
      output: "_site"
    },
    templateFormats: ["njk", "html", "xml", "txt"],
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: false
  };
};
