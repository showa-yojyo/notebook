// Usage: see <http://docs.mathjax.org/en/latest/configuration.html>.

window.MathJax = {
    TeX:
    {
        Macros: {
            NN: "{\\mathbb N}",
            ZZ: "{\\mathbb Z}",
            QQ: "{\\mathbb Q}",
            RR: "{\\mathbb R}",
            CC: "{\\mathbb C}",
            bm: ["{\\boldsymbol #1}",1],
            dd: ["{\\mathrm d^{#1}}", 1, ""],
            diff: ["{\\frac{\\dd {#1}}{\\dd {#2}}}", 2],
            diag: "{{\\operatorname{diag}}}",
            dt: "{\\mathrm d t}",
            dx: "{\\mathrm d x}",
            dy: "{\\mathrm d y}",
            dz: "{\\mathrm d z}",
            eps: "{\\varepsilon}",
            grad: "{{\\operatorname{grad}}}",
            id: "{{\\operatorname{id}}}",
            longto: "\\longrightarrow",
            mdiff: ["{\\frac{\\dd[#2]#1}{\\dd #3^{#2}}}", 3],
            rank: "{{\\operatorname{rank}}}",
            supp: "{{\\operatorname{supp}}}",
            trace: "{{\\operatorname{trace}}}"
        }
    }
};
