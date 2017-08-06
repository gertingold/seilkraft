from math import cos, radians, sin, tan
from pyx import canvas, color, deco, path, style, text, trafo, unit

unit.set(xscale=1.2)
text.set(text.LatexRunner)
c = canvas.canvas()
w = 8
h = 5
c.stroke(path.path(path.moveto(w, 0),
                   path.lineto(0, 0),
                   path.lineto(0, h)),
         [deco.barrow, deco.earrow])
c.text(w, -0.2, '$x$', [text.halign.right, text.valign.top])
c.text(-0.2, h, '$y$', [text.halign.right, text.valign.top])

l = 2.5
phil = 20
phi = 35
phir = 50
c.stroke(path.line(0, 0, l, 0), [style.linestyle.dotted,
                                 trafo.rotate(180+phil).translated(2.6, 1.5)])
c.stroke(path.line(0, 0, l, 0), [trafo.rotate(phi).translated(2.6, 1.5)])
c.stroke(path.line(0, 0, l, 0),
         [style.linestyle.dotted,
          trafo.rotate(phir).translated(2.6+l*cos(radians(phi)),
                                         1.5+l*sin(radians(phi)))])
c.stroke(path.circle(2.6, 1.5, 0.05), [deco.filled([color.grey(1)])])
c.stroke(path.circle(2.6+l*cos(radians(phi)),
                     1.5+l*sin(radians(phi)), 0.05), [deco.filled([color.grey(1)])])

fx = 1
c.stroke(path.line(0, 0, 0, -fx*(tan(radians(phir))-tan(radians(phil)))),
         [deco.earrow, style.linewidth.thick,
         trafo.translate(2.6+0.5*l*cos(radians(phi)),
                         1.5+0.5*l*sin(radians(phi)))])
c.text(2.6+0.5*l*cos(radians(phi))+0.2,
       1.5+0.5*l*sin(radians(phi))-fx*(tan(radians(phir))-tan(radians(phil))),
       r'$\vec G$')
c.text(2.6+0.5*l*cos(radians(phi))-0.2, 1.5+0.5*l*sin(radians(phi))+0.2,
       r'$\mathrm{d}s$')

c.stroke(path.line(0, 0, -fx, 0),
         [color.grey(0.5), deco.earrow, style.linewidth.thick,
          trafo.translate(2.6, 1.5)])
c.stroke(path.line(0, 0, 0, -fx*tan(radians(phil))),
         [color.grey(0.5), deco.earrow, style.linewidth.thick,
          trafo.translate(2.6, 1.5)])
c.stroke(path.line(0, 0, -fx, -fx*tan(radians(phil))),
         [deco.earrow, style.linewidth.thick, trafo.translate(2.6, 1.5)])
c.text(2.6-fx, 1.6-fx*tan(radians(phil))-0.2, r'$\vec F^{(-)}$',
       [text.valign.top])

c.stroke(path.line(0, 0, fx, 0),
         [color.grey(0.5), deco.earrow, style.linewidth.thick,
          trafo.translate(2.6+l*cos(radians(phi)), 1.5+l*sin(radians(phi)))])
c.stroke(path.line(0, 0, 0, fx*tan(radians(phir))),
         [color.grey(0.5), deco.earrow, style.linewidth.thick,
          trafo.translate(2.6+l*cos(radians(phi)), 1.5+l*sin(radians(phi)))])
c.stroke(path.line(0, 0, fx, fx*tan(radians(phir))),
         [deco.earrow, style.linewidth.thick,
          trafo.translate(2.6+l*cos(radians(phi)),
                          1.5+l*sin(radians(phi)))])
c.text(2.6+l*cos(radians(phi))+fx+0.1,
       1.5+l*sin(radians(phi))+fx*tan(radians(phir)),
       r'$\vec F^{(+)}$', [text.valign.top])
        

c.stroke(path.line(2.6, -0.1, 2.6, 0.1))
c.stroke(path.line(2.6+l*cos(radians(phi)), -0.1, 2.6+l*cos(radians(phi)), 0.1))
c.text(2.6+0.5*l*cos(radians(phi)), 0.2, '$\mathrm{d}x$', [text.halign.center])
c.stroke(path.line(2.6+0.5*l*cos(radians(phi)), -0.1,
                   2.6+0.5*l*cos(radians(phi)), 0))
c.text(2.6+0.5*l*cos(radians(phi)), -0.2, '$x_0$',
       [text.halign.center, text.valign.top])

c.writePDFfile()
