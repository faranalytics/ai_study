import { DEFAULT_PROJECT_SERVICE_ACCOUNT_KEY } from "./secrets.js";
import * as util from "node:util";
import * as openai from "openai";

const response = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${DEFAULT_PROJECT_SERVICE_ACCOUNT_KEY}`,
    },
    body: JSON.stringify({
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": `
                "A fedora is a hat with a soft brim and indented crown."
                "A baseball cap is a type of soft hat with a rounded crown and a stiff bill projecting in front."
                "A knit cap is a piece of knitted headwear designed to provide warmth in cold weather."
                "A hard hat is a type of helmet predominantly used in workplace environments such as industrial or construction sites to protect the head from injury due to falling objects, impact with other objects, debris, rain, and electric shock."
                "A cowboy hat is a high-crowned, wide-brimmed hat best known as the defining piece of attire for the North American cowboy."
                Answer is only a JSON array:{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "type": "array",
                "minItems": 1,
                "maxItems": 1,
                "items": {
                    "type": "object",
                    "properties": {
                        "hat": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "hex_color": {
                            "type": "number",
                            "pattern": "^#\\w{6}$"
                        },
                        "color": {
                            "type": "string",
                            "pattern": "^[^\\s]+$"
                        },
                        "cool": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "hat",
                        "description",
                        "color"
                    ]
                }
            }
                `,
            }, {
                "role": "user",
                "content": "I want the kind of hat not worn by Johnny Depp."
            }],
        "temperature": 0.7
    }),
});

// console.log(util.inspect((await response.json()), { showHidden: true, depth: null, colors: true }));
console.log((await response.json()).choices[0].message.content);