(() => {
  const attributeNames = [
    'title',
    'aria-label',
    'aria-description',
    'placeholder',
    'alt',
    'data-label',
    'data-tooltip',
  ];
  const skippedTags = new Set(['SCRIPT', 'STYLE', 'CODE', 'PRE', 'TEXTAREA']);

  function replaceBrand(value) {
    if (!value || !/revo/i.test(value)) return value;

    return value
      .replace(/\bREVO\s+ENGINE\b/gi, 'VITERAZ ENGINE')
      .replace(/\bRevo\s*Studio\b/gi, 'Viteraz Studio')
      .replace(/\bRevo\s*Voice\b/gi, 'Viteraz Voice')
      .replace(/\bRevoVoice\b/gi, 'Viteraz Voice')
      .replace(/\bRevo\b/gi, 'Viteraz');
  }

  function updateTextNode(node) {
    if (skippedTags.has(node.parentElement?.tagName)) return;
    const updated = replaceBrand(node.nodeValue);
    if (updated !== node.nodeValue) node.nodeValue = updated;
  }

  function updateElement(element) {
    if (skippedTags.has(element.tagName)) return;

    for (const attributeName of attributeNames) {
      if (!element.hasAttribute(attributeName)) continue;
      const current = element.getAttribute(attributeName);
      const updated = replaceBrand(current);
      if (updated !== current) element.setAttribute(attributeName, updated);
    }
  }

  function updateTree(root) {
    if (root.nodeType === Node.TEXT_NODE) {
      updateTextNode(root);
      return;
    }
    if (root.nodeType !== Node.ELEMENT_NODE) return;

    updateElement(root);
    for (const element of root.querySelectorAll('*')) updateElement(element);

    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) updateTextNode(walker.currentNode);
  }

  const observer = new MutationObserver((mutations) => {
    for (const mutation of mutations) {
      if (mutation.type === 'characterData') {
        updateTextNode(mutation.target);
      } else if (mutation.type === 'attributes') {
        updateElement(mutation.target);
      } else {
        for (const node of mutation.addedNodes) updateTree(node);
      }
    }
  });

  updateTree(document.documentElement);
  observer.observe(document.documentElement, {
    subtree: true,
    childList: true,
    characterData: true,
    attributes: true,
    attributeFilter: attributeNames,
  });
})();
