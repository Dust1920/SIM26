def arrow(text, position, text_position, ax):
    ax.annotate(text, xy=position, xytext=text_position,
                arrowprops=dict(facecolor='k', width=0.1, headwidth=2, headlength = 2),
                ha='center', va='center', fontsize=12,
                xycoords=ax.transAxes, weight = 'bold')
    return text_position

def text_block(content, pos, ax):
    ax.annotate(text = content,
                    xy=pos, 
                    fontsize=12,
                    horizontalalignment='center', 
                    verticalalignment='center',
                    weight = 'bold')
    return pos 