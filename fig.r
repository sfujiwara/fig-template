x <- 1:10
sin_x <- sin(x)
cos_x <- cos(x)


postscript(file="test.eps", width = 9, height = 9,
           horizontal = FALSE, onefile = FALSE, paper = "special",)

ylim <- c(-1.1, 1.1)

par(mar = c(5.5, 6.0, 4.1, 2)) #  余白の広さを行数で指定．下，左，上，右の順．
plot(x, sin_x, type="l", lty=1, col=1, lwd=7, xlab="x", ylab="f(x)", cex.lab=2.5, cex.axis=1.8, ylim=ylim)
par(new=TRUE)
plot(x, cos_x, type="l", lty=2, col=2, lwd=7, xlab="", ylab="", cex.lab=2.5, cex.axis=1.8, ylim=ylim)
points(x, cos_x, cex=4, lwd=3, col=3)

grid(col = "gray10")
legend("bottomright", legend=c("sin x", "cos x"),
       lty=1:2, col=1:2, lwd=5, bg="white", cex=1.8, inset=c(0.02,0.02), seg.len=5)

dev.off()
