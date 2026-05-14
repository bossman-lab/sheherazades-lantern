const now = new Date().toISOString().split('T')[0];

module.exports = function(eleventyConfig) {
  // Custom filters
  eleventyConfig.addFilter("dateISO", () => now);
  eleventyConfig.addFilter("dateRfc822", (dateStr) => {
    const d = new Date(dateStr);
    const days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];
    const months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
    return `${days[d.getUTCDay()]}, ${String(d.getUTCDate()).padStart(2,"0")} ${months[d.getUTCMonth()]} ${d.getUTCFullYear()} ${String(d.getUTCHours()).padStart(2,"0")}:${String(d.getUTCMinutes()).padStart(2,"0")}:${String(d.getUTCSeconds()).padStart(2,"0")} +0000`;
  });
  eleventyConfig.addFilter("pad", (num, len, char) => {
    return String(num).padStart(len || 2, char || '0');
  });
  eleventyConfig.addFilter("json_str", (str) => {
    return JSON.stringify(str).slice(1, -1); // remove surrounding quotes
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
