from interactions import *
import random

class RockScissorsPaper(Extension) :
    
    @slash_command(
        name="rockpaperscissors",
        description="Start a Rock Paper Scissors game !",
        options=[
            SlashCommandOption(
                name="user",
                description="Someone you want to play with",
                type=OptionType.USER,
                required=False                
            )
        ]
    )
    async def RockPaperScissors(self, ctx : InteractionContext, user : str = None) -> None : 
        if not user :
            await ctx.send(
                embed=Embed(
                    title="Rock Paper Scissors",
                    description="Make your choice by clicking on a button !",
                    footer=EmbedFooter(
                        text=f"{ctx.author.nickname} VS Insermius",
                        icon_url=ctx.author.avatar_url                    
                        )
                    ),
                components=[ActionRow(
                    Button(style=ButtonStyle.BLUE, emoji="✂️", custom_id=f"rcs_{ctx.author_id}_scissors_solo"),
                    Button(style=ButtonStyle.RED, emoji="📃", custom_id=f"rcs_{ctx.author_id}_paper_solo"),
                    Button(style=ButtonStyle.GREEN, emoji="🪨", custom_id=f"rcs_{ctx.author_id}_rock_solo"))
            ])
        
        
    @listen()
    async def on_component(self, ctx ) :
        """
        Handler for when a user play vs the bot (slash_command_option empty
        """
        ctx : ComponentContext = ctx.ctx
        cid = ctx.custom_id.split("_")
        if cid[0] == "rcs" :
            if cid[1] == str(ctx.author_id) and cid[3] == "solo" : 
                res = random.choice(["rock", "papier", "scissors"])
                if (res == cid[2]) : 
                    await ctx.edit_origin(
                        embed=Embed(
                            title="Draw !",
                            description=f"You choose {cid[2]} and I choose {res} !"                        
                        ),
                        components=[]  
                )
                elif ((res == "rock" and cid[2] == "paper") or (res == "paper" and cid[2] == "scissors") or (res == "scissors" and cid[2] == "rock")) : 
                    await ctx.edit_origin(
                        embed=Embed(
                            title="You won !",
                            description=f"You choose {cid[2]} and I choose {res} !",
                            color=(0, 255, 0)              
                        ),
                        components=[]
                )                    
                elif ((res == "paper" and cid[2] == "rock") or (res == "scissors" and cid[2] == "paper") or (res == "rock" and cid[2] == "scissors")) :
                    await ctx.edit_origin(
                        embed=Embed(
                            title="You lost !",
                            description=f"You choose {cid[2]} and I choose {res} !",
                            color=(255, 0, 0)             
                        ),
                        components=[]
                ) 
            else : 
                await ctx.send("This is not your game !", ephemeral=True)
                
                
    # @listen()
    # async def on_component(self, ctx) :
    #     """
    #     Handler for when a user play vs the bot (slash_command_option empty
    #     """
    #     ctx : ComponentContext = ctx.ctx
    #     cid = ctx.custom_id.split("_")
        
            
        