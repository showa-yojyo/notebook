window.addEventListener('load', () => {
    if (!document.querySelector('.mermaid')) {
        return;
    }

    const js = document.createElement("script");
    js.src = "https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js";
    js.onload = () => {
        mermaid.initialize({
            startOnLoad: true,
            theme: 'base',
            themeVariables: {
                primaryColor: 'white',
                lineColor: 'black',
                textColor: 'black',
                primaryBorderColor: 'black',
            },
        });
        mermaid.init(undefined, document.querySelectorAll('.mermaid'));
    };
    document.head.appendChild(js);
});
