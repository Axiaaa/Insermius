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
    async def RockPaperScissors(self, ctx : InteractionContext, user : (Member | User) = None) -> None : 
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
        if user :
            for i in ctx.guild.members : 
                if i == user :
                    await ctx.send(
                        content=f"<@{user.id}>",
                        embed=Embed(
                            title=f"{ctx.author.display_name} wants to play Rock Paper Scissors",
                            description="You can accept the invitation with ✅ or press :negative_squared_cross_mark: if you don't want to !",
                            footer=EmbedFooter(f"By {ctx.author.display_name}")
                        ),
                        components=[
                            ActionRow(
                                Button(style=ButtonStyle.GREEN, emoji="✅", custom_id=f"rcs_{ctx.author_id}_{user}_true"),
                                Button(style=ButtonStyle.RED, emoji=":negative_squared_cross_mark:", custom_id=f"rcs_{ctx.author_id}_{user}_false")
                            )
                        ])
                    return
            await ctx.send("The user isn't correct", ephemeral=True)

        
        
        
    @listen()
    async def on_component(self, ctx ) :
        """
        Handler for when a user play vs the bot (slash_command_option empty
        
        customID format :
        
        rcs_AuthorID_UserChoice_solo -> ["rcs", "AuthorID", "("rock" || "papier" || "scissors")", "solo"]
        
        > rcs : 
            To identify the event we are listenning to. The number at the end is just to avoid having the same customID
        > AuthorID :
            Used to make the game personnal and not having everyone playing it
        > "rock" || "papier" || "scissors" 
            The user's choice
        > "solo" 
            The "gamemode"
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
                
    @listen()
    async def on_component(self, ctx ) :
        """
        Handler for when a user play vs the bot (slash_command_option empty
        
        customID format :
        
        rcs_User1ID_User1Choice_User2ID_User2Choice -> ["rcs", "User1ID", "User1Choice", "User2ID", "Uer2Choice"]
        
        > rcs : 
            To identify the event we are listenning to. The number at the end is just to avoid having the same customID
        > User 1 ID :
            First player's ID (the one who typed the command)
        > User 1 Choice ("rock" || "paper" || "scissors")
            The first user's choice
        > User 2 ID :
            First player's ID (the one who typed the command)
        > User 2 Choice ("rock" || "paper" || "scissors")
            The first user's choice
        """
        ctx : ComponentContext = ctx.ctx
        cid = ctx.custom_id.split("_")
        if cid[3] == "true" :
            await ctx.edit_origin(
                embed=Embed(
                    title="Rock Paper Scissors",
                    description=f"{ctx.author.display_name} and {cid[2]} are playing Rock Paper Scissors !",
                    footer=EmbedFooter(f"{ctx.author.display_name} VS {cid[2]}")
                ),
                components=[
                    ActionRow(
                        Button(style=ButtonStyle.BLUE, emoji="✂️", custom_id=f"rcs_{ctx.author_id}_{cid[2]}_scissors_{cid[4]}"),
                        Button(style=ButtonStyle.RED, emoji="📃", custom_id=f"rcs_{ctx.author_id}_{cid[2]}_paper_{cid[4]}"),
                        Button(style=ButtonStyle.GREEN, emoji="🪨", custom_id=f"rcs_{ctx.author_id}_{cid[2]}_rock_{cid[4]}")
                    )
                ]
            )
        elif cid[3] == "false" :
            await ctx.send("The user declined the invitation", ephemeral=True)
        
        
        
    @listen()
    async def on_component(self, ctx ) :
        """
        Handler for when a user play vs the bot (slash_command_option empty
        
        customID format :
        
        rcs_User1ID_User1Choice_User2ID_User2Choice -> ["rcs", "User1ID", "User1Choice", "User2ID", "Uer2Choice"]
        
        > rcs : 
            To identify the event we are listenning to. The number at the end is just to avoid having the same customID
        > User 1 ID :
            First player's ID (the one who typed the command)
        > User 1 Choice ("rock" || "paper" || "scissors")
            The first user's choice
        > User 2 ID :
            First player's ID (the one who typed the command)
        > User 2 Choice ("rock" || "paper" || "scissors")
            The first user's choice
        """
        ctx : ComponentContext = ctx.ctx
        cid = ctx.custom_id.split("_")
        if cid[0] == "rcs" :
            if cid[1] == str(ctx.author_id) or cid[3] == str(cid[ctx.author_id]) :
                print("test")